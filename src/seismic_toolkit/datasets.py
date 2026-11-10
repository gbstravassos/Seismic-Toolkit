"""Synthetic facies attributes for methodological ML exercises only."""

from __future__ import annotations

import numpy as np
import pandas as pd

FEATURE_COLUMNS = ("impedance", "amplitude", "frequency", "coherence")


def make_synthetic_facies_dataset(
    n_groups: int = 12, samples_per_group: int = 50, seed: int = 42
) -> pd.DataFrame:
    """Generate toy attribute/facies samples with survey-group correlations.

    'group' stands in for a spatial/acquisition grouping. Features and labels
    are synthetic and do not represent validated reservoir physics.
    """
    if n_groups < 4 or samples_per_group < 6:
        raise ValueError("Use at least 4 groups and 6 samples per group")
    rng = np.random.default_rng(seed)
    frames: list[pd.DataFrame] = []
    for group_id in range(n_groups):
        facies = rng.choice(3, size=samples_per_group, p=[0.40, 0.35, 0.25])
        group_effect = rng.normal(0, 0.25)
        frame = pd.DataFrame(
            {
                "impedance": 4.0 + 0.8 * facies + group_effect + rng.normal(0, 0.45, samples_per_group),
                "amplitude": -0.3 + 0.55 * facies + 0.25 * group_effect + rng.normal(0, 0.4, samples_per_group),
                "frequency": 44.0 - 5.0 * facies + 2.0 * group_effect + rng.normal(0, 3.0, samples_per_group),
                "coherence": 0.8 - 0.17 * facies + rng.normal(0, 0.08, samples_per_group),
                "facies": facies.astype(int),
                "group": np.repeat(group_id, samples_per_group),
            }
        )
        frames.append(frame)
    return pd.concat(frames, ignore_index=True)
