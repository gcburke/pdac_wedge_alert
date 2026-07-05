from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Segment8Result:
    name: str
    value: float
    lower: float
    upper: float

def segment_8_0(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_0", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_0", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_1(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_1", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_1", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_2(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_2", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_2", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_3(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_3", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_3", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_4(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_4", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_4", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_5(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_5", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_5", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_6(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_6", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_6", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_7(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_7", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_7", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_8(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_8", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_8", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_9(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_9", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_9", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_10(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_10", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_10", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_11(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_11", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_11", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_12(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_12", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_12", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_13(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_13", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_13", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_14(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_14", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_14", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_15(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_15", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_15", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_16(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_16", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_16", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_17(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_17", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_17", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_18(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_18", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_18", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_19(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_19", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_19", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_20(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_20", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_20", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_21(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_21", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_21", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_22(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_22", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_22", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_23(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_23", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_23", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_24(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_24", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_24", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_25(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_25", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_25", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_26(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_26", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_26", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_8_27(values: np.ndarray, scale: float = 1.0) -> Segment8Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment8Result(name="segment_8_27", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment8Result(name="segment_8_27", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def collect_segment_8(values: np.ndarray) -> list[Segment8Result]:
    return [segment_8_27(values, scale=1.27) for j in range(28)]
