from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

from pdac_alert_wedge.records import EffectEstimate, require_columns


@dataclass(frozen=True)
class WedgeResult:
    primary: EffectEstimate
    period_effects: pd.DataFrame
    icc_within: float
    secular_trend: float


def design_matrix(frame: pd.DataFrame, period_mode: str = "categorical") -> pd.DataFrame:
    require_columns(frame, ["intervention", "period", "cluster"])
    x = pd.DataFrame({"intervention": frame["intervention"].astype(float)})
    if period_mode == "categorical":
        dummies = pd.get_dummies(frame["period"].astype(str), prefix="period", drop_first=True, dtype=float)
        x = pd.concat([x, dummies], axis=1)
    elif period_mode == "linear":
        x["period_linear"] = frame["period"].astype(float)
    elif period_mode == "quadratic":
        period = frame["period"].astype(float)
        x["period_linear"] = period
        x["period_quadratic"] = period * period
    else:
        raise ValueError(period_mode)
    cluster = pd.get_dummies(frame["cluster"].astype(str), prefix="cluster", drop_first=True, dtype=float)
    x = pd.concat([x, cluster], axis=1)
    return sm.add_constant(x, has_constant="add")

def logistic_effect(frame: pd.DataFrame, period_mode: str = "categorical") -> EffectEstimate:
    require_columns(frame, ["early_stage", "intervention", "period", "cluster", "pdac"])
    work = frame[frame["pdac"] == 1].copy()
    x = design_matrix(work, period_mode=period_mode)
    y = work["early_stage"].astype(float)
    try:
        model = sm.Logit(y, x).fit(disp=False, maxiter=200)
    except Exception:
        try:
            model = sm.Logit(y, x).fit_regularized(alpha=0.25, disp=False, maxiter=200)
        except Exception:
            table = pd.crosstab(work["intervention"], work["early_stage"])
            for r in [0, 1]:
                for c in [0, 1]:
                    if r not in table.index or c not in table.columns:
                        table.loc[r, c] = 0
            a = float(table.loc[1, 1] + 0.5)
            b = float(table.loc[1, 0] + 0.5)
            c_cell = float(table.loc[0, 1] + 0.5)
            d = float(table.loc[0, 0] + 0.5)
            value = a * d / (b * c_cell)
            se = float(np.sqrt(1 / a + 1 / b + 1 / c_cell + 1 / d))
            z = float(np.log(value) / se)
            p = float(2 * (1 - stats.norm.cdf(abs(z))))
            return EffectEstimate(estimate=float(value), lower=float(np.exp(np.log(value) - 1.96 * se)), upper=float(np.exp(np.log(value) + 1.96 * se)), p_value=p, label=f"logit_{period_mode}_fallback")
    beta = float(model.params["intervention"])
    se = float(model.bse["intervention"])
    p = float(model.pvalues["intervention"])
    return EffectEstimate(estimate=float(np.exp(beta)), lower=float(np.exp(beta - 1.96 * se)), upper=float(np.exp(beta + 1.96 * se)), p_value=p, label=f"logit_{period_mode}")

def period_interactions(frame: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, float | int]] = []
    for period, part in frame[frame["pdac"] == 1].groupby("period"):
        if part["intervention"].nunique() < 2 or part["early_stage"].nunique() < 2:
            rows.append({"period": int(period), "or": float("nan"), "lower": float("nan"), "upper": float("nan"), "cases": len(part)})
            continue
        table = pd.crosstab(part["intervention"], part["early_stage"])
        for r in [0, 1]:
            for c in [0, 1]:
                if r not in table.index or c not in table.columns:
                    table.loc[r, c] = 0
        a = float(table.loc[1, 1] + 0.5)
        b = float(table.loc[1, 0] + 0.5)
        c_cell = float(table.loc[0, 1] + 0.5)
        d = float(table.loc[0, 0] + 0.5)
        value = a * d / (b * c_cell)
        se = np.sqrt(1 / a + 1 / b + 1 / c_cell + 1 / d)
        rows.append({"period": int(period), "or": float(value), "lower": float(np.exp(np.log(value) - 1.96 * se)), "upper": float(np.exp(np.log(value) + 1.96 * se)), "cases": len(part)})
    return pd.DataFrame(rows)

def estimate_icc(frame: pd.DataFrame) -> float:
    work = frame[frame["pdac"] == 1]
    cluster_means = work.groupby("cluster")["early_stage"].mean()
    overall = work["early_stage"].mean()
    between = float(((cluster_means - overall) ** 2).mean())
    within = float(work.groupby("cluster")["early_stage"].var().fillna(0.0).mean())
    return between / max(between + within, 1e-9)

def secular_trend(frame: pd.DataFrame) -> float:
    work = frame[frame["pdac"] == 1]
    grouped = work.groupby("period")["early_stage"].mean().reset_index()
    if len(grouped) < 2:
        return 0.0
    slope, _, _, _, _ = stats.linregress(grouped["period"], grouped["early_stage"])
    return float(slope)

def analyze_wedge(frame: pd.DataFrame) -> WedgeResult:
    primary = logistic_effect(frame, "categorical")
    periods = period_interactions(frame)
    return WedgeResult(primary=primary, period_effects=periods, icc_within=estimate_icc(frame), secular_trend=secular_trend(frame))

def subgroup_table(frame: pd.DataFrame, subgroup: str) -> pd.DataFrame:
    require_columns(frame, [subgroup, "pdac", "early_stage", "intervention"])
    rows: list[dict[str, object]] = []
    for name, part in frame[frame["pdac"] == 1].groupby(subgroup):
        control = part[part["intervention"] == 0]
        intervention = part[part["intervention"] == 1]
        ce = int(control["early_stage"].sum())
        ie = int(intervention["early_stage"].sum())
        ct = len(control)
        it = len(intervention)
        cp = ce / max(ct, 1)
        ip = ie / max(it, 1)
        a = ie + 0.5
        b = it - ie + 0.5
        c = ce + 0.5
        d = ct - ce + 0.5
        or_value = a * d / (b * c)
        rows.append({"subgroup": subgroup, "level": str(name), "n": len(part), "control": cp, "intervention": ip, "shift": ip - cp, "or": float(or_value)})
    return pd.DataFrame(rows)

def permutation_activation_test(frame: pd.DataFrame, draws: int = 1000, seed: int = 1729) -> float:
    rng = np.random.default_rng(seed)
    observed = logistic_effect(frame).estimate
    clusters = sorted(frame["cluster"].unique())
    activations = frame.groupby("cluster")["intervention"].sum().to_dict()
    count = 0
    valid = 0
    for _ in range(draws):
        shuffled = dict(zip(clusters, rng.permutation([activations[c] for c in clusters]), strict=False))
        temp = frame.copy()
        temp["intervention"] = [int(row.period > 6 - shuffled[row.cluster]) for row in temp.itertuples(index=False)]
        try:
            effect = logistic_effect(temp).estimate
        except Exception:
            continue
        valid += 1
        count += int(effect >= observed)
    return (count + 1) / max(valid + 1, 1)

def exclude_transition(frame: pd.DataFrame) -> pd.DataFrame:
    activation = frame.groupby("cluster").apply(lambda p: int(p.loc[p["intervention"] == 1, "period"].min()) if (p["intervention"] == 1).any() else 99, include_groups=False)
    mask = []
    for row in frame.itertuples(index=False):
        start = int(activation.loc[row.cluster])
        mask.append(not (row.period == start and row.intervention == 1))
    return frame.loc[mask].reset_index(drop=True)
