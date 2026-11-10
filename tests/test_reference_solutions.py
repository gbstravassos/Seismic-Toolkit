"""Ensure the optional reference solutions work."""

import json

import numpy as np

from seismic_toolkit.datasets import FEATURE_COLUMNS, make_synthetic_facies_dataset
from solutions import reference_challenges as answers


def test_all_reference_answers():
    np.testing.assert_allclose(answers.normalize_trace(np.array([-2.0, 0, 1])), [-1, 0, 0.5])
    b, m = np.zeros(100), np.zeros(100)
    b[40], m[44] = 1, 1
    assert answers.estimate_shift_samples(b, m, 8) == 4
    assert answers.moving_rms(np.array([1., 2., 3.]), 3).shape == (3,)
    np.testing.assert_equal(answers.qc_generated_predictions([0, 1], 2, 3), [0, 1])
    df = make_synthetic_facies_dataset(8, 20)
    model = answers.fit_baseline_classifier(df)
    assert model.predict(df[list(FEATURE_COLUMNS)].head()).size == 5
    assert answers.evaluate_by_group(df, 4).size == 4
    json.dumps(answers.prepare_plot_payload(np.array([0.0, 1.0]), .001))
    manifest = answers.build_run_manifest(2, 100, np.array([.6, .8]))
    assert manifest["mean_accuracy"] == 0.7 or np.isclose(manifest["mean_accuracy"], 0.7)
    json.dumps(manifest)
