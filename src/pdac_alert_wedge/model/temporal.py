from __future__ import annotations

from dataclasses import dataclass

import torch
from torch import nn

from pdac_alert_wedge.records import ModelConfig


@dataclass(frozen=True)
class RiskOutput:
    logits: torch.Tensor
    risk: torch.Tensor
    attention_mask: torch.Tensor

class RecencyEncoding(nn.Module):
    def __init__(self, model_dim: int) -> None:
        super().__init__()
        self.scale = nn.Parameter(torch.ones(model_dim))
        self.bias = nn.Parameter(torch.zeros(model_dim))

    def forward(self, months: torch.Tensor) -> torch.Tensor:
        recency = (36.0 - months).clamp(min=0.0, max=36.0) / 36.0
        base = recency.unsqueeze(-1)
        return base * self.scale + self.bias

class ValueProjector(nn.Module):
    def __init__(self, model_dim: int) -> None:
        super().__init__()
        self.net = nn.Sequential(nn.Linear(1, model_dim), nn.GELU(), nn.Linear(model_dim, model_dim))

    def forward(self, values: torch.Tensor) -> torch.Tensor:
        projected = self.net(values.unsqueeze(-1))
        return torch.as_tensor(projected)

class TemporalRiskTransformer(nn.Module):
    def __init__(self, config: ModelConfig) -> None:
        super().__init__()
        self.config = config
        self.code_embedding = nn.Embedding(config.vocabulary_size, config.model_dim, padding_idx=0)
        self.recency = RecencyEncoding(config.model_dim)
        self.value_projector = ValueProjector(config.model_dim)
        layer = nn.TransformerEncoderLayer(d_model=config.model_dim, nhead=config.heads, dim_feedforward=config.feedforward, dropout=config.dropout, batch_first=True, activation="gelu", norm_first=True)
        self.encoder = nn.TransformerEncoder(layer, num_layers=config.layers)
        self.norm = nn.LayerNorm(config.model_dim)
        self.head = nn.Sequential(nn.Linear(config.model_dim, config.model_dim), nn.GELU(), nn.Dropout(config.dropout), nn.Linear(config.model_dim, 1))

    def forward(self, codes: torch.Tensor, values: torch.Tensor, months: torch.Tensor, mask: torch.Tensor) -> RiskOutput:
        padding = mask <= 0
        x = self.code_embedding(codes) + self.recency(months) + self.value_projector(values)
        encoded = self.encoder(x, src_key_padding_mask=padding)
        weights = mask / mask.sum(dim=1, keepdim=True).clamp_min(1.0)
        pooled = (encoded * weights.unsqueeze(-1)).sum(dim=1)
        logits = self.head(self.norm(pooled))
        return RiskOutput(logits=logits, risk=torch.sigmoid(logits), attention_mask=weights)

    def score(self, codes: torch.Tensor, values: torch.Tensor, months: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
        with torch.no_grad():
            return self.forward(codes, values, months, mask).risk.squeeze(-1)

class PathwayCalibrator(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.temperature = nn.Parameter(torch.ones(()))
        self.bias = nn.Parameter(torch.zeros(()))

    def forward(self, logits: torch.Tensor) -> torch.Tensor:
        return torch.sigmoid(logits / self.temperature.clamp_min(0.05) + self.bias)

class MonotoneThresholdLayer(nn.Module):
    def __init__(self, threshold: float, softness: float = 0.01) -> None:
        super().__init__()
        self.threshold = nn.Parameter(torch.tensor(float(threshold)), requires_grad=False)
        self.softness = nn.Parameter(torch.tensor(float(softness)), requires_grad=False)

    def forward(self, risk: torch.Tensor) -> torch.Tensor:
        return torch.sigmoid((risk - self.threshold) / self.softness.clamp_min(1e-6))

def build_model(config: ModelConfig) -> TemporalRiskTransformer:
    return TemporalRiskTransformer(config)

def count_parameters(model: nn.Module) -> int:
    return int(sum(p.numel() for p in model.parameters() if p.requires_grad))
