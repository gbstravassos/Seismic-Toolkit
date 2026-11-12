"""Eight intentionally unfinished student exercises.

The base application works without these functions. Run `pytest -m exercise`
after implementing them. Reference implementations are in solutions/.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from numpy.typing import NDArray


def normalize_trace(trace: np.ndarray) -> np.ndarray:
    """
    Normalize a seismic trace by its maximum absolute amplitude.

    Parameters
    ----------
    trace : np.ndarray
        Nonempty, finite, one-dimensional numeric array.

    Returns
    -------
    np.ndarray
        New array with normalized amplitudes.
        A zero-amplitude trace returns an array of zeros.

    Raises
    ------
    ValueError
        If the input is empty, nonnumeric, nonfinite,
        or not one-dimensional.
    """
    try:
        a = np.asarray(trace, dtype=np.float64)
    except (TypeError, ValueError) as exc:
        raise ValueError("Trace must contain numeric values") from exc

    if a.ndim != 1 or a.size == 0:
        raise ValueError("Trace must be a nonempty, one-dimensional array")

    if not np.all(np.isfinite(a)):
        raise ValueError("Trace must contain only finite values")

    max_amplitude = np.max(np.abs(a))

    if max_amplitude == 0:
        return np.zeros_like(a)

    return a / max_amplitude


def estimate_shift_samples(baseline: np.ndarray, monitor: np.ndarray, max_lag_samples: int) -> int:
    """W2: return signed integer delay; positive = monitor later."""
    raise NotImplementedError("Week 2: implement estimate_shift_samples")


def moving_rms(trace: np.ndarray, window: int) -> np.ndarray:
    """W3: centered moving RMS with edge windows clipped to available samples."""
    raise NotImplementedError("Week 3: implement moving_rms")


def qc_generated_predictions(predictions: object, n_samples: int, n_classes: int) -> np.ndarray:
    """W4: validate 1D integer class predictions in [0, n_classes)."""
    raise NotImplementedError("Week 4: implement qc_generated_predictions")


def fit_baseline_classifier(frame: pd.DataFrame):
    """W5: fit and return an sklearn Pipeline on FEATURE_COLUMNS and facies."""
    raise NotImplementedError("Week 5: implement fit_baseline_classifier")


def evaluate_by_group(frame: pd.DataFrame, n_splits: int = 4) -> np.ndarray:
    """W6: return group-separated CV accuracy scores, shape (n_splits,)."""
    raise NotImplementedError("Week 6: implement evaluate_by_group")


def prepare_plot_payload(trace: np.ndarray, dt: float) -> dict[str, list[float]]:
    """W7: JSON-safe dict with 'time_s' and 'amplitude' lists."""
    raise NotImplementedError("Week 7: implement prepare_plot_payload")


def build_run_manifest(seed: int, n_samples: int, scores: np.ndarray) -> dict[str, object]:
    """W8: JSON-safe dict with seed, n_samples, mean_accuracy, std_accuracy."""
    raise NotImplementedError("Week 8: implement build_run_manifest")
