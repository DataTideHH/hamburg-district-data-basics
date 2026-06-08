# Hamburg District Data Basics

Small exploratory data analysis project based on public Hamburg district profile data.

This repository is part of my DataTideHH portfolio and documents a practical Data/BI workflow: source documentation, structured CSV data, Python-based analysis, generated visualizations and short written findings.

## Purpose

The goal of this repository is to practice a small, reproducible data analysis workflow using public Hamburg district-level data.

The project demonstrates:

- source documentation
- structured CSV preparation
- basic exploratory data analysis with Python and pandas
- descriptive statistics and simple rankings
- matplotlib-based visualizations
- written findings with clear interpretation limits
- preparation for later Power BI or dashboard work

## Current Scope

The current version focuses on selected district profile indicators for the borough of Altona, Hamburg.

The analysis is intentionally small and transparent. It is not meant to be a complete Hamburg-wide data platform yet. The current goal is to show a clean workflow from documented source data to reproducible analysis output.

## Data Source

The analysis is based on a processed extract from the official Hamburg District Profiles 2024.

Source context:

- Hamburger Stadtteil-Profile
- Reporting year: 2024
- Publisher: Statistikamt Nord
- Granularity: Hamburg city districts / Stadtteile
- Current analysis focus: Altona borough

The source documentation is maintained in:

    docs/data-sources.md

The data dictionary is maintained in:

    docs/data-dictionary.md

The processed analysis file is:

    data/processed/altona_district_profiles_2024.csv

## Dataset

The processed CSV contains 14 Altona districts.

Included districts:

- Altona-Altstadt
- Sternschanze
- Altona-Nord
- Ottensen
- Bahrenfeld
- Groß Flottbek
- Othmarschen
- Lurup
- Osdorf
- Nienstedten
- Blankenese
- Iserbrook
- Sülldorf
- Rissen

Selected indicators include:

- population
- area
- population density
- age structure
- unemployment share
- SGB II share
- average income per taxpayer
- general practitioners
- pharmacies
- private cars per 1,000 residents
- electric cars

## Analysis Workflow

The current workflow is:

1. maintain a processed CSV extract
2. validate the local Python environment
3. load the dataset with pandas
4. calculate descriptive summaries and rankings
5. generate selected charts with matplotlib
6. document findings and limitations

## Repository Structure

    hamburg-district-data-basics/
    ├── data/
    │   ├── README.md
    │   ├── processed/
    │   │   └── altona_district_profiles_2024.csv
    │   └── raw/
    │       └── .gitkeep
    ├── docs/
    │   ├── data-dictionary.md
    │   └── data-sources.md
    ├── notebooks/
    │   ├── 01_altona_district_profiles_2024.ipynb
    │   └── README.md
    ├── reports/
    │   ├── findings.md
    │   └── figures/
    │       ├── income_vs_sgb2_share_altona_2024.png
    │       ├── population_by_district_altona_2024.png
    │       ├── population_density_by_district_altona_2024.png
    │       └── private_cars_per_1000_altona_2024.png
    ├── src/
    │   ├── README.md
    │   ├── analyze_altona_profiles.py
    │   └── check_environment.py
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    └── requirements.txt

## How to Run

Create and activate a virtual environment:

    python3.12 -m venv .venv
    source .venv/bin/activate

Install dependencies:

    python -m pip install -r requirements.txt

Check the environment:

    python src/check_environment.py

Run the analysis:

    python src/analyze_altona_profiles.py

## Outputs

The analysis script generates figures in:

    reports/figures/

The written findings are documented in:

    reports/findings.md

The notebook-based exploration is available in:

    notebooks/01_altona_district_profiles_2024.ipynb

## What This Demonstrates

This project demonstrates a practical early-stage Data/BI workflow:

- turning public source data into a structured analysis dataset
- documenting source context and limitations
- using Python and pandas for lightweight analysis
- generating charts as reusable report artifacts
- separating data, scripts, documentation and reports
- keeping the project small enough to be understandable and maintainable

## Interpretation Limits

This is a descriptive analysis, not a causal model.

The current dataset is small and limited to one Hamburg borough. Indicators should not be interpreted without understanding the source definitions, reporting year, granularity and local context.

## Next Steps

Planned improvements:

- extend the analysis to additional Hamburg boroughs
- add population-density and social-indicator comparison charts
- prepare a later Power BI version with a clean data model
