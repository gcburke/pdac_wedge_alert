from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Segment0Result:
    name: str
    value: float
    lower: float
    upper: float

def segment_0_0(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_0", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_0", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_1(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_1", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_1", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_2(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_2", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_2", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_3(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_3", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_3", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_4(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_4", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_4", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_5(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_5", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_5", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_6(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_6", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_6", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_7(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_7", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_7", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_8(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_8", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_8", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_9(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_9", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_9", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_10(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_10", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_10", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_11(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_11", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_11", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_12(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_12", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_12", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_13(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_13", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_13", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_14(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_14", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_14", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_15(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_15", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_15", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_16(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_16", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_16", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_17(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_17", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_17", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_18(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_18", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_18", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_19(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_19", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_19", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_20(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_20", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_20", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_21(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_21", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_21", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_22(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_22", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_22", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_23(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_23", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_23", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_24(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_24", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_24", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_25(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_25", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_25", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_26(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_26", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_26", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_0_27(values: np.ndarray, scale: float = 1.0) -> Segment0Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment0Result(name="segment_0_27", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment0Result(name="segment_0_27", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def collect_segment_0(values: np.ndarray) -> list[Segment0Result]:
    return [segment_0_27(values, scale=1.27) for j in range(28)]
