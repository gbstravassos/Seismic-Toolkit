"""Signal-level attributes and time-shift estimation."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray
from scipy.signal import correlate, correlation_lags

from .validation import require_positive, require_trace


def trace_rms(trace: NDArray[np.float64]) -> float:
    """Return RMS amplitude; a zero trace has RMS zero."""
    x = require_trace(trace)
    return float(np.sqrt(np.mean(x**2)))


def estimate_time_shift(
    baseline: NDArray[np.float64],
    monitor: NDArray[np.float64],
    dt: float,
    max_lag: float,
) -> float:
    """Estimate integer-sample delay of monitor relative to baseline, in seconds.

    Sign convention: positive means monitor arrives later. Both traces must have
    equal lengths and non-zero energy. A lag is limited to +/- max_lag seconds.
    Correlation is globally normalized; the waveforms are not mean-subtracted.
    """
    b = require_trace(baseline, "baseline")
    m = require_trace(monitor, "monitor")
    sample_interval = require_positive(dt, "dt")
    if b.size != m.size:
        raise ValueError("baseline and monitor must have the same length")
    if b.size < 2:
        raise ValueError("traces must have at least two samples")
    if not np.isfinite(max_lag) or max_lag < 0:
        raise ValueError("max_lag must be a finite, non-negative value")
    energy = np.linalg.norm(b) * np.linalg.norm(m)
    if energy == 0.0:
        raise ValueError("time-shift estimation needs non-zero-energy traces")
    lag_samples = min(int(np.floor(max_lag / sample_interval + 1e-12)), b.size - 1)
    lags = correlation_lags(m.size, b.size, mode="full")
    coefficients = correlate(m, b, mode="full", method="auto") / energy
    allowed = np.abs(lags) <= lag_samples
    best_lag = int(lags[allowed][np.argmax(coefficients[allowed])])
    return float(best_lag * sample_interval)
