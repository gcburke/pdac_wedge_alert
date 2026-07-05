from __future__ import annotations

import torch

from pdac_alert_wedge.data.encode import EhrSequenceDataset
from pdac_alert_wedge.data.simulate import compact_bundle
from pdac_alert_wedge.model.temporal import TemporalRiskTransformer
from pdac_alert_wedge.records import ModelConfig


def test_sequence_model_forward() -> None:
    bundle = compact_bundle(n=48, max_events=16)
    dataset = EhrSequenceDataset(bundle.events, bundle.outcomes, vocabulary_size=128, max_events=16)
    codes, values, months, mask, target = dataset[0]
    model = TemporalRiskTransformer(ModelConfig(vocabulary_size=128, feature_size=8, model_dim=16, heads=2, layers=1, feedforward=32, dropout=0.0, max_events=16))
    out = model(codes.unsqueeze(0), values.unsqueeze(0), months.unsqueeze(0), mask.unsqueeze(0))
    assert out.risk.shape == (1, 1)
    assert torch.isfinite(out.risk).all()
    assert target.shape == (1,)
