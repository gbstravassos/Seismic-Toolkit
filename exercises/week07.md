# Week 07 exercise — Prepare a clean API payload for plotting

**Required function:** `prepare_plot_payload(trace, dt)` in `src/seismic_toolkit/challenges.py`  
**Prerequisite notebook:** `notebooks/07_streamlit_app.ipynb`  
**Suggested time:** 90–150 minutes plus applied problem.

## Engineering request

A web interface needs a serialization-safe trace with a matching time axis. Return exactly `{'time_s': [...], 'amplitude': [...]}` where both fields are ordinary Python lists. Time begins at zero and increases by `dt` seconds. Reject invalid sample intervals and malformed traces.

## Acceptance criteria

- `[0,1,0.5]` at `dt=0.002` yields times `[0,0.002,0.004]`.
- `json.dumps(payload)` succeeds without a custom encoder.
- Each list has the same number of entries as the trace.
- Reject empty traces, NaN and nonpositive `dt`.
- Do not import Streamlit inside the numerical function.

## Approach and hints

1. Reuse validation helpers.
2. Create a NumPy time axis using `np.arange`.
3. Convert arrays to lists only at the interface boundary.
4. Verify JSON encoding and exact expected tiny values in a test.

## How to test

Implement **your own** tests first. Then execute:

```bash
python -m pytest -o addopts='' -m exercise -k week7 -q
python -m pytest -q
```

The first command is expected to fail before implementation. The second verifies that existing working functionality has not regressed. Consider a debugger when a test fails; avoid rewriting multiple modules at once.

## Applied problem and stretch challenge

**Applied problem — UI enhancement.** Modify `apps/streamlit_app.py` to show an optional RMS amplitude for baseline and monitor; keep numeric computations in the library. Document a manual test of slider behavior and units.

**Stretch:** add a safe synthetic CSV export button, ensuring that it never reads untrusted file paths or real field data.

## Submission checklist

- [ ] Contract explained in a docstring and clear function name.
- [ ] Normal numerical cases and invalid inputs covered by tests.
- [ ] Edge cases, unit conventions and limitations documented.
- [ ] No proprietary code/data, secret keys or unsafe generated code committed.
- [ ] Feature branch committed with an engineering summary.
- [ ] One insight or open question recorded for the next module.

**Scoring:** see `resources/assessment_rubric.md` (20 points per weekly exercise). Reference answers are in `solutions/reference_challenges.py` for use **after** your own attempt.
