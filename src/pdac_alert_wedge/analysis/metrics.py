from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy import stats
from sklearn.metrics import roc_auc_score


@dataclass(frozen=True)
class BinaryOperatingPoint:
    threshold: float
    sensitivity: float
    specificity: float
    ppv: float
    npv: float
    alerts: int

@dataclass(frozen=True)
class CalibrationSummary:
    slope: float
    intercept: float
    hosmer_lemeshow_p: float

@dataclass(frozen=True)
class BootstrapInterval:
    estimate: float
    lower: float
    upper: float


def auroc(y_true: np.ndarray, scores: np.ndarray) -> float:
    if len(np.unique(y_true)) < 2:
        return float("nan")
    return float(roc_auc_score(y_true, scores))

def percentile_threshold(scores: np.ndarray, percentile: float) -> float:
    return float(np.percentile(scores, percentile))

def operating_point(y_true: np.ndarray, scores: np.ndarray, threshold: float) -> BinaryOperatingPoint:
    pred = scores >= threshold
    y = y_true.astype(bool)
    tp = int(np.logical_and(pred, y).sum())
    fp = int(np.logical_and(pred, ~y).sum())
    tn = int(np.logical_and(~pred, ~y).sum())
    fn = int(np.logical_and(~pred, y).sum())
    sensitivity = tp / max(tp + fn, 1)
    specificity = tn / max(tn + fp, 1)
    ppv = tp / max(tp + fp, 1)
    npv = tn / max(tn + fn, 1)
    return BinaryOperatingPoint(threshold=threshold, sensitivity=float(sensitivity), specificity=float(specificity), ppv=float(ppv), npv=float(npv), alerts=int(pred.sum()))

def bootstrap_auc(y_true: np.ndarray, scores: np.ndarray, draws: int = 500, seed: int = 1729) -> BootstrapInterval:
    rng = np.random.default_rng(seed)
    values: list[float] = []
    n = len(y_true)
    for _ in range(draws):
        idx = rng.integers(0, n, size=n)
        value = auroc(y_true[idx], scores[idx])
        if np.isfinite(value):
            values.append(value)
    arr = np.array(values, dtype=float)
    return BootstrapInterval(estimate=auroc(y_true, scores), lower=float(np.percentile(arr, 2.5)), upper=float(np.percentile(arr, 97.5)))

def calibration_summary(y_true: np.ndarray, scores: np.ndarray, groups: int = 10) -> CalibrationSummary:
    eps = 1e-6
    logits = np.log(np.clip(scores, eps, 1 - eps) / np.clip(1 - scores, eps, 1 - eps))
    slope, intercept, _, _, _ = stats.linregress(logits, y_true)
    order = np.argsort(scores)
    bins = np.array_split(order, groups)
    chi = 0.0
    dof = max(groups - 2, 1)
    for idx in bins:
        observed = y_true[idx].sum()
        expected = scores[idx].sum()
        denom = max(expected * (1 - expected / max(len(idx), 1)), 1e-6)
        chi += float((observed - expected) ** 2 / denom)
    p = float(1 - stats.chi2.cdf(chi, dof))
    return CalibrationSummary(slope=float(slope), intercept=float(intercept), hosmer_lemeshow_p=p)

def stage_shift(control_early: int, control_total: int, intervention_early: int, intervention_total: int) -> float:
    return intervention_early / max(intervention_total, 1) - control_early / max(control_total, 1)

def odds_ratio(a: int, b: int, c: int, d: int) -> BootstrapInterval:
    cells = np.array([a, b, c, d], dtype=float) + 0.5
    value = cells[0] * cells[3] / (cells[1] * cells[2])
    se = np.sqrt(np.sum(1.0 / cells))
    lower = np.exp(np.log(value) - 1.96 * se)
    upper = np.exp(np.log(value) + 1.96 * se)
    return BootstrapInterval(estimate=float(value), lower=float(lower), upper=float(upper))

def quantile_ci(values: np.ndarray, q: float = 0.5, draws: int = 1000, seed: int = 1729) -> BootstrapInterval:
    rng = np.random.default_rng(seed)
    reps = [float(np.quantile(values[rng.integers(0, len(values), len(values))], q)) for _ in range(draws)]
    return BootstrapInterval(estimate=float(np.quantile(values, q)), lower=float(np.percentile(reps, 2.5)), upper=float(np.percentile(reps, 97.5)))
