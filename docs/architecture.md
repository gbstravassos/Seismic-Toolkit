# Architecture and numerical contracts

## Dependency direction

```text
Notebooks ───────────┐
CLI ─────────────────┼──> seismic_toolkit.pipeline ──> synthetic / attributes
Streamlit application┘                                   │
                                                         └──> validation

ML notebooks ──> seismic_toolkit.ml ──> datasets + sklearn Pipeline
Tests ────────────────────────────────> public package functions
```

The math layer must **not** import Streamlit, notebook utilities or other presentation modules. The UI consumes the library. `challenges.py` holds isolated student assignments whose failure does not break the baseline library.

## Contracts and conventions

### Ricker wavelet

`ricker(frequency, dt, duration)` requires frequency in Hz, sample interval and window duration in seconds, and enforces a frequency below Nyquist. The returned array has an odd number of samples with its unit maximum at the central sample.

### Convolution

`synthetic_trace(reflectivity, wavelet)` returns the same number of samples as the reflectivity, centering an odd-length wavelet on each spike. Trace values must be finite 1D arrays.

### Signed time shift

`estimate_time_shift(baseline, monitor, dt, max_lag)` computes a global cross-correlation on aligned-length 1D traces and returns seconds; **positive = monitor later**. Resolution is one sample; fractional delays are not estimated. The method assumes adequate waveform similarity and should not be treated as a robust 4D time-strain estimator.

### Synthetic facies ML

`make_synthetic_facies_dataset(...)` constructs toy classes and four seismic-like features plus a grouping label. These arbitrary relationships demonstrate supervised ML workflow design, not quantitative subsurface characterization. `evaluate_group_holdout` and `grouped_cv_accuracy` isolate groups to reduce optimistic validation from correlated samples. Group definitions must match deployment for real experiments.

## Reliability boundaries

- Validate shape, range, units and finiteness.
- Keep random numbers seeded.
- Use `sklearn.pipeline.Pipeline` so transformations are refit inside CV folds.
- Keep UI input constraints and library-level input checks.
- Never assume an LLM-generated implementation is correct without independent tests.
- Only commit synthetic data or properly authorized resources.

## Why intentionally unfinished functions are included

The repo is both **working reference code** and a **student exercise environment**. The default test suite checks the working modules. The `exercise` marker gates challenge tests that are supposed to fail until a learner implements the assignment. Both behaviors are explicitly documented to avoid confusing a fresh user's first `pytest` run.
