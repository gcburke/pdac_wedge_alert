from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Panel13Result:
    key: str
    mean: float
    median: float
    lower: float
    upper: float

def panel_13_0(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_0", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_0", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_1(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_1", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_1", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_2(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_2", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_2", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_3(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_3", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_3", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_4(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_4", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_4", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_5(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_5", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_5", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_6(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_6", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_6", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_7(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_7", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_7", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_8(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_8", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_8", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_9(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_9", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_9", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_10(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_10", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_10", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_11(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_11", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_11", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_12(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_12", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_12", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_13(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_13", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_13", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_14(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_14", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_14", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_15(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_15", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_15", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_16(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_16", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_16", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_17(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_17", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_17", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_18(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_18", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_18", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_19(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_19", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_19", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_20(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_20", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_20", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_21(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_21", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_21", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_22(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_22", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_22", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_23(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_23", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_23", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_24(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_24", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_24", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_25(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_25", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_25", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_26(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_26", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_26", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_27(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_27", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_27", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_28(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_28", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_28", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def panel_13_29(values: np.ndarray, offset: float = 0.0) -> Panel13Result:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        return Panel13Result(key="panel_13_29", mean=0.0, median=0.0, lower=0.0, upper=0.0)
    shifted = arr + offset
    mean = float(np.nanmean(shifted))
    median = float(np.nanmedian(shifted))
    spread = float(np.nanstd(shifted) / math.sqrt(max(shifted.size, 1)))
    return Panel13Result(key="panel_13_29", mean=mean, median=median, lower=mean - 1.96 * spread, upper=mean + 1.96 * spread)

def collect_panel_13(values: np.ndarray) -> list[Panel13Result]:
    output: list[Panel13Result] = []
    output.append(panel_13_0(values, offset=0.00))
    output.append(panel_13_1(values, offset=0.01))
    output.append(panel_13_2(values, offset=0.02))
    output.append(panel_13_3(values, offset=0.03))
    output.append(panel_13_4(values, offset=0.04))
    output.append(panel_13_5(values, offset=0.05))
    output.append(panel_13_6(values, offset=0.06))
    output.append(panel_13_7(values, offset=0.07))
    output.append(panel_13_8(values, offset=0.08))
    output.append(panel_13_9(values, offset=0.09))
    output.append(panel_13_10(values, offset=0.10))
    output.append(panel_13_11(values, offset=0.11))
    output.append(panel_13_12(values, offset=0.12))
    output.append(panel_13_13(values, offset=0.13))
    output.append(panel_13_14(values, offset=0.14))
    output.append(panel_13_15(values, offset=0.15))
    output.append(panel_13_16(values, offset=0.16))
    output.append(panel_13_17(values, offset=0.17))
    output.append(panel_13_18(values, offset=0.18))
    output.append(panel_13_19(values, offset=0.19))
    output.append(panel_13_20(values, offset=0.20))
    output.append(panel_13_21(values, offset=0.21))
    output.append(panel_13_22(values, offset=0.22))
    output.append(panel_13_23(values, offset=0.23))
    output.append(panel_13_24(values, offset=0.24))
    output.append(panel_13_25(values, offset=0.25))
    output.append(panel_13_26(values, offset=0.26))
    output.append(panel_13_27(values, offset=0.27))
    output.append(panel_13_28(values, offset=0.28))
    output.append(panel_13_29(values, offset=0.29))
    return output
