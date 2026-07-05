from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ReachState:
    sensitivity: float
    adoption: float
    completion: float
    kappa: float

@dataclass(frozen=True)
class Lever:
    name: str
    current: float
    ceiling: float
    marginal_cost: float

@dataclass(frozen=True)
class LeverRanking:
    name: str
    headroom: float
    attainable_gain: float
    gain_per_cost: float


def effective_reach(sensitivity: float, adoption: float, completion: float) -> float:
    return float(sensitivity * adoption * completion)

def stage_gain(state: ReachState) -> float:
    return float(state.kappa * state.sensitivity * state.adoption * state.completion)

def unit_elasticity(state: ReachState, factor: str, relative_delta: float) -> float:
    values = {"sensitivity": state.sensitivity, "adoption": state.adoption, "completion": state.completion, "kappa": state.kappa}
    if factor not in values:
        raise ValueError(factor)
    values[factor] *= 1.0 + relative_delta
    return stage_gain(ReachState(sensitivity=values["sensitivity"], adoption=values["adoption"], completion=values["completion"], kappa=values["kappa"]))

def rank_levers(state: ReachState, levers: list[Lever]) -> list[LeverRanking]:
    base = stage_gain(state)
    rows: list[LeverRanking] = []
    for lever in levers:
        headroom = max(lever.ceiling / max(lever.current, 1e-9) - 1.0, 0.0)
        gain = base * headroom
        rows.append(LeverRanking(name=lever.name, headroom=float(headroom), attainable_gain=float(gain), gain_per_cost=float(gain / max(lever.marginal_cost, 1e-9))))
    return sorted(rows, key=lambda row: row.gain_per_cost, reverse=True)

def threshold_at_budget(scores: np.ndarray, budget_fraction: float) -> float:
    percentile = 100.0 * (1.0 - budget_fraction)
    return float(np.percentile(scores, percentile))

def alert_volume(scores: np.ndarray, threshold: float) -> int:
    return int((scores >= threshold).sum())

def budget_optimal_threshold(scores: np.ndarray, max_alerts: int) -> float:
    if max_alerts <= 0:
        return float(np.inf)
    order = np.sort(scores)
    index = max(len(order) - max_alerts, 0)
    return float(order[index])

def dependence_lower_bound(sensitivity: float, adoption: float, completion: float) -> float:
    return effective_reach(sensitivity, adoption, completion)

def reach_interval(samples: np.ndarray) -> tuple[float, float, float]:
    reach = samples[:, 0] * samples[:, 1] * samples[:, 2]
    return float(np.mean(reach)), float(np.percentile(reach, 2.5)), float(np.percentile(reach, 97.5))
