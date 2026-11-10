"""Production baseline tests. Expected to pass before student work begins."""

import numpy as np
import pytest

from seismic_toolkit.attributes import estimate_time_shift, trace_rms
from seismic_toolkit.pipeline import run_synthetic_demo
from seismic_toolkit.synthetic import ricker, spike_reflectivity, synthetic_trace
from seismic_toolkit.validation import require_trace


def test_ricker_is_symmetric_and_unit_peak():
    w = ricker(30, 0.001, 0.128)
    assert len(w) % 2 == 1
    np.testing.assert_allclose(w, w[::-1], atol=1e-12)
    assert w[len(w) // 2] == pytest.approx(1.0)


@pytest.mark.parametrize("frequency,dt,duration", [(0, 0.001, 0.1), (30, 0, 0.1), (600, 0.001, 0.1), (30, 0.001, 0)])
def test_invalid_ricker_inputs_raise(frequency, dt, duration):
    with pytest.raises(ValueError):
        ricker(frequency, dt, duration)


def test_trace_preserves_length_even_for_long_wavelet():
    w = ricker(30, 0.001, 0.128)
    r = np.zeros(21)
    r[10] = 1
    assert synthetic_trace(r, w).shape == r.shape


def test_reflectivity_spikes_and_input_validation():
    r = spike_reflectivity(100, [40, 40, 60], [1.0, -0.25, 0.5])
    assert r[40] == pytest.approx(0.75)
    with pytest.raises(ValueError):
        require_trace([1.0, np.nan])
    with pytest.raises(ValueError):
        synthetic_trace(np.ones(10), np.ones(4))


@pytest.mark.parametrize("delay", [-7, -3, 0, 2, 5])
def test_signed_shift(delay):
    base = np.zeros(100)
    base[35] = 1
    mon = np.zeros(100)
    mon[35 + delay] = 1
    assert estimate_time_shift(base, mon, dt=0.002, max_lag=0.02) == pytest.approx(delay * 0.002)


def test_shift_rejects_bad_input():
    with pytest.raises(ValueError):
        estimate_time_shift(np.zeros(50), np.zeros(50), 0.001, 0.02)
    with pytest.raises(ValueError):
        estimate_time_shift(np.ones(50), np.ones(40), 0.001, 0.02)
    with pytest.raises(ValueError):
        estimate_time_shift(np.ones(50), np.ones(50), 0.001, -1)


def test_pipeline_is_reproducible_and_correct():
    a = run_synthetic_demo()
    b = run_synthetic_demo()
    np.testing.assert_array_equal(a["baseline"], b["baseline"])
    assert a["estimated_delay_s"] == pytest.approx(a["true_delay_s"])
    assert a["baseline_rms"] == pytest.approx(trace_rms(a["baseline"]))
