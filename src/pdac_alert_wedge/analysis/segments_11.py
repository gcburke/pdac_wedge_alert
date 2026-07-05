from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Segment11Result:
    name: str
    value: float
    lower: float
    upper: float

def segment_11_0(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_0", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_0", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_1(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_1", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_1", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_2(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_2", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_2", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_3(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_3", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_3", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_4(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_4", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_4", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_5(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_5", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_5", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_6(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_6", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_6", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_7(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_7", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_7", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_8(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_8", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_8", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_9(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_9", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_9", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_10(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_10", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_10", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_11(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_11", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_11", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_12(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_12", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_12", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_13(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_13", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_13", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_14(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_14", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_14", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_15(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_15", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_15", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_16(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_16", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_16", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_17(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_17", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_17", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_18(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_18", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_18", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_19(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_19", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_19", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_20(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_20", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_20", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_21(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_21", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_21", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_22(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_22", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_22", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_23(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_23", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_23", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_24(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_24", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_24", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_25(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_25", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_25", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_26(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_26", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_26", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_11_27(values: np.ndarray, scale: float = 1.0) -> Segment11Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment11Result(name="segment_11_27", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment11Result(name="segment_11_27", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def collect_segment_11(values: np.ndarray) -> list[Segment11Result]:
    return [segment_11_27(values, scale=1.27) for j in range(28)]
