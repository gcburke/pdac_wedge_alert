from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Panel12Result:
    key: str
    mean: float
    median: float
    lower: float
    upper: float

def panel_12_0(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_0", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_0", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_1(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_1", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_1", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_2(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_2", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_2", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_3(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_3", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_3", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_4(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_4", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_4", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_5(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_5", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_5", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_6(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_6", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_6", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_7(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_7", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_7", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_8(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_8", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_8", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_9(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_9", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_9", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_10(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_10", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_10", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_11(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_11", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_11", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_12(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_12", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_12", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_13(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_13", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_13", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_14(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_14", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_14", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_15(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_15", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_15", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_16(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_16", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_16", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_17(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_17", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_17", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_18(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_18", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_18", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_19(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_19", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_19", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_20(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_20", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_20", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_21(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_21", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_21", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_22(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_22", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_22", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_23(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_23", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_23", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_24(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_24", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_24", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_25(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_25", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_25", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_26(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_26", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_26", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_27(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_27", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_27", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_28(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_28", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_28", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_12_29(values: np.ndarray, offset: float = 0.0) -> Panel12Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel12Result(key="panel_12_29", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel12Result(key="panel_12_29", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def collect_panel_12(values: np.ndarray) -> list[Panel12Result]:
    output: list[Panel12Result] = []
    output.append(panel_12_0(values, offset=0.00))
    output.append(panel_12_1(values, offset=0.01))
    output.append(panel_12_2(values, offset=0.02))
    output.append(panel_12_3(values, offset=0.03))
    output.append(panel_12_4(values, offset=0.04))
    output.append(panel_12_5(values, offset=0.05))
    output.append(panel_12_6(values, offset=0.06))
    output.append(panel_12_7(values, offset=0.07))
    output.append(panel_12_8(values, offset=0.08))
    output.append(panel_12_9(values, offset=0.09))
    output.append(panel_12_10(values, offset=0.10))
    output.append(panel_12_11(values, offset=0.11))
    output.append(panel_12_12(values, offset=0.12))
    output.append(panel_12_13(values, offset=0.13))
    output.append(panel_12_14(values, offset=0.14))
    output.append(panel_12_15(values, offset=0.15))
    output.append(panel_12_16(values, offset=0.16))
    output.append(panel_12_17(values, offset=0.17))
    output.append(panel_12_18(values, offset=0.18))
    output.append(panel_12_19(values, offset=0.19))
    output.append(panel_12_20(values, offset=0.20))
    output.append(panel_12_21(values, offset=0.21))
    output.append(panel_12_22(values, offset=0.22))
    output.append(panel_12_23(values, offset=0.23))
    output.append(panel_12_24(values, offset=0.24))
    output.append(panel_12_25(values, offset=0.25))
    output.append(panel_12_26(values, offset=0.26))
    output.append(panel_12_27(values, offset=0.27))
    output.append(panel_12_28(values, offset=0.28))
    output.append(panel_12_29(values, offset=0.29))
    return output
