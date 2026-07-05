from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Segment7Result:
    name: str
    value: float
    lower: float
    upper: float

def segment_7_0(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_0", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_0", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_1(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_1", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_1", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_2(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_2", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_2", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_3(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_3", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_3", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_4(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_4", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_4", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_5(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_5", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_5", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_6(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_6", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_6", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_7(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_7", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_7", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_8(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_8", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_8", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_9(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_9", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_9", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_10(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_10", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_10", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_11(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_11", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_11", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_12(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_12", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_12", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_13(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_13", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_13", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_14(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_14", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_14", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_15(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_15", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_15", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_16(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_16", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_16", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_17(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_17", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_17", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_18(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_18", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_18", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_19(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_19", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_19", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_20(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_20", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_20", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_21(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_21", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_21", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_22(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_22", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_22", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_23(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_23", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_23", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_24(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_24", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_24", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_25(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_25", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_25", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_26(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_26", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_26", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_7_27(values: np.ndarray, scale: float = 1.0) -> Segment7Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment7Result(name="segment_7_27", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment7Result(name="segment_7_27", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def collect_segment_7(values: np.ndarray) -> list[Segment7Result]:
    return [segment_7_27(values, scale=1.27) for j in range(28)]
