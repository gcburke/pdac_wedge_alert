from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
import torch
from torch.utils.data import Dataset

from pdac_alert_wedge.records import stable_code_index, validate_event_frame, validate_outcome_frame


@dataclass(frozen=True)
class TensorBatch:
    codes: torch.Tensor
    values: torch.Tensor
    months: torch.Tensor
    mask: torch.Tensor
    targets: torch.Tensor

class EhrSequenceDataset(Dataset[tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]]):
    def __init__(self, events: pd.DataFrame, outcomes: pd.DataFrame, vocabulary_size: int, max_events: int) -> None:
        self.events = validate_event_frame(events)
        self.outcomes = validate_outcome_frame(outcomes).set_index("patient_id")
        self.vocabulary_size = vocabulary_size
        self.max_events = max_events
        self.patient_ids = sorted(set(self.events["patient_id"]).intersection(set(self.outcomes.index)))

    def __len__(self) -> int:
        return len(self.patient_ids)

    def __getitem__(self, index: int) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
        patient_id = self.patient_ids[index]
        part = self.events[self.events["patient_id"] == patient_id].sort_values("month").tail(self.max_events)
        codes = np.zeros(self.max_events, dtype=np.int64)
        values = np.zeros(self.max_events, dtype=np.float32)
        months = np.zeros(self.max_events, dtype=np.float32)
        mask = np.zeros(self.max_events, dtype=np.float32)
        offset = self.max_events - len(part)
        for i, row in enumerate(part.itertuples(index=False), start=offset):
            codes[i] = stable_code_index(f"{row.kind}:{row.code}", self.vocabulary_size)
            values[i] = float(row.value)
            months[i] = float(row.month)
            mask[i] = 1.0
        target = np.array([float(self.outcomes.loc[patient_id, "pdac"])], dtype=np.float32)
        return torch.tensor(codes), torch.tensor(values), torch.tensor(months), torch.tensor(mask), torch.tensor(target)

def collate_sequences(items: list[tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]]) -> TensorBatch:
    codes = torch.stack([item[0] for item in items], dim=0)
    values = torch.stack([item[1] for item in items], dim=0)
    months = torch.stack([item[2] for item in items], dim=0)
    mask = torch.stack([item[3] for item in items], dim=0)
    targets = torch.stack([item[4] for item in items], dim=0)
    return TensorBatch(codes=codes, values=values, months=months, mask=mask, targets=targets)

def event_counts(events: pd.DataFrame) -> pd.DataFrame:
    frame = validate_event_frame(events)
    return frame.groupby(["patient_id", "kind"]).size().unstack(fill_value=0).reset_index()

def laboratory_slopes(events: pd.DataFrame) -> pd.DataFrame:
    frame = validate_event_frame(events)
    labs = frame[frame["kind"] == "laboratory"]
    rows: list[dict[str, object]] = []
    for (patient, code), part in labs.groupby(["patient_id", "code"]):
        if len(part) < 2:
            slope = 0.0
        else:
            x = part["month"].to_numpy(dtype=float)
            y = part["value"].to_numpy(dtype=float)
            slope = float(np.polyfit(x, y, deg=1)[0])
        rows.append({"patient_id": patient, "code": code, "slope": slope})
    if not rows:
        return pd.DataFrame(columns=["patient_id"])
    return pd.DataFrame(rows).pivot(index="patient_id", columns="code", values="slope").fillna(0.0).reset_index()

def patient_feature_matrix(events: pd.DataFrame, outcomes: pd.DataFrame) -> tuple[np.ndarray, np.ndarray, list[str]]:
    counts = event_counts(events)
    slopes = laboratory_slopes(events)
    features = counts.merge(slopes, on="patient_id", how="left").fillna(0.0)
    yframe = validate_outcome_frame(outcomes)[["patient_id", "pdac"]]
    merged = features.merge(yframe, on="patient_id", how="inner")
    names = [column for column in merged.columns if column not in {"patient_id", "pdac"}]
    return merged[names].to_numpy(dtype=np.float32), merged["pdac"].to_numpy(dtype=np.float32), names
