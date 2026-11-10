# Week 03 exercise — Centered moving RMS with incomplete edge windows

**Required function:** `moving_rms(trace, window)` in `src/seismic_toolkit/challenges.py`  
**Prerequisite notebook:** `notebooks/03_robust_python.ipynb`  
**Suggested time:** 90–150 minutes plus applied problem.

## Engineering request

A QC report needs local signal energy. For an odd positive window, compute RMS in a centered neighborhood around every trace sample. Where the window reaches beyond the trace, use only available points; do not pad zero values. Preserve trace length and reject invalid input or even/zero windows.

## Acceptance criteria

- For `[1, 2, 3, 4, 5]` and window `3`, the center equals `sqrt(29/3)`.
- For the same input, the first sample equals `sqrt((1+4)/2)`.
- Window `1` returns absolute sample amplitudes.
- All outputs are finite; output length matches input length.
- Reject even, zero or negative window sizes and invalid traces.

## Approach and hints

1. Start with a five-element example and a plain loop.
2. Explicitly compute `left=max(0,i-radius)` and `right=min(n,i+radius+1)`.
3. Compare with hand calculations.
4. Only then consider convolution or vectorization; benchmark both variants if optimizing.

## How to test

Implement **your own** tests first. Then execute:

```bash
python -m pytest -o addopts='' -m exercise -k week3 -q
python -m pytest -q
```

The first command is expected to fail before implementation. The second verifies that existing working functionality has not regressed. Consider a debugger when a test fails; avoid rewriting multiple modules at once.

## Applied problem and stretch challenge

**Applied problem — signal-energy QC.** Calculate local RMS of a synthetic baseline and monitor with one interval of artificially increased noise. Detect the abnormal region and discuss sensitivity to window size.

**Stretch:** offer an optional time-based window in milliseconds converted to an odd number of samples, with tested rounding rules.

## Submission checklist

- [ ] Contract explained in a docstring and clear function name.
- [ ] Normal numerical cases and invalid inputs covered by tests.
- [ ] Edge cases, unit conventions and limitations documented.
- [ ] No proprietary code/data, secret keys or unsafe generated code committed.
- [ ] Feature branch committed with an engineering summary.
- [ ] One insight or open question recorded for the next module.

**Scoring:** see `resources/assessment_rubric.md` (20 points per weekly exercise). Reference answers are in `solutions/reference_challenges.py` for use **after** your own attempt.
