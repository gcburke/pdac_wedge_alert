from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Segment1Result:
    name: str
    value: float
    lower: float
    upper: float

def segment_1_0(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_0", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_0", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_1(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_1", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_1", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_2(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_2", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_2", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_3(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_3", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_3", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_4(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_4", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_4", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_5(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_5", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_5", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_6(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_6", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_6", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_7(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_7", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_7", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_8(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_8", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_8", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_9(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_9", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_9", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_10(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_10", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_10", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_11(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_11", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_11", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_12(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_12", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_12", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_13(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_13", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_13", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_14(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_14", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_14", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_15(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_15", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_15", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_16(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_16", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_16", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_17(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_17", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_17", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_18(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_18", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_18", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_19(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_19", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_19", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_20(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_20", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_20", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_21(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_21", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_21", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_22(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_22", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_22", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_23(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_23", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_23", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_24(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_24", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_24", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_25(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_25", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_25", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_26(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_26", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_26", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_1_27(values: np.ndarray, scale: float = 1.0) -> Segment1Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment1Result(name="segment_1_27", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment1Result(name="segment_1_27", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def collect_segment_1(values: np.ndarray) -> list[Segment1Result]:
    return [segment_1_27(values, scale=1.27) for j in range(28)]
