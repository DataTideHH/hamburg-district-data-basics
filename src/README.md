# Source Code

| File | Responsibility |
|---|---|
| `data_contract.py` | Expected schema, district set, domain rules and cross-field validation |
| `analysis_workflow.py` | Shared loading, metrics, rankings, correlations and artifact generation |
| `analyze_altona_profiles.py` | Command-line orchestration and concise run summary |
| `check_environment.py` | Minimum Python runtime and installed-library check |

Run the complete workflow from the repository root:

```bash
python -m src.analyze_altona_profiles
```

The notebook and tests import the same shared functions so that calculation and validation logic remains centralized.
