# Week 06 exercise — Evaluate correlated samples by group

**Required function:** `evaluate_by_group(frame, n_splits=4)` in `src/seismic_toolkit/challenges.py`  
**Prerequisite notebook:** `notebooks/06_ml_validation.ipynb`  
**Suggested time:** 90–150 minutes plus applied problem.

## Engineering request

An ML team claims 95% validation accuracy on seismic-like records. They randomly mixed nearby traces into training and test sets. Implement group-separated cross-validation as a fairer assessment for new areas: return one float accuracy score per fold using `GroupKFold`. Fit all preprocessing **inside** each fold.

## Acceptance criteria

- For 8 groups and 4 folds, return `np.ndarray` with shape `(4,)`.
- Every score lies in `[0,1]`.
- Groups are not shared between train and validation in a fold.
- Reject too many folds or fewer than two folds.
- No scaling/imputation of the full dataset prior to the fold split.

## Approach and hints

1. Inspect the `grouped_cv_accuracy` reference in `ml.py`.
2. Test group disjointness for every fold.
3. Wrap the imputer, scaler and classifier in an sklearn Pipeline.
4. Compare row-level StratifiedKFold to GroupKFold and explain both estimands.

## How to test

Implement **your own** tests first. Then execute:

```bash
python -m pytest -o addopts='' -m exercise -k week6 -q
python -m pytest -q
```

The first command is expected to fail before implementation. The second verifies that existing working functionality has not regressed. Consider a debugger when a test fails; avoid rewriting multiple modules at once.

## Applied problem and stretch challenge

**Applied problem — 4D leakage audit.** Describe a split where baseline/monitor at the same location stay together. Explain whether this split measures performance on unseen locations or merely a new acquisition vintage.

**Stretch:** repeat group-aware evaluation at multiple random seeds with GroupShuffleSplit and report empirical distribution, not a guaranteed confidence bound.

## Submission checklist

- [ ] Contract explained in a docstring and clear function name.
- [ ] Normal numerical cases and invalid inputs covered by tests.
- [ ] Edge cases, unit conventions and limitations documented.
- [ ] No proprietary code/data, secret keys or unsafe generated code committed.
- [ ] Feature branch committed with an engineering summary.
- [ ] One insight or open question recorded for the next module.

**Scoring:** see `resources/assessment_rubric.md` (20 points per weekly exercise). Reference answers are in `solutions/reference_challenges.py` for use **after** your own attempt.
