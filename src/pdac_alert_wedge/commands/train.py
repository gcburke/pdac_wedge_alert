from __future__ import annotations

import argparse
import logging

from pdac_alert_wedge.training.run import train_steps

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("pdac_alert_wedge.train")

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--steps", type=int, default=20)
    args = parser.parse_args()
    summary = train_steps(args.config, steps=args.steps)
    LOGGER.info("loss %.6f %.6f steps %s checkpoint %s", summary.first_loss, summary.last_loss, summary.steps, summary.checkpoint)

if __name__ == "__main__":
    main()
