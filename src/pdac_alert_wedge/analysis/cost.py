from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from pdac_alert_wedge.records import CostParameters, CostResult


@dataclass(frozen=True)
class MarkovTrace:
    early: np.ndarray
    late: np.ndarray
    dead: np.ndarray
    cost: np.ndarray
    qaly: np.ndarray


def discount_weights(years: int, rate: float) -> np.ndarray:
    return np.array([(1.0 / ((1.0 + rate) ** year)) for year in range(years)], dtype=float)

def simulate_markov(early_cases: float, late_cases: float, params: CostParameters, years: int = 20) -> MarkovTrace:
    early = np.zeros(years)
    late = np.zeros(years)
    dead = np.zeros(years)
    cost = np.zeros(years)
    qaly = np.zeros(years)
    early[0] = early_cases
    late[0] = late_cases
    for year in range(years):
        if year > 0:
            early[year] = early[year - 1] * 0.82
            late[year] = late[year - 1] * 0.45
            dead[year] = early_cases + late_cases - early[year] - late[year]
        cost[year] = early[year] * params.treatment_stage_i_ii + late[year] * params.treatment_stage_iii_iv
        qaly[year] = early[year] * params.qaly_stage_i_ii + late[year] * params.qaly_stage_iii_iv
    weights = discount_weights(years, params.discount)
    return MarkovTrace(early=early, late=late, dead=dead, cost=cost * weights, qaly=qaly * weights)

def diagnostic_cost(alerts: float, completed: float, params: CostParameters) -> float:
    return params.ai_infrastructure + alerts * 0.714 * params.ct_cost + completed * 0.186 * params.biopsy_cost + completed * 0.449 * params.eus_cost

def icer(population: str, screened: int, stage_shift: float, alerts: int, completed: int, params: CostParameters, probability_ce: float) -> CostResult:
    additional_early = screened * stage_shift
    nns = screened / max(additional_early, 1e-9)
    usual = simulate_markov(early_cases=screened * 0.153, late_cases=screened * 0.847, params=params)
    aided = simulate_markov(early_cases=screened * (0.153 + stage_shift), late_cases=screened * (0.847 - stage_shift), params=params)
    added_cost = float(aided.cost.sum() + diagnostic_cost(alerts, completed, params) - usual.cost.sum())
    added_qaly = float(aided.qaly.sum() - usual.qaly.sum())
    value = added_cost / max(added_qaly, 1e-9)
    cost_case = added_cost / max(additional_early, 1e-9)
    return CostResult(population=population, icer=float(value), nns=float(nns), qalys_per_1000=float(added_qaly / screened * 1000.0), cost_per_case=float(cost_case), probability_cost_effective=float(probability_ce))

def default_cost_parameters() -> CostParameters:
    return CostParameters(ai_infrastructure=512000.0, ct_cost=840.0, eus_cost=2600.0, biopsy_cost=3400.0, treatment_stage_i_ii=42000.0, treatment_stage_iii_iv=78000.0, qaly_stage_i_ii=0.74, qaly_stage_iii_iv=0.38, discount=0.03)

def probabilistic_icer(seed: int, draws: int, screened: int, stage_shift: float, alerts: int, completed: int, params: CostParameters, threshold: float = 100000.0) -> float:
    rng = np.random.default_rng(seed)
    count = 0
    for _ in range(draws):
        sampled = CostParameters(ai_infrastructure=float(rng.normal(params.ai_infrastructure, params.ai_infrastructure * 0.08)), ct_cost=float(rng.normal(params.ct_cost, params.ct_cost * 0.12)), eus_cost=float(rng.normal(params.eus_cost, params.eus_cost * 0.12)), biopsy_cost=float(rng.normal(params.biopsy_cost, params.biopsy_cost * 0.12)), treatment_stage_i_ii=float(rng.normal(params.treatment_stage_i_ii, params.treatment_stage_i_ii * 0.15)), treatment_stage_iii_iv=float(rng.normal(params.treatment_stage_iii_iv, params.treatment_stage_iii_iv * 0.15)), qaly_stage_i_ii=float(rng.normal(params.qaly_stage_i_ii, 0.05)), qaly_stage_iii_iv=float(rng.normal(params.qaly_stage_iii_iv, 0.05)), discount=params.discount)
        result = icer("sample", screened, max(float(rng.normal(stage_shift, 0.015)), 0.001), alerts, completed, sampled, 0.0)
        count += int(result.icer <= threshold)
    return count / max(draws, 1)
