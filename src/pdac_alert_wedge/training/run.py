from __future__ import annotations

import os
import random
from dataclasses import dataclass
from pathlib import Path
from typing import cast

import numpy as np
import torch
import yaml
from torch.utils.data import DataLoader

from pdac_alert_wedge.data.encode import EhrSequenceDataset, collate_sequences
from pdac_alert_wedge.data.simulate import compact_bundle
from pdac_alert_wedge.model.losses import WeightedIncidentLoss
from pdac_alert_wedge.model.temporal import TemporalRiskTransformer
from pdac_alert_wedge.records import ModelConfig, TrainConfig


@dataclass(frozen=True)
class TrainSummary:
    first_loss: float
    last_loss: float
    steps: int
    checkpoint: str


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

def load_yaml(path: str | Path) -> dict[str, object]:
    with Path(path).open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(str(path))
    return data

def model_config(data: dict[str, object]) -> ModelConfig:
    values = cast(dict[str, int | float | str], data)
    return ModelConfig(vocabulary_size=int(values["vocabulary_size"]), feature_size=int(values["feature_size"]), model_dim=int(values["model_dim"]), heads=int(values["heads"]), layers=int(values["layers"]), feedforward=int(values["feedforward"]), dropout=float(values["dropout"]), max_events=int(values["max_events"]))

def train_config(data: dict[str, object]) -> TrainConfig:
    values = cast(dict[str, int | float | str], data)
    return TrainConfig(seed=int(values["seed"]), batch_size=int(values["batch_size"]), grad_accum=int(values["grad_accum"]), epochs=int(values["epochs"]), learning_rate=float(values["learning_rate"]), weight_decay=float(values["weight_decay"]), warmup_steps=int(values["warmup_steps"]), scheduler=str(values["scheduler"]), precision=str(values["precision"]), world_size=int(values["world_size"]), checkpoint_dir=str(values["checkpoint_dir"]))

def atomic_save(payload: dict[str, object], path: str | Path) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(target.suffix + ".tmp")
    torch.save(payload, tmp)
    os.replace(tmp, target)

def train_steps(config_path: str | Path, steps: int = 2) -> TrainSummary:
    raw = load_yaml(config_path)
    mcfg = model_config(raw)
    tcfg = train_config(raw)
    set_seed(tcfg.seed)
    bundle = compact_bundle(seed=tcfg.seed, n=max(tcfg.batch_size * 4, 64), max_events=mcfg.max_events)
    dataset = EhrSequenceDataset(bundle.events, bundle.outcomes, vocabulary_size=mcfg.vocabulary_size, max_events=mcfg.max_events)
    loader = DataLoader(dataset, batch_size=min(tcfg.batch_size, len(dataset)), shuffle=True, collate_fn=collate_sequences)
    model = TemporalRiskTransformer(mcfg)
    loss_fn = WeightedIncidentLoss(positive_weight=10.0)
    optimizer = torch.optim.AdamW(model.parameters(), lr=tcfg.learning_rate, weight_decay=tcfg.weight_decay)
    losses: list[float] = []
    iterator = iter(loader)
    for _step in range(steps):
        try:
            batch = next(iterator)
        except StopIteration:
            iterator = iter(loader)
            batch = next(iterator)
        optimizer.zero_grad(set_to_none=True)
        output = model(batch.codes, batch.values, batch.months, batch.mask)
        loss = loss_fn(output.logits, batch.targets)
        loss.backward()
        optimizer.step()
        losses.append(float(loss.detach().cpu()))
    ckpt = Path(tcfg.checkpoint_dir) / "latest.pt"
    atomic_save({"model": model.state_dict(), "seed": tcfg.seed, "losses": losses, "config": raw}, ckpt)
    return TrainSummary(first_loss=losses[0], last_loss=losses[-1], steps=len(losses), checkpoint=str(ckpt))
