# Hamburg District Data Basics

Initial exploratory data analysis scaffold for public Hamburg district profile data.

## Purpose

This repository is the starting point for a small, reproducible Data/BI learning project based on public Hamburg district data.

The goal is to practice:

- dataset documentation
- data source tracking
- basic exploratory data analysis
- clean project structure
- Python-based analysis workflows
- later Power BI / dashboard preparation

## Current Status

This repository is an initial scaffold.

No raw source data is committed yet. The next step is to document the selected source dataset, extract a small structured table and build a first basic analysis.

## Planned Data Source

The planned starting point is the public Hamburg district profile publication by Statistikamt Nord:

- Hamburger Stadtteil-Profile
- Berichtsjahr 2024
- public district-level profile data for Hamburg

The original PDF source is documented in `docs/data-sources.md`.

## Repository Structure

```text
hamburg-district-data-basics/
├── data/
│   ├── README.md
│   └── raw/
│       └── .gitkeep
├── docs/
│   └── data-sources.md
├── notebooks/
│   └── README.md
├── src/
│   ├── README.md
│   └── check_environment.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Run Environment Check

```zsh
python3 src/check_environment.py
```

Expected output:

```text
Hamburg District Data Basics
Python version: ...
Project scaffold is ready.
```

## Planned Workflow

1. Select a small subset of Hamburg district indicators.
2. Convert the source into a structured CSV table.
3. Load the data with pandas.
4. Run basic checks and descriptive analysis.
5. Create first simple visualizations.
6. Prepare the dataset for later Power BI usage.

## What This Repository Demonstrates

- Data source documentation
- Reproducible project setup
- Python environment basics
- pandas-based data analysis preparation
- Hamburg-focused Data/BI project planning

## Next Steps

- add first structured CSV extract
- create first pandas analysis script
- add basic charts
- document first findings
- optionally connect the prepared data to Power BI

## License

MIT License.
