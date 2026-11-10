# Seismic Python & AI Engineering — 8-Week Hands-on Course

[![Python CI](https://img.shields.io/badge/CI-GitHub%20Actions-blue)](.github/workflows/python-ci.yml) [![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](pyproject.toml) [![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

**Learn to turn scientific Python scripts into maintainable applications, use generative AI responsibly for coding, and evaluate machine-learning models on synthetic seismic-like data.**

This repository is a complete, self-paced English-language course for **intermediate Python users** who already know functions, classes, NumPy and scientific computing, but want stronger software-engineering practice. It is tailored to a multidisciplinary geoscience environment where colleagues build Python products with generative AI and apply machine learning to reservoir interpretation.

> **Important scope:** all examples use **synthetic educational data**. The toy facies generator does not represent geologically validated reservoir behavior. No proprietary software, seismic data, external API keys, GPU, or account access is needed. This code is **not approved for operational reservoir decisions**.

## What you will learn

- **Professional Python:** project layout, packaging, type hints, validation, exceptions, logging, testing, debugging and Git collaboration.
- **AI-assisted development:** specification-driven prompting, reviewing generated changes, red-team testing, confidentiality and human sign-off.
- **ML foundations:** pandas, scikit-learn pipelines, classification metrics, grouped cross-validation, leakage prevention and careful interpretation.
- **Application engineering:** command-line interfaces, reusable algorithms, Streamlit, JSON-safe reporting, documentation and reproducible deliverables.

### Course map

| Week | Jupyter notebook | Major topic | Required programming challenge |
|---|---|---|---|
| 1 | [`01_python_project_architecture.ipynb`](notebooks/01_python_project_architecture.ipynb) | Project architecture and scientific functions | `normalize_trace` |
| 2 | [`02_testing_git_debugging.ipynb`](notebooks/02_testing_git_debugging.ipynb) | Unit tests, debugging and Git | `estimate_shift_samples` |
| 3 | [`03_robust_python.ipynb`](notebooks/03_robust_python.ipynb) | Types, validation, logs, pipelines | `moving_rms` |
| 4 | [`04_ai_assisted_development.ipynb`](notebooks/04_ai_assisted_development.ipynb) | Test-driven generative AI workflows | `qc_generated_predictions` |
| 5 | [`05_ml_fundamentals.ipynb`](notebooks/05_ml_fundamentals.ipynb) | Tabular ML, preprocessing, metrics | `fit_baseline_classifier` |
| 6 | [`06_ml_validation.ipynb`](notebooks/06_ml_validation.ipynb) | Group-based CV, model interpretation | `evaluate_by_group` |
| 7 | [`07_streamlit_app.ipynb`](notebooks/07_streamlit_app.ipynb) | Python-backed interactive application | `prepare_plot_payload` |
| 8 | [`08_capstone_integration.ipynb`](notebooks/08_capstone_integration.ipynb) | Reproducible capstone and report | `build_run_manifest` |

Each week includes a runnable notebook, an independent implementation exercise, passing baseline tests, **deliberately failing optional exercise tests** (until solved), an applied problem and a stretch problem. See [`SYLLABUS.md`](SYLLABUS.md), [`COURSE_GUIDE.md`](COURSE_GUIDE.md) and [`exercises/`](exercises/).

## Quick start

**Prerequisites:** Python 3.10 or later, Git and a terminal. VS Code with Python/Jupyter extensions is recommended. On Windows, use PowerShell; on Linux/macOS use a shell.

1. Download and extract the ZIP or clone your GitHub repository.
2. Enter the root folder containing `pyproject.toml`.
3. Create and activate a virtual environment:

**Windows PowerShell:**

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[course,dev]"
```

**Linux or macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[course,dev]'
```

4. Start JupyterLab **from the repository root**:

```bash
python -m jupyterlab
```

5. Open [`notebooks/01_python_project_architecture.ipynb`](notebooks/01_python_project_architecture.ipynb) and select the `.venv` Python kernel if prompted.

6. Run baseline tests:

```bash
python -m pytest -q
```

These tests pass before exercises are completed. They validate the supplied working reference library.

### How exercises are graded

Student functions are **intentionally unimplemented** in [`src/seismic_toolkit/challenges.py`](src/seismic_toolkit/challenges.py). Their tests are marked `exercise` and excluded from ordinary `pytest` runs. This means a clean initial installation is green while independent exercises remain unsolved.

To run **one week's challenge** (replace `week1` with `week2`, etc.):

```bash
python -m pytest -o addopts='' -m exercise -k week1 -q
```

To check **all eight challenges** after implementing them:

```bash
python -m pytest -o addopts='' -m exercise -q
```

A failing challenge test is expected **until you implement that function**. Optional reference solutions are in [`solutions/reference_challenges.py`](solutions/reference_challenges.py); avoid looking at them before attempting your own code. The course is designed for learning, not copy-and-paste answers.

## Working example: seismic time shifts

```python
from seismic_toolkit.pipeline import run_synthetic_demo

result = run_synthetic_demo(dt=0.001, delay_samples=4)
print(result["true_delay_s"])       # 0.004 s
print(result["estimated_delay_s"])  # 0.004 s
```

Sign convention: **positive time shift means that the monitor arrives later than the baseline**. Sample interval and lag limits are specified in **seconds**. The example uses synthetic 1D traces and integer-sample lag resolution.

CLI alternative (works after installation):

```bash
python -m seismic_toolkit.cli --dt 0.001 --delay-samples 4
# or: seismic-demo --dt 0.001 --delay-samples 4
```

## Optional interactive app

```bash
python -m pip install -e '.[app]'
streamlit run apps/streamlit_app.py
```

The Streamlit app presents baseline/monitor traces and time-shift estimates. It does not require any deployed service and performs calculations locally.

## Repository layout

```text
seismic-python-ai-course/
├── README.md                     # Start here
├── COURSE_GUIDE.md               # Study routine and setup troubleshooting
├── SYLLABUS.md                   # Learning outcomes and weekly deliverables
├── pyproject.toml                # Dependencies, scripts, pytest settings
├── .github/workflows/python-ci.yml
├── notebooks/                    # Eight executable English lessons (.ipynb)
├── exercises/                    # Eight detailed problem sets (.md)
├── src/seismic_toolkit/
│   ├── synthetic.py              # Ricker, reflectivity, convolution
│   ├── attributes.py             # RMS, signed cross-correlation time shift
│   ├── validation.py             # Input contracts
│   ├── datasets.py               # Synthetic facies-like data
│   ├── ml.py                     # Pipeline and leakage-aware evaluation
│   ├── pipeline.py               # End-to-end signal demonstration
│   ├── cli.py                    # Command-line example
│   └── challenges.py             # Eight TODO assignments
├── tests/                        # Baseline, reference and optional exercise tests
├── apps/streamlit_app.py         # Optional interactive UI
├── solutions/                    # Optional reference answers
├── resources/                    # AI prompts, glossary, rubric, checklists
├── docs/                         # Design and testing architecture
├── data/                         # Data-use guidance (no proprietary inputs)
└── outputs/                      # Generated reports; ignored by Git
```

## Weekly workflow (6–8 hours)

1. **Read** (45–60 min): review the concepts and existing source code.
2. **Experiment** (90 min): execute the notebook's cells and explore controlled variations.
3. **Implement** (2–3 h): solve the assignment in `challenges.py`, writing tests first.
4. **Review** (60 min): inspect the code and AI suggestions; run regression tests.
5. **Deliver** (45–60 min): commit to a feature branch with a clear change summary.

The timeline is flexible: a working deliverable matters more than finishing a week on a fixed calendar.

## Source control and collaboration

```bash
git init
git add .
git commit -m "chore: initialize seismic Python AI course"
git branch -M main
# After creating an empty repository on GitHub, replace the URL below:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

If an origin already exists, use `git remote -v` to inspect it and `git remote set-url origin <CORRECT_URL>` to fix it. For each weekly task, create a feature branch (`git switch -c feature/week01-normalization`), commit only the relevant files, push it and open a pull request.

## AI safety and confidentiality

The notebooks demonstrate AI-assisted programming **without accessing external AI services**. For AI prompts, templates and review checklists see [`resources/ai_prompts.md`](resources/ai_prompts.md). Treat AI-generated code as untrusted until inspected and tested. Do not paste internal lab code, licensed data, credentials, customer information or proprietary architecture into public AI tools without authorization.

## Reproducibility and verification

- Seeded synthetic datasets; no network calls in notebook execution.
- Tests use `pytest`; GitHub Actions runs standard checks on push/PR.
- Source computations stay outside notebooks so the same code can run in tests, a CLI or an app.
- ML pipelines fit preprocessing inside training folds and support separate `group` identifiers to reduce correlated-data leakage.
- Results on synthetic data are didactic; even flawless code does not demonstrate reservoir-model validity.

## Study materials

- [Python documentation](https://docs.python.org/3/)
- [Python packaging tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [pytest documentation](https://docs.pytest.org/en/stable/)
- [Git book](https://git-scm.com/book/en/v2)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Streamlit documentation](https://docs.streamlit.io/)

Some optional readings are online; course execution and examples are offline once dependencies are installed.

## License and contributions

Example code and original instructional materials are released under the [MIT License](LICENSE). See [`CONTRIBUTING.md`](CONTRIBUTING.md) for suggested review practices. This is an educational course, not affiliated with a university, lab or company.
