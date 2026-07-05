from __future__ import annotations

import numpy as np

from pdac_alert_wedge.analysis.metrics import operating_point, percentile_threshold
from pdac_alert_wedge.analysis.pathway import ReachState, stage_gain, unit_elasticity
from pdac_alert_wedge.analysis.wedge import analyze_wedge, subgroup_table
from pdac_alert_wedge.data.simulate import compact_bundle


def test_metrics_and_pathway() -> None:
    y = np.array([0, 0, 1, 1])
    scores = np.array([0.1, 0.2, 0.8, 0.9])
    threshold = percentile_threshold(scores, 50.0)
    point = operating_point(y, scores, threshold)
    state = ReachState(sensitivity=0.384, adoption=0.623, completion=0.783, kappa=1.0)
    assert point.sensitivity == 1.0
    assert stage_gain(state) > 0.0
    assert unit_elasticity(state, "adoption", 0.1) > stage_gain(state)


def test_wedge_outputs() -> None:
    bundle = compact_bundle(n=500)
    result = analyze_wedge(bundle.deployment)
    table = subgroup_table(bundle.deployment, "platform")
    assert result.primary.estimate > 0.0
    assert len(table) >= 1
