"""Small reproducible end-to-end synthetic signal demonstration."""

from __future__ import annotations

import numpy as np

from .attributes import estimate_time_shift, trace_rms
from .synthetic import ricker, spike_reflectivity, synthetic_trace


def run_synthetic_demo(dt: float = 0.001, delay_samples: int = 4) -> dict[str, object]:
    """Return arrays and measurements for a deterministic baseline/monitor pair."""
    if not isinstance(delay_samples, int) or not 0 <= delay_samples <= 20:
        raise ValueError("delay_samples must be an integer in [0, 20]")
    w = ricker(30.0, dt, 0.128)
    r = spike_reflectivity(512, [120, 230, 350], [1.0, -0.6, 0.9])
    baseline = synthetic_trace(r, w)
    delayed = np.pad(baseline, (delay_samples, 0))[: baseline.size]
    measured = estimate_time_shift(baseline, delayed, dt, 0.020)
    return {
        "baseline": baseline,
        "monitor": delayed,
        "dt": dt,
        "true_delay_s": delay_samples * dt,
        "estimated_delay_s": measured,
        "baseline_rms": trace_rms(baseline),
    }
