# PDAC Alert Wedge

This repository contains a compact Python implementation for experimenting with
pancreatic cancer early-warning workflows built from structured EHR sequences.
It combines a temporal risk model, synthetic data utilities, operating-point
analysis, stepped-wedge deployment summaries, pathway reach calculations, and
basic cost-effectiveness helpers.

The code is intended for reproducible method checks and local development. It
does not include protected clinical datasets or trained production weights.

## What Is Included

- A PyTorch temporal Transformer for patient-level risk scoring.
- Synthetic EHR-like sequence generation for smoke tests and examples.
- Training and evaluation command modules.
- Alert threshold, AUROC, sensitivity, specificity, and subgroup utilities.
- Deployment wedge, pathway lever, and economic analysis modules.
- Minimal tests under `checks/`.

## Repository Layout

```text
src/pdac_alert_wedge/
  analysis/      Metrics, subgroup summaries, wedge analysis, cost utilities
  commands/      CLI-style entry points for train, evaluate, and audit
  data/          Synthetic data generation and tensor encoding
  model/         Temporal risk model and loss functions
  training/      Training loop and checkpoint writing
  records.py     Shared typed configuration records

configs/         Example model and training configuration
scripts/         Shell wrappers for common commands
checks/          Pytest checks
```

## Setup

Use Python 3.11 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

The pinned dependencies are listed in `pyproject.toml`, with equivalent package
lists in `requirements.txt` and `environment.yml`.

## Run The Main Workflows

Train a small local model run:

```bash
python -m pdac_alert_wedge.commands.train --config configs/main.yaml
```

Evaluate a synthetic cohort:

```bash
python -m pdac_alert_wedge.commands.evaluate --config configs/main.yaml
```

Run the audit-style analysis bundle:

```bash
python -m pdac_alert_wedge.commands.audit
```

The shell wrappers in `scripts/` call the same module entry points.

## Configuration

`configs/main.yaml` controls the model shape, alert percentiles, synthetic
training loop parameters, and checkpoint location. The default settings are
small enough for local verification while preserving the same interfaces used by
the package modules.

## Data And Weights

No public patient-level dataset is shipped with this repository. The package
uses synthetic records for tests and command examples. Production clinical data,
de-identified analytic extracts, and model weights require the appropriate data
use, privacy, and governance review before access.

## Development Checks

```bash
pytest
```

The tests exercise data encoding, model training, and analysis helpers. They are
designed to verify package behavior without external datasets.

## Notes

This code is research and analysis infrastructure. It is not a standalone
clinical decision support product and should not be used for patient care
without independent validation, deployment controls, monitoring, and regulatory
review.
