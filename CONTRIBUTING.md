# Contribution guide

This is a learning repository. Contributions should improve clarity, correctness, reproducibility and safety.

## Pull request checklist

- [ ] One change per focused feature branch.
- [ ] Existing baseline tests remain green: `python -m pytest -q`.
- [ ] New behavior has new tests, including an invalid-input or edge-case test.
- [ ] Numerical units and sign conventions are documented.
- [ ] New dependencies are justified in `pyproject.toml`.
- [ ] Notebook cells are executable sequentially; bulky outputs are cleared before commit.
- [ ] No credentials, private workplace data, real seismic volumes or licensed software are included.
- [ ] Any assistance by generative AI was reviewed and tested by a human.

## Style

Prefer small, typed functions, descriptive identifiers, concise docstrings and explicit validation at module boundaries. Make input data and random seeds reproducible. Keep core computation independent of notebooks and UI frameworks.

## Issue template

Describe expected behavior, actual behavior, a minimal reproducible example using synthetic inputs, Python version, and output from `pytest`. For scientific issues, include units and a clearly defined sign convention.
