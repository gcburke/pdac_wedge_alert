from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from pdac_alert_wedge.records import EhrPlatform, EventKind, age_group


@dataclass(frozen=True)
class SyntheticBundle:
    events: pd.DataFrame
    outcomes: pd.DataFrame
    deployment: pd.DataFrame
    sites: pd.DataFrame

class EhrSimulator:
    def __init__(self, seed: int = 1729) -> None:
        self.rng = np.random.default_rng(seed)

    def site_table(self, sites: int = 20) -> pd.DataFrame:
        platforms = [EhrPlatform.epic.value] * 14 + [EhrPlatform.cerner.value] * 4 + [EhrPlatform.legacy.value] * 2
        regions = ["A"] * 6 + ["B"] * 5 + ["C"] * 5 + ["D"] * 4
        settings = ["urban"] * 8 + ["suburban"] * 7 + ["rural"] * 5
        volume = self.rng.integers(6800, 12400, size=sites)
        return pd.DataFrame({"site_id": np.arange(sites), "platform": platforms[:sites], "region": regions[:sites], "setting": settings[:sites], "volume": volume})

    def activation_table(self, sites: pd.DataFrame) -> pd.DataFrame:
        sequence = np.repeat(np.arange(1, 7), [4, 4, 3, 3, 3, 3])[: len(sites)]
        out = sites.copy()
        out["sequence"] = sequence
        out["activation_period"] = sequence
        return out

    def patients(self, n: int, sites: pd.DataFrame) -> pd.DataFrame:
        site_ids = self.rng.choice(sites["site_id"].to_numpy(), size=n, replace=True)
        site_map = sites.set_index("site_id")
        ages = np.clip(self.rng.normal(68, 11, size=n).round(), 40, 95).astype(int)
        sex = self.rng.choice(["male", "female"], size=n, p=[0.53, 0.47])
        race = self.rng.choice(["white_non_hispanic", "black", "hispanic", "asian_other"], size=n, p=[0.65, 0.15, 0.12, 0.08])
        nod = self.rng.binomial(1, 0.066, size=n)
        return pd.DataFrame({"patient_id": [f"P{i:07d}" for i in range(n)], "site_id": site_ids, "age": ages, "sex": sex, "race_ethnicity": race, "nod": nod, "platform": [site_map.loc[s, "platform"] for s in site_ids]})

    def events_for_patients(self, patients: pd.DataFrame, max_events: int = 80) -> pd.DataFrame:
        rows: list[dict[str, object]] = []
        diagnosis_codes = ["E11", "R63.4", "K86", "R10", "C25", "K83", "R17", "Z00", "I10", "E78"]
        procedure_codes = ["74177", "43259", "48150", "99213", "80053", "83036"]
        medications = ["metformin", "statin", "ppi", "insulin", "ace_inhibitor"]
        for row in patients.itertuples(index=False):
            count = int(self.rng.integers(max(8, max_events // 4), max_events + 1))
            months = np.sort(self.rng.integers(0, 36, size=count))
            for month in months:
                kind = self.rng.choice([EventKind.diagnosis.value, EventKind.procedure.value, EventKind.laboratory.value, EventKind.medication.value], p=[0.42, 0.18, 0.28, 0.12])
                if kind == EventKind.diagnosis.value:
                    code = str(self.rng.choice(diagnosis_codes))
                    if row.nod and self.rng.random() < 0.18:
                        code = "E11"
                elif kind == EventKind.procedure.value:
                    code = str(self.rng.choice(procedure_codes))
                elif kind == EventKind.laboratory.value:
                    code = str(self.rng.choice(["glucose", "bilirubin", "alt", "ast", "ca199", "albumin"]))
                else:
                    code = str(self.rng.choice(medications))
                value = float(self.rng.normal(0.0, 1.0))
                if code == "glucose" and row.nod:
                    value += 1.5
                if code in {"R63.4", "bilirubin", "ca199"}:
                    value += float(self.rng.random() < 0.08) * 2.0
                rows.append({"patient_id": row.patient_id, "month": int(month), "kind": kind, "code": code, "value": value, "unit": "scaled"})
        return pd.DataFrame(rows)

    def outcomes(self, patients: pd.DataFrame) -> pd.DataFrame:
        age_risk = (patients["age"].to_numpy() - 40) / 55
        nod = patients["nod"].to_numpy()
        platform_bonus = patients["platform"].map({"Epic": 0.0, "Cerner": 0.05, "Legacy": 0.08}).to_numpy()
        logits = -4.7 + 1.1 * age_risk + 1.8 * nod + platform_bonus
        prob = 1.0 / (1.0 + np.exp(-logits))
        pdac = self.rng.binomial(1, prob)
        stage_probs = np.array([0.07, 0.10, 0.24, 0.54, 0.05])
        stages = np.where(pdac == 1, self.rng.choice([1, 2, 3, 4, 9], size=len(pdac), p=stage_probs), 0)
        diagnosis_month = self.rng.integers(0, 30, size=len(pdac))
        survival = np.where(stages <= 2, self.rng.gamma(3.0, 8.0, size=len(pdac)), self.rng.gamma(1.5, 5.0, size=len(pdac)))
        censored = self.rng.binomial(1, 0.2, size=len(pdac))
        return pd.DataFrame({"patient_id": patients["patient_id"], "pdac": pdac, "stage": stages, "diagnosis_month": diagnosis_month, "survival_months": survival, "censored": censored, "nod": patients["nod"]})

    def deployment_rows(self, patients: pd.DataFrame, outcomes: pd.DataFrame, sites: pd.DataFrame) -> pd.DataFrame:
        site_map = sites.set_index("site_id")
        merged = patients.merge(outcomes, on=["patient_id", "nod"])
        rows: list[dict[str, object]] = []
        for row in merged.itertuples(index=False):
            period = int(row.diagnosis_month // 5) + 1
            activation = int(site_map.loc[row.site_id, "activation_period"])
            intervention = int(period >= activation)
            early = int(row.stage in [1, 2])
            rows.append({"cluster": int(row.site_id), "period": period, "intervention": intervention, "early_stage": early, "pdac": int(row.pdac), "nod": int(row.nod), "age_group": age_group(int(row.age)), "sex": row.sex, "race_ethnicity": row.race_ethnicity, "platform": row.platform})
        return pd.DataFrame(rows)

    def bundle(self, n: int = 1200, max_events: int = 80) -> SyntheticBundle:
        sites = self.activation_table(self.site_table())
        patients = self.patients(n, sites)
        events = self.events_for_patients(patients, max_events=max_events)
        outcomes = self.outcomes(patients)
        deployment = self.deployment_rows(patients, outcomes, sites)
        return SyntheticBundle(events=events, outcomes=outcomes, deployment=deployment, sites=sites)

def compact_bundle(seed: int = 1729, n: int = 96, max_events: int = 24) -> SyntheticBundle:
    return EhrSimulator(seed).bundle(n=n, max_events=max_events)
