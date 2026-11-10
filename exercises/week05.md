# Week 05 exercise — Fit a leakage-resistant baseline classifier

**Required function:** `fit_baseline_classifier(frame)` in `src/seismic_toolkit/challenges.py`  
**Prerequisite notebook:** `notebooks/05_ml_fundamentals.ipynb`  
**Suggested time:** 90–150 minutes plus applied problem.

## Engineering request

You are given a synthetic facies DataFrame containing impedance, amplitude, frequency, coherence, facies and group columns. Return a **fitted scikit-learn Pipeline** with preprocessing (including missing-value handling), scaling and a baseline classifier. Fit using only the four `FEATURE_COLUMNS`; never treat group IDs as physical predictors.

## Acceptance criteria

- Returned object is an sklearn `Pipeline`.
- Predicting on a five-row `FEATURE_COLUMNS` DataFrame returns five class labels.
- Missing required columns trigger a `ValueError`.
- The model handles isolated missing feature values via an imputer.
- You can justify each preprocessing step and explain when it is fitted.

## Approach and hints

1. Start with `make_baseline_model()` in `ml.py` and inspect its steps.
2. Select the named feature columns; do not accidentally include labels or groups.
3. Fit a pipeline on a training subset; compare predictions on held-out groups.
4. Explain why any scaler fitted on the entire dataset before splitting is leakage.

## How to test

Implement **your own** tests first. Then execute:

```bash
python -m pytest -o addopts='' -m exercise -k week5 -q
python -m pytest -q
```

The first command is expected to fail before implementation. The second verifies that existing working functionality has not regressed. Consider a debugger when a test fails; avoid rewriting multiple modules at once.

## Applied problem and stretch challenge

**Applied problem — compare models.** Using the same grouped holdout, compare logistic regression with a random forest. Report accuracy, balanced accuracy, macro F1 and a confusion matrix. Note at least three limitations of the synthetic task.

**Stretch:** inject some missing values into training rows using a fixed seed; demonstrate that missing-value handling is inside the pipeline rather than precomputed globally.

## Submission checklist

- [ ] Contract explained in a docstring and clear function name.
- [ ] Normal numerical cases and invalid inputs covered by tests.
- [ ] Edge cases, unit conventions and limitations documented.
- [ ] No proprietary code/data, secret keys or unsafe generated code committed.
- [ ] Feature branch committed with an engineering summary.
- [ ] One insight or open question recorded for the next module.

**Scoring:** see `resources/assessment_rubric.md` (20 points per weekly exercise). Reference answers are in `solutions/reference_challenges.py` for use **after** your own attempt.
