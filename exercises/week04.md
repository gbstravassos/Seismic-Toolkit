# Week 04 exercise — Defend the boundary of an AI-generated classifier

**Required function:** `qc_generated_predictions(predictions, n_samples, n_classes)` in `src/seismic_toolkit/challenges.py`  
**Prerequisite notebook:** `notebooks/04_ai_assisted_development.ipynb`  
**Suggested time:** 90–150 minutes plus applied problem.

## Engineering request

A model-assisted interpretation feature returns class IDs as text-decoded numeric values. Validate this untrusted data before it touches downstream plots or reports. Accept only a 1D sequence of finite whole-number labels, exactly `n_samples` long, with classes in the half-open range `[0,n_classes)`. Return an integer NumPy array.

## Acceptance criteria

- `[0,1,2]`, 3 samples and 3 classes is accepted.
- Reject class 3 when `n_classes=3`, values `1.5`, NaN and nested list shapes.
- Reject wrong sample count, zero samples or fewer than two classes.
- Returned dtype is integer, and error messages identify the violated contract.

## Approach and hints

1. Write validation tests from the spec before showing your implementation to an AI model.
2. Compare `np.asarray(values, dtype=float)` to strict length and range tests.
3. Ensure whole-number checking happens before converting floats to integer.
4. Ask a model to review your implementation; test every accepted suggestion independently.

## How to test

Implement **your own** tests first. Then execute:

```bash
python -m pytest -o addopts='' -m exercise -k week4 -q
python -m pytest -q
```

The first command is expected to fail before implementation. The second verifies that existing working functionality has not regressed. Consider a debugger when a test fails; avoid rewriting multiple modules at once.

## Applied problem and stretch challenge

**Applied problem — prompt and patch audit.** Write a 150-word request for an LLM to propose this function. Save a review note with assumptions, potential errors and accepted/rejected changes. Do not paste proprietary laboratory data or code.

**Stretch:** produce an audit record that identifies which test detected an intentionally introduced bad class label.

## Submission checklist

- [ ] Contract explained in a docstring and clear function name.
- [ ] Normal numerical cases and invalid inputs covered by tests.
- [ ] Edge cases, unit conventions and limitations documented.
- [ ] No proprietary code/data, secret keys or unsafe generated code committed.
- [ ] Feature branch committed with an engineering summary.
- [ ] One insight or open question recorded for the next module.

**Scoring:** see `resources/assessment_rubric.md` (20 points per weekly exercise). Reference answers are in `solutions/reference_challenges.py` for use **after** your own attempt.
