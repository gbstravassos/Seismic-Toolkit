"""Input validation shared across seismic signal routines."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray


def require_trace(values: object, name: str = "trace") -> NDArray[np.float64]:
    """Return a finite, non-empty 1D float trace or raise ValueError."""
    try:
        a = np.asarray(values, dtype=np.float64)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must contain numeric values") from exc
    if a.ndim != 1 or a.size == 0:
        raise ValueError(f"{name} must be a non-empty, one-dimensional array")
    if not np.all(np.isfinite(a)):
        raise ValueError(f"{name} must contain only finite values")
    return a


def require_positive(value: float, name: str) -> float:
    """Require a finite, strictly positive scalar."""
    try:
        x = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be a positive finite number") from exc
    if not np.isfinite(x) or x <= 0:
        raise ValueError(f"{name} must be a positive finite number")
    return x
