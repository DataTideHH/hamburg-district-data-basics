# Notebooks

The notebook provides a readable exploration of the validated Altona district dataset:

```text
01_altona_district_profiles_2024.ipynb
```

It uses the same shared functions as the command-line workflow for:

- dataset loading and contract validation
- canonical summary metrics
- long-format rankings
- descriptive correlations
- figure generation

This avoids maintaining separate analytical logic in the notebook and script.

Run from the repository root:

```bash
source .venv/bin/activate
jupyter notebook notebooks/01_altona_district_profiles_2024.ipynb
```

The committed notebook is intended as a readable review artifact. Re-execution requires the processed CSV and installed project dependencies.
