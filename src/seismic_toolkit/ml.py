"""Machine learning baseline and leakage-aware group evaluation."""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, balanced_accuracy_score, f1_score
from sklearn.model_selection import GroupKFold, GroupShuffleSplit, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from .datasets import FEATURE_COLUMNS


def make_baseline_model() -> Pipeline:
    """Return an sklearn Pipeline; preprocessing is fit on training folds only."""
    return Pipeline(
        [
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            ("model", LogisticRegression(max_iter=2000, random_state=7)),
        ]
    )


def evaluate_group_holdout(frame: pd.DataFrame, seed: int = 42) -> dict[str, object]:
    """Fit on some groups, assess on entirely unseen groups."""
    required = set(FEATURE_COLUMNS) | {"facies", "group"}
    if not required.issubset(frame.columns):
        raise ValueError(f"dataset must contain columns: {sorted(required)}")
    if frame["group"].nunique() < 4:
        raise ValueError("at least four groups are required")
    X = frame[list(FEATURE_COLUMNS)]
    y = frame["facies"]
    groups = frame["group"]
    splitter = GroupShuffleSplit(n_splits=1, test_size=0.25, random_state=seed)
    train_idx, test_idx = next(splitter.split(X, y, groups))
    model = make_baseline_model()
    model.fit(X.iloc[train_idx], y.iloc[train_idx])
    predicted = model.predict(X.iloc[test_idx])
    return {
        "model": model,
        "accuracy": float(accuracy_score(y.iloc[test_idx], predicted)),
        "balanced_accuracy": float(balanced_accuracy_score(y.iloc[test_idx], predicted)),
        "macro_f1": float(f1_score(y.iloc[test_idx], predicted, average="macro", zero_division=0)),
        "train_groups": sorted(set(groups.iloc[train_idx].tolist())),
        "test_groups": sorted(set(groups.iloc[test_idx].tolist())),
        "y_true": np.asarray(y.iloc[test_idx]),
        "y_pred": np.asarray(predicted),
    }


def grouped_cv_accuracy(frame: pd.DataFrame, n_splits: int = 4) -> np.ndarray:
    """Compute group-separated CV accuracy; no fit/preprocess leakage."""
    if n_splits < 2 or n_splits > frame["group"].nunique():
        raise ValueError("n_splits must be between 2 and the number of groups")
    return cross_val_score(
        make_baseline_model(),
        frame[list(FEATURE_COLUMNS)],
        frame["facies"],
        groups=frame["group"],
        cv=GroupKFold(n_splits=n_splits),
        scoring="accuracy",
    )
