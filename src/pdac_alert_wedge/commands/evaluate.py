from __future__ import annotations

import argparse
import logging

import numpy as np

from pdac_alert_wedge.analysis.metrics import auroc, operating_point, percentile_threshold
from pdac_alert_wedge.data.encode import patient_feature_matrix
from pdac_alert_wedge.data.simulate import compact_bundle

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("pdac_alert_wedge.evaluate")

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    bundle = compact_bundle(n=256)
    x, y, _ = patient_feature_matrix(bundle.events, bundle.outcomes)
    raw = x.sum(axis=1)
    scores = 1.0 / (1.0 + np.exp(-(raw - raw.mean()) / max(raw.std(), 1e-6)))
    threshold = percentile_threshold(scores, 99.5)
    point = operating_point(y, scores, threshold)
    LOGGER.info("config %s auroc %.6f sensitivity %.6f specificity %.6f alerts %s", args.config, auroc(y, scores), point.sensitivity, point.specificity, point.alerts)

if __name__ == "__main__":
    main()
