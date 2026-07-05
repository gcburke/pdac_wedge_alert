from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
from enum import StrEnum

import numpy as np
import pandas as pd
from numpy.typing import NDArray


class EventKind(StrEnum):
    diagnosis = "diagnosis"
    procedure = "procedure"
    laboratory = "laboratory"
    medication = "medication"
    demographic = "demographic"

class EhrPlatform(StrEnum):
    epic = "Epic"
    cerner = "Cerner"
    legacy = "Legacy"

class AlertTier(StrEnum):
    none = "none"
    enhanced = "enhanced_monitoring"
    urgent = "urgent_evaluation"

@dataclass(frozen=True)
class PatientEvent:
    patient_id: str
    month: int
    kind: EventKind
    code: str
    value: float
    unit: str

@dataclass(frozen=True)
class PatientRecord:
    patient_id: str
    age: int
    sex: str
    race_ethnicity: str
    platform: EhrPlatform
    region: str
    site_id: int
    events: tuple[PatientEvent, ...]

@dataclass(frozen=True)
class OutcomeRecord:
    patient_id: str
    pdac: int
    stage: int
    diagnosis_month: int
    survival_months: float
    censored: int
    nod: int

@dataclass(frozen=True)
class AlertRecord:
    patient_id: str
    site_id: int
    period: int
    risk: float
    percentile: float
    tier: AlertTier
    acted: int
    completed: int
    pdac: int

@dataclass(frozen=True)
class DeploymentRow:
    cluster: int
    period: int
    intervention: int
    early_stage: int
    pdac: int
    nod: int
    age_group: str
    sex: str
    race_ethnicity: str
    platform: str

@dataclass(frozen=True)
class ModelConfig:
    vocabulary_size: int
    feature_size: int
    model_dim: int
    heads: int
    layers: int
    feedforward: int
    dropout: float
    max_events: int

@dataclass(frozen=True)
class TrainConfig:
    seed: int
    batch_size: int
    grad_accum: int
    epochs: int
    learning_rate: float
    weight_decay: float
    warmup_steps: int
    scheduler: str
    precision: str
    world_size: int
    checkpoint_dir: str

@dataclass(frozen=True)
class ThresholdConfig:
    alert_percentile: float
    urgent_percentile: float
    target_alerts_min: float
    target_alerts_max: float

@dataclass(frozen=True)
class WedgeDesign:
    clusters: int
    periods: int
    months_per_period: int
    sequence_sizes: tuple[int, ...]

@dataclass(frozen=True)
class EffectEstimate:
    estimate: float
    lower: float
    upper: float
    p_value: float
    label: str

@dataclass(frozen=True)
class CostParameters:
    ai_infrastructure: float
    ct_cost: float
    eus_cost: float
    biopsy_cost: float
    treatment_stage_i_ii: float
    treatment_stage_iii_iv: float
    qaly_stage_i_ii: float
    qaly_stage_iii_iv: float
    discount: float

@dataclass(frozen=True)
class CostResult:
    population: str
    icer: float
    nns: float
    qalys_per_1000: float
    cost_per_case: float
    probability_cost_effective: float

class SchemaError(ValueError):
    pass

def require_columns(frame: pd.DataFrame, columns: Sequence[str]) -> None:
    missing = [column for column in columns if column not in frame.columns]
    if missing:
        raise SchemaError(", ".join(missing))

def as_event_frame(events: Iterable[PatientEvent]) -> pd.DataFrame:
    rows = [event.__dict__ | {"kind": event.kind.value} for event in events]
    return pd.DataFrame(rows, columns=["patient_id", "month", "kind", "code", "value", "unit"])

def as_alert_frame(alerts: Iterable[AlertRecord]) -> pd.DataFrame:
    rows = [alert.__dict__ | {"tier": alert.tier.value} for alert in alerts]
    return pd.DataFrame(rows)

def as_deployment_frame(rows: Iterable[DeploymentRow]) -> pd.DataFrame:
    return pd.DataFrame([row.__dict__ for row in rows])

def validate_event_frame(frame: pd.DataFrame) -> pd.DataFrame:
    require_columns(frame, ["patient_id", "month", "kind", "code", "value"])
    out = frame.copy()
    out["patient_id"] = out["patient_id"].astype(str)
    out["month"] = out["month"].astype(int)
    out["kind"] = out["kind"].astype(str)
    out["code"] = out["code"].astype(str)
    out["value"] = out["value"].astype(float)
    if (out["month"] < 0).any():
        raise SchemaError("month")
    return out

def validate_outcome_frame(frame: pd.DataFrame) -> pd.DataFrame:
    require_columns(frame, ["patient_id", "pdac", "stage", "diagnosis_month", "survival_months", "censored", "nod"])
    out = frame.copy()
    for column in ["pdac", "stage", "diagnosis_month", "censored", "nod"]:
        out[column] = out[column].astype(int)
    out["survival_months"] = out["survival_months"].astype(float)
    return out

def split_by_patient(frame: pd.DataFrame) -> dict[str, pd.DataFrame]:
    validate_event_frame(frame)
    return {str(pid): part.sort_values("month").reset_index(drop=True) for pid, part in frame.groupby("patient_id")}

def encode_categories(values: Sequence[str]) -> dict[str, int]:
    unique = sorted(set(values))
    return {value: index + 1 for index, value in enumerate(unique)}

def stable_code_index(code: str, vocabulary_size: int) -> int:
    acc = 2166136261
    for byte in code.encode("utf-8"):
        acc ^= byte
        acc = (acc * 16777619) % (2**32)
    return int(acc % max(vocabulary_size - 1, 1)) + 1

def month_age_weights(months: np.ndarray, lookback: int) -> NDArray[np.float64]:
    recency = np.clip(lookback - months, 0, lookback)
    return np.asarray(np.exp(-recency / max(lookback / 3.0, 1.0)), dtype=np.float64)

def early_stage_indicator(stage: pd.Series) -> pd.Series:
    return stage.isin([1, 2]).astype(int)

def period_from_month(month: int, months_per_period: int) -> int:
    return int(month // months_per_period) + 1

def age_group(age: int) -> str:
    if age < 55:
        return "40-54"
    if age < 65:
        return "55-64"
    return "65+"

def mapping_frame(mapping: Mapping[str, int]) -> pd.DataFrame:
    return pd.DataFrame({"key": list(mapping.keys()), "value": list(mapping.values())})
