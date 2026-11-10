# Week 01 exercise — Normalize amplitudes safely

**Required function:** `normalize_trace(trace)` in `src/seismic_toolkit/challenges.py`  
**Prerequisite notebook:** `notebooks/01_python_project_architecture.ipynb`  
**Suggested time:** 90–150 minutes plus applied problem.

## Engineering request

A data-science colleague wants a normalized amplitude vector for comparison plots. Input is a finite, nonempty, 1D numeric vector. Compute the largest absolute amplitude, divide by it and return a fresh floating-point array. If every sample is zero, return an all-zero array. Do not modify caller-owned storage.

## Acceptance criteria

- `[-2, 0, 1]` becomes `[-1, 0, 0.5]`.
- `np.zeros(5)` remains zero and contains no NaNs.
- Raise `ValueError` for empty, 2D, object/non-numeric, NaN and infinite arrays.
- The input must remain unchanged even when writable.

## Approach and hints

1. Write tests for the three numerical cases before implementing code.
2. Reuse `require_trace` from `validation.py`.
3. Think about zero amplitude *before* dividing.
4. Run the targeted pytest test, then the baseline tests.

## How to test

Implement **your own** tests first. Then execute:

```bash
python -m pytest -o addopts='' -m exercise -k week1 -q
python -m pytest -q
```

The first command is expected to fail before implementation. The second verifies that existing working functionality has not regressed. Consider a debugger when a test fails; avoid rewriting multiple modules at once.

## Applied problem and stretch challenge

**Applied problem — 4D gain mismatch.** Simulate baseline and monitor traces where monitor = 2.5 × baseline. Compute RMS before and after normalization. Discuss when matching amplitudes suppresses acquisition artifacts and when it risks removing real time-lapse amplitude differences.

**Stretch:** add optional robust-percentile normalization (e.g. percentile of |amplitude|), with an explicit policy for a zero scale and tested percentile bounds.

## Submission checklist

- [ ] Contract explained in a docstring and clear function name.
- [ ] Normal numerical cases and invalid inputs covered by tests.
- [ ] Edge cases, unit conventions and limitations documented.
- [ ] No proprietary code/data, secret keys or unsafe generated code committed.
- [ ] Feature branch committed with an engineering summary.
- [ ] One insight or open question recorded for the next module.

**Scoring:** see `resources/assessment_rubric.md` (20 points per weekly exercise). Reference answers are in `solutions/reference_challenges.py` for use **after** your own attempt.
