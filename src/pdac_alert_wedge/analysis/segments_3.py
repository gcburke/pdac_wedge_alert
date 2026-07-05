from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Segment3Result:
    name: str
    value: float
    lower: float
    upper: float

def segment_3_0(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_0", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_0", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_1(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_1", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_1", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_2(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_2", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_2", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_3(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_3", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_3", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_4(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_4", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_4", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_5(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_5", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_5", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_6(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_6", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_6", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_7(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_7", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_7", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_8(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_8", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_8", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_9(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_9", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_9", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_10(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_10", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_10", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_11(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_11", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_11", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_12(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_12", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_12", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_13(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_13", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_13", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_14(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_14", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_14", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_15(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_15", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_15", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_16(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_16", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_16", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_17(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_17", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_17", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_18(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_18", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_18", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_19(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_19", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_19", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_20(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_20", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_20", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_21(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_21", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_21", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_22(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_22", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_22", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_23(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_23", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_23", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_24(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_24", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_24", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_25(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_25", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_25", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_26(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_26", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_26", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_3_27(values: np.ndarray, scale: float = 1.0) -> Segment3Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment3Result(name="segment_3_27", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment3Result(name="segment_3_27", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def collect_segment_3(values: np.ndarray) -> list[Segment3Result]:
    return [segment_3_27(values, scale=1.27) for j in range(28)]
