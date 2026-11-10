"""Intentionally failing until the corresponding student challenge is solved.

Run only week N: pytest -o addopts='' -m exercise -k weekN -q
Run all challenge tests: pytest -o addopts='' -m exercise -q
The default `pytest` excludes these exercises.
"""

import json

import numpy as np
import pytest
from sklearn.pipeline import Pipeline

from seismic_toolkit import challenges
from seismic_toolkit.datasets import FEATURE_COLUMNS, make_synthetic_facies_dataset


@pytest.mark.exercise
def test_week1_normalize_trace():
    result = challenges.normalize_trace(np.array([-2.0, 0.0, 1.0]))
    np.testing.assert_allclose(result, [-1, 0, 0.5])
    np.testing.assert_allclose(challenges.normalize_trace(np.zeros(5)), np.zeros(5))


@pytest.mark.exercise
def test_week2_estimate_shift_samples():
    b = np.zeros(80)
    m = np.zeros(80)
    b[30] = 1
    m[34] = 1
    assert challenges.estimate_shift_samples(b, m, 8) == 4
    assert challenges.estimate_shift_samples(m, b, 8) == -4


@pytest.mark.exercise
def test_week3_moving_rms():
    x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    out = challenges.moving_rms(x, 3)
    expected = [np.sqrt((1 + 4) / 2), np.sqrt(14 / 3), np.sqrt(29 / 3), np.sqrt(50 / 3), np.sqrt((16 + 25) / 2)]
    np.testing.assert_allclose(out, expected)
    with pytest.raises(ValueError):
        challenges.moving_rms(x, 0)


@pytest.mark.exercise
def test_week4_generated_prediction_qc():
    np.testing.assert_array_equal(challenges.qc_generated_predictions([0, 1, 2], 3, 3), [0, 1, 2])
    for values in ([0, 3], [0, 0.5], [0, np.nan], [[0], [1]]):
        with pytest.raises(ValueError):
            challenges.qc_generated_predictions(values, 2, 3)


@pytest.mark.exercise
def test_week5_fit_baseline_classifier():
    frame = make_synthetic_facies_dataset(8, 20)
    model = challenges.fit_baseline_classifier(frame)
    assert isinstance(model, Pipeline)
    assert len(model.predict(frame[list(FEATURE_COLUMNS)].head(5))) == 5


@pytest.mark.exercise
def test_week6_evaluate_by_group():
    frame = make_synthetic_facies_dataset(8, 30)
    scores = challenges.evaluate_by_group(frame, 4)
    assert scores.shape == (4,)
    assert np.all((scores >= 0) & (scores <= 1))


@pytest.mark.exercise
def test_week7_plot_payload_is_json_safe():
    data = challenges.prepare_plot_payload(np.array([0.0, 1.0, 0.5]), 0.002)
    assert data == {"time_s": [0.0, 0.002, 0.004], "amplitude": [0.0, 1.0, 0.5]}
    json.dumps(data)


@pytest.mark.exercise
def test_week8_manifest_is_json_safe():
    record = challenges.build_run_manifest(42, 600, np.array([0.7, 0.8, 0.9]))
    assert record["seed"] == 42
    assert record["n_samples"] == 600
    assert record["mean_accuracy"] == pytest.approx(0.8)
    assert record["std_accuracy"] == pytest.approx(float(np.std([0.7, 0.8, 0.9])))
    json.dumps(record)
