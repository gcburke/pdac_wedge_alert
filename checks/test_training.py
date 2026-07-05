from __future__ import annotations

from pdac_alert_wedge.training.run import train_steps


def test_training_two_steps() -> None:
    summary = train_steps("configs/check.yaml", steps=2)
    assert summary.steps == 2
    assert summary.first_loss > 0.0
    assert summary.last_loss > 0.0
