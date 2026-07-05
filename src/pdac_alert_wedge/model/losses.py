from __future__ import annotations

import torch
from torch import nn


class WeightedIncidentLoss(nn.Module):
    def __init__(self, positive_weight: float = 20.0, calibration_weight: float = 0.02) -> None:
        super().__init__()
        self.register_buffer("positive_weight", torch.tensor(float(positive_weight)))
        self.calibration_weight = calibration_weight

    def forward(self, logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        positive_weight = self.get_buffer("positive_weight")
        bce = nn.functional.binary_cross_entropy_with_logits(logits, targets, pos_weight=positive_weight)
        risk = torch.sigmoid(logits)
        calibration = (risk.mean() - targets.mean()).pow(2)
        return bce + self.calibration_weight * calibration

class AlertBudgetLoss(nn.Module):
    def __init__(self, target_rate: float = 0.005, penalty: float = 1.0) -> None:
        super().__init__()
        self.target_rate = target_rate
        self.penalty = penalty

    def forward(self, risk: torch.Tensor) -> torch.Tensor:
        return self.penalty * (risk.mean() - self.target_rate).pow(2)

class ReachUtilityLoss(nn.Module):
    def __init__(self, adoption: float, completion: float, kappa: float) -> None:
        super().__init__()
        self.adoption = adoption
        self.completion = completion
        self.kappa = kappa

    def forward(self, sensitivity: torch.Tensor) -> torch.Tensor:
        return -(self.kappa * self.adoption * self.completion * sensitivity).mean()

def focal_binary_loss(logits: torch.Tensor, targets: torch.Tensor, gamma: float = 2.0, alpha: float = 0.25) -> torch.Tensor:
    probs = torch.sigmoid(logits)
    ce = nn.functional.binary_cross_entropy_with_logits(logits, targets, reduction="none")
    p_t = probs * targets + (1.0 - probs) * (1.0 - targets)
    alpha_t = alpha * targets + (1.0 - alpha) * (1.0 - targets)
    return (alpha_t * (1.0 - p_t).pow(gamma) * ce).mean()

def pairwise_rank_loss(scores: torch.Tensor, targets: torch.Tensor, margin: float = 0.05) -> torch.Tensor:
    pos = scores[targets.squeeze(-1) > 0.5]
    neg = scores[targets.squeeze(-1) <= 0.5]
    if pos.numel() == 0 or neg.numel() == 0:
        return scores.sum() * 0.0
    diffs = margin - pos.view(-1, 1) + neg.view(1, -1)
    return torch.relu(diffs).mean()
