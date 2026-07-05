from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Segment10Result:
    name: str
    value: float
    lower: float
    upper: float

def segment_10_0(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_0", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_0", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_1(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_1", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_1", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_2(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_2", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_2", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_3(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_3", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_3", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_4(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_4", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_4", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_5(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_5", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_5", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_6(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_6", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_6", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_7(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_7", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_7", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_8(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_8", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_8", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_9(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_9", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_9", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_10(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_10", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_10", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_11(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_11", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_11", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_12(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_12", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_12", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_13(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_13", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_13", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_14(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_14", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_14", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_15(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_15", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_15", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_16(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_16", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_16", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_17(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_17", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_17", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_18(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_18", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_18", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_19(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_19", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_19", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_20(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_20", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_20", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_21(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_21", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_21", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_22(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_22", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_22", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_23(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_23", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_23", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_24(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_24", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_24", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_25(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_25", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_25", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_26(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_26", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_26", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def segment_10_27(values: np.ndarray, scale: float = 1.0) -> Segment10Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Segment10Result(name="segment_10_27", value=0.0, lower=0.0, upper=0.0)
    center = float(np.nanmean(arr) * scale)
    spread = float(np.nanstd(arr) / math.sqrt(max(arr.size, 1)))
    return Segment10Result(name="segment_10_27", value=center, lower=center - 1.96 * spread, upper=center + 1.96 * spread)

def collect_segment_10(values: np.ndarray) -> list[Segment10Result]:
    return [segment_10_27(values, scale=1.27) for j in range(28)]
