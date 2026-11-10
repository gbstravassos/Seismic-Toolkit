# Week 02 exercise — Cross-correlation with a documented sign convention

**Required function:** `estimate_shift_samples(baseline, monitor, max_lag_samples)` in `src/seismic_toolkit/challenges.py`  
**Prerequisite notebook:** `notebooks/02_testing_git_debugging.ipynb`  
**Suggested time:** 90–150 minutes plus applied problem.

## Engineering request

A signal-processing team needs an integer lag estimator. A positive answer must indicate the monitor arrives later than the baseline. Restrict eligible lags to ±`max_lag_samples`; enforce equal 1D lengths, nonzero energy and non-negative integer lag limit.

## Acceptance criteria

- A unit spike at sample 30 for baseline and 34 for monitor yields `+4`.
- Reversing the traces yields `-4`.
- Identical spikes yield zero.
- Invalid shape, zero energy and negative lag limits fail clearly.
- Do not accidentally return a lag outside the search window.

## Approach and hints

1. Inspect the arguments of `scipy.signal.correlate` and `correlation_lags`.
2. Create a +4 and a −4 synthetic unit-spike test.
3. Ensure the returned value is an integer **number of samples**, not seconds.
4. Reproduce one wrong-sign implementation and show a regression test catching it.

## How to test

Implement **your own** tests first. Then execute:

```bash
python -m pytest -o addopts='' -m exercise -k week2 -q
python -m pytest -q
```

The first command is expected to fail before implementation. The second verifies that existing working functionality has not regressed. Consider a debugger when a test fails; avoid rewriting multiple modules at once.

## Applied problem and stretch challenge

**Applied problem — noise sensitivity.** With a fixed seed, add white Gaussian noise at several strengths and measure the fraction of correct lag estimates over 100 realizations. Make a plot of empirical success rate against noise scale, but do not present it as a universal field-data performance curve.

**Stretch:** add an optional parabolic sub-sample interpolation, creating a *separate* function with a floating-point return and explicit limitations.

## Submission checklist

- [ ] Contract explained in a docstring and clear function name.
- [ ] Normal numerical cases and invalid inputs covered by tests.
- [ ] Edge cases, unit conventions and limitations documented.
- [ ] No proprietary code/data, secret keys or unsafe generated code committed.
- [ ] Feature branch committed with an engineering summary.
- [ ] One insight or open question recorded for the next module.

**Scoring:** see `resources/assessment_rubric.md` (20 points per weekly exercise). Reference answers are in `solutions/reference_challenges.py` for use **after** your own attempt.
