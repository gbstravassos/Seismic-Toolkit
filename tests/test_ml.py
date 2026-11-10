"""ML checks use synthetic datasets and group-separated splits."""

import numpy as np
import pytest

from seismic_toolkit.datasets import FEATURE_COLUMNS, make_synthetic_facies_dataset
from seismic_toolkit.ml import evaluate_group_holdout, grouped_cv_accuracy


def test_dataset_is_deterministic_and_has_expected_shape():
    one = make_synthetic_facies_dataset(12, 30, seed=3)
    two = make_synthetic_facies_dataset(12, 30, seed=3)
    assert one.equals(two)
    assert len(one) == 360
    assert set(FEATURE_COLUMNS).issubset(one.columns)
    assert one["facies"].nunique() == 3


def test_group_holdout_never_reuses_groups():
    frame = make_synthetic_facies_dataset()
    result = evaluate_group_holdout(frame)
    assert set(result["train_groups"]).isdisjoint(result["test_groups"])
    assert 0 <= result["accuracy"] <= 1
    assert 0 <= result["macro_f1"] <= 1
    assert len(result["y_pred"]) == len(result["y_true"])


def test_group_cv_score_shape():
    frame = make_synthetic_facies_dataset(8, 30, seed=11)
    scores = grouped_cv_accuracy(frame, n_splits=4)
    assert scores.shape == (4,)
    assert np.all((scores >= 0) & (scores <= 1))


def test_group_cv_fails_for_too_few_groups():
    with pytest.raises(ValueError):
        grouped_cv_accuracy(make_synthetic_facies_dataset(4), n_splits=5)
