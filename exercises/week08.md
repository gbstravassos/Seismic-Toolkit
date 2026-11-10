# Week 08 exercise — Generate a reproducible run manifest

**Required function:** `build_run_manifest(seed, n_samples, scores)` in `src/seismic_toolkit/challenges.py`  
**Prerequisite notebook:** `notebooks/08_capstone_integration.ipynb`  
**Suggested time:** 90–150 minutes plus applied problem.

## Engineering request

A team wants a machine-readable summary for reproducing an experiment. Return a JSON-safe dictionary containing integer `seed`, integer `n_samples`, float `mean_accuracy` and float `std_accuracy` (population standard deviation) from a finite nonempty array of scores in `[0,1]`. Reject invalid input.

## Acceptance criteria

- Scores `[.7,.8,.9]` have mean `.8` and standard deviation `np.std([.7,.8,.9])`.
- `json.dumps(manifest)` succeeds without special encoders.
- `seed` and `n_samples` are integers; `n_samples` is positive.
- NaN, infinities, negative or >1 scores raise `ValueError`.
- A one-element score array is supported with standard deviation zero.

## Approach and hints

1. Treat this as a boundary between NumPy calculations and a report.
2. Validate inputs before computing any metrics.
3. Convert NumPy scalars to native Python floats/ints.
4. Verify round-trip with `json.loads(json.dumps(...))`.

## How to test

Implement **your own** tests first. Then execute:

```bash
python -m pytest -o addopts='' -m exercise -k week8 -q
python -m pytest -q
```

The first command is expected to fail before implementation. The second verifies that existing working functionality has not regressed. Consider a debugger when a test fails; avoid rewriting multiple modules at once.

## Applied problem and stretch challenge

**Applied problem — final handoff.** Integrate the synthetic signal demo, grouped ML evaluation and manifest into one concise report. Include a branch link or commit ID, test output, assumptions and limitations. Ask a colleague to run it from a clean environment using only README instructions.

**Stretch:** produce a reproducibility comparison tool that ignores timestamps but checks seeds, package versions, input definitions, validation policy and metric values.

## Submission checklist

- [ ] Contract explained in a docstring and clear function name.
- [ ] Normal numerical cases and invalid inputs covered by tests.
- [ ] Edge cases, unit conventions and limitations documented.
- [ ] No proprietary code/data, secret keys or unsafe generated code committed.
- [ ] Feature branch committed with an engineering summary.
- [ ] One insight or open question recorded for the next module.

**Scoring:** see `resources/assessment_rubric.md` (20 points per weekly exercise). Reference answers are in `solutions/reference_challenges.py` for use **after** your own attempt.
