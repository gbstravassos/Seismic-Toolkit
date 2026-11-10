# Syllabus — Seismic Python & AI Engineering

**Level:** intermediate Python; experience with scientific arrays recommended.  
**Duration:** 8 modules × approximately 6–8 hours.  
**Format:** eight executable Jupyter notebooks, test-driven implementation challenges, applied problems, code review and a capstone.  
**Hardware:** ordinary laptop; GPU not required.  
**Environment:** Python >=3.10; local dependencies; offline examples.

## Outcomes by module

| Module | Concepts | Evidence of completion |
|---|---|---|
| 1 | Packaging, module boundaries, NumPy contracts, editable installs | Tested `normalize_trace`, clearly documented API |
| 2 | pytest, fixtures/parametrization, Git, debugging | Correct +/− lag in `estimate_shift_samples`; test report |
| 3 | Typed interfaces, validation, exceptions, dataclasses, logging, CLI | Robust `moving_rms` with edge-window behavior |
| 4 | Prompt contracts, generated code review, security/privacy | Validated `qc_generated_predictions` and review log |
| 5 | Feature/label separation, sklearn Pipeline, metrics | `fit_baseline_classifier` and a comparison of models |
| 6 | GroupKFold, group leakage, performance uncertainty | `evaluate_by_group` and validation memo |
| 7 | Streamlit architecture, serialization, UI testing | `prepare_plot_payload` and running optional UI |
| 8 | Integration, reproducibility, manifest, PR documentation | `build_run_manifest`, complete capstone evidence |

## Required artifacts for assessment

1. Source file(s) with implemented, documented challenge functions.
2. Relevant test results and new edge-case tests for every challenge.
3. Eight notebook study records (answers in markdown or a separate study journal).
4. At least one structured AI code-review example with accepted/rejected suggestions.
5. A final JSON report using synthetic inputs, with seeds and validation policy documented.
6. Final pull request with a concise explanation of architecture and limitations.

## Expected competency at completion

A learner should be able to read and modify an unfamiliar medium-sized Python package, write meaningful tests for scientific routines, review model-generated Python patches, build a basic tabular ML evaluation without obvious preprocessing leakage, and separate a user-facing application from the numerical core.

This course does **not** claim that completing it makes someone a reservoir engineer, senior software engineer or ML research scientist. Those roles require additional domain-specific experience and operational validation.

## Recommended sequence and flexibility

Weeks 1–4 form the Python engineering foundation. Weeks 5–6 address ML and experimental design. Weeks 7–8 connect components into a deliverable. If a real workplace task is more urgent, re-order the relevant notebook while revisiting prerequisites. The 8-week schedule is a learning scaffold rather than a certification standard.
