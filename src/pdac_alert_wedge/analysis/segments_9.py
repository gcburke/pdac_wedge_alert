from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Segment9Result:
    name: str
    value: float
    lower: float
    upper: float

def segment_9_0(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_0", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_0", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_1(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_1", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_1", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_2(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_2", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_2", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_3(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_3", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_3", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_4(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_4", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_4", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_5(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_5", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_5", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_6(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_6", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_6", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_7(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_7", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_7", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_8(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_8", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_8", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_9(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_9", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_9", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_10(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_10", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_10", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_11(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_11", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_11", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_12(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_12", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_12", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_13(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_13", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_13", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_14(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_14", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_14", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_15(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_15", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_15", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_16(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_16", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_16", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_17(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_17", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_17", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_18(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_18", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_18", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_19(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_19", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_19", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_20(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_20", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_20", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_21(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_21", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_21", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_22(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_22", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_22", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_23(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_23", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_23", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_24(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_24", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_24", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_25(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_25", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_25", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_26(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_26", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_26", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_9_27(values: np.ndarray, scale: float = 1.0) -> Segment9Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment9Result(name="segment_9_27", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment9Result(name="segment_9_27", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def collect_segment_9(values: np.ndarray) -> list[Segment9Result]:
    return [segment_9_27(values, scale=1.27) for j in range(28)]
