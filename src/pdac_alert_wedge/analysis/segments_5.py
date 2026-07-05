from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Segment5Result:
    name: str
    value: float
    lower: float
    upper: float

def segment_5_0(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_0", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_0", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_1(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_1", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_1", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_2(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_2", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_2", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_3(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_3", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_3", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_4(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_4", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_4", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_5(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_5", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_5", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_6(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_6", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_6", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_7(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_7", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_7", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_8(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_8", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_8", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_9(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_9", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_9", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_10(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_10", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_10", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_11(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_11", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_11", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_12(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_12", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_12", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_13(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_13", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_13", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_14(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_14", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_14", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_15(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_15", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_15", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_16(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_16", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_16", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_17(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_17", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_17", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_18(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_18", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_18", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_19(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_19", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_19", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_20(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_20", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_20", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_21(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_21", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_21", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_22(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_22", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_22", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_23(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_23", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_23", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_24(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_24", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_24", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_25(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_25", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_25", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_26(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_26", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_26", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_5_27(values: np.ndarray, scale: float = 1.0) -> Segment5Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment5Result(name="segment_5_27", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment5Result(name="segment_5_27", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def collect_segment_5(values: np.ndarray) -> list[Segment5Result]:
    return [segment_5_27(values, scale=1.27) for j in range(28)]
