"""Ricker wavelets and 1D synthetic seismic traces."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

from .validation import require_positive, require_trace


def ricker(frequency: float, dt: float, duration: float) -> NDArray[np.float64]:
    """Build a zero-phase Ricker wavelet with an odd number of samples.

    Parameters
    ----------
    frequency : float
        Peak frequency in Hz. Must be below the Nyquist frequency.
    dt : float
        Sample interval in seconds.
    duration : float
        Approximate full wavelet duration in seconds (rounded to an odd grid).

    Returns
    -------
    ndarray
        Symmetric wavelet with its unit-amplitude peak at the center sample.
    """
    f = require_positive(frequency, "frequency")
    sample_interval = require_positive(dt, "dt")
    window = require_positive(duration, "duration")
    if f >= 0.5 / sample_interval:
        raise ValueError("frequency must be below the Nyquist frequency")
    n_half = int(round(window / (2.0 * sample_interval)))
    if n_half < 1:
        raise ValueError("duration must span at least two sample intervals")
    t = np.arange(-n_half, n_half + 1, dtype=np.float64) * sample_interval
    a = (np.pi * f * t) ** 2
    return (1.0 - 2.0 * a) * np.exp(-a)


def synthetic_trace(
    reflectivity: NDArray[np.float64], wavelet: NDArray[np.float64]
) -> NDArray[np.float64]:
    """Convolve reflectivity and an odd-length wavelet, preserving trace size.

    The center sample of the wavelet corresponds to zero time.
    """
    r = require_trace(reflectivity, "reflectivity")
    w = require_trace(wavelet, "wavelet")
    if w.size % 2 == 0:
        raise ValueError("wavelet must have an odd number of samples")
    full = np.convolve(r, w, mode="full")
    start = (w.size - 1) // 2
    return full[start : start + r.size]


def spike_reflectivity(n_samples: int, positions: list[int], amplitudes: list[float]) -> NDArray[np.float64]:
    """Create a reflectivity series with specified spikes (duplicate positions sum)."""
    if isinstance(n_samples, bool) or not isinstance(n_samples, int) or n_samples < 1:
        raise ValueError("n_samples must be a positive integer")
    if len(positions) != len(amplitudes):
        raise ValueError("positions and amplitudes must have equal length")
    series = np.zeros(n_samples, dtype=np.float64)
    for position, amplitude in zip(positions, amplitudes):
        if not isinstance(position, (int, np.integer)) or not 0 <= position < n_samples:
            raise ValueError("each position must be an in-range integer index")
        a = float(amplitude)
        if not np.isfinite(a):
            raise ValueError("amplitudes must be finite")
        series[position] += a
    return series
