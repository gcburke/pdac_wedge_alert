from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Segment2Result:
    name: str
    value: float
    lower: float
    upper: float

def segment_2_0(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_0", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_0", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_1(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_1", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_1", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_2(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_2", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_2", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_3(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_3", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_3", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_4(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_4", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_4", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_5(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_5", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_5", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_6(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_6", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_6", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_7(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_7", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_7", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_8(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_8", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_8", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_9(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_9", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_9", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_10(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_10", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_10", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_11(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_11", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_11", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_12(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_12", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_12", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_13(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_13", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_13", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_14(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_14", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_14", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_15(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_15", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_15", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_16(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_16", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_16", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_17(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_17", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_17", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_18(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_18", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_18", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_19(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_19", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_19", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_20(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_20", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_20", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_21(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_21", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_21", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_22(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_22", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_22", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_23(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_23", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_23", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_24(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_24", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_24", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_25(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_25", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_25", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_26(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_26", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_26", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_2_27(values: np.ndarray, scale: float = 1.0) -> Segment2Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment2Result(name="segment_2_27", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment2Result(name="segment_2_27", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def collect_segment_2(values: np.ndarray) -> list[Segment2Result]:
    return [segment_2_27(values, scale=1.27) for j in range(28)]
