from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Segment6Result:
    name: str
    value: float
    lower: float
    upper: float

def segment_6_0(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_0", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_0", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_1(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_1", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_1", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_2(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_2", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_2", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_3(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_3", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_3", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_4(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_4", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_4", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_5(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_5", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_5", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_6(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_6", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_6", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_7(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_7", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_7", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_8(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_8", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_8", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_9(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_9", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_9", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_10(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_10", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_10", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_11(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_11", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_11", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_12(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_12", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_12", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_13(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_13", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_13", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_14(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_14", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_14", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_15(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_15", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_15", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_16(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_16", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_16", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_17(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_17", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_17", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_18(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_18", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_18", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_19(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_19", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_19", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_20(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_20", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_20", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_21(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_21", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_21", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_22(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_22", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_22", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_23(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_23", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_23", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_24(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_24", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_24", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_25(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_25", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_25", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_26(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_26", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_26", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_6_27(values: np.ndarray, scale: float = 1.0) -> Segment6Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment6Result(name="segment_6_27", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment6Result(name="segment_6_27", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def collect_segment_6(values: np.ndarray) -> list[Segment6Result]:
    return [segment_6_27(values, scale=1.27) for j in range(28)]
