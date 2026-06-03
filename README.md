# Hamburg District Data Basics

Small exploratory data analysis project based on public Hamburg district profile data.

This repository is part of my DataTideHH portfolio and documents a first practical Data/BI workflow: source documentation, structured CSV data, Python-based analysis, generated visualizations and short written findings.

## Purpose

The goal of this repository is to practice a small, reproducible data analysis workflow using public Hamburg district-level data.

The project demonstrates:

- data source documentation
- structured CSV preparation
- basic exploratory data analysis with Python and pandas
- first descriptive statistics and rankings
- simple matplotlib visualizations
- short written findings
- preparation for later Power BI / dashboard work

## Current Status

The repository now contains a first focused analysis of selected district profile indicators for the borough of Altona.

The first analysis includes:

- a processed CSV dataset for Altona districts
- a Python/pandas analysis script
- four generated PNG figures
- a short findings report

## Data Source

The analysis is based on a processed extract from the official Hamburg District Profiles 2024.

Source context:

- Hamburger Stadtteil-Profile
- Berichtsjahr 2024
- published by Statistikamt Nord
- public district-level profile data for Hamburg

The original source is documented in:

```text
docs/data-sources.md
```

The processed analysis file is:

```text
data/processed/altona_district_profiles_2024.csv
```

## First Analysis: Altona District Profiles 2024

This first analysis focuses on all districts within the borough of Altona.

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

## Repository Structure

```text
hamburg-district-data-basics/
├── data/
│   ├── README.md
│   ├── processed/
│   │   └── altona_district_profiles_2024.csv
│   └── raw/
│       └── .gitkeep
├── docs/
│   └── data-sources.md
├── notebooks/
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
```

## Run the Environment Check

```zsh
python3 src/check_environment.py
```

Expected output:

```text
Hamburg District Data Basics
Python version: ...
Project scaffold is ready.
```

## Run the Altona Analysis

Create and activate a local virtual environment:

```zsh
python3.12 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```zsh
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run the analysis:

```zsh
python src/analyze_altona_profiles.py
```

The script loads the processed CSV file, prints basic checks and rankings, and creates figures in:

```text
reports/figures/
```

## Generated Figures

The analysis currently creates the following figures:

- `reports/figures/population_by_district_altona_2024.png`
- `reports/figures/population_density_by_district_altona_2024.png`
- `reports/figures/private_cars_per_1000_altona_2024.png`
- `reports/figures/income_vs_sgb2_share_altona_2024.png`

## Findings

The first written findings are documented in:

```text
reports/findings.md
```

The initial observations focus on:

- population differences between Altona districts
- density differences between inner-city and western districts
- private car density
- differences in social indicators
- the contrast between average income and SGB II share

## What This Repository Demonstrates

This repository demonstrates a compact practical Data/BI workflow:

- public data source tracking
- manual processed data extract
- reproducible Python analysis
- pandas-based data loading and checks
- matplotlib-based chart generation
- short written findings
- Hamburg-focused portfolio documentation
- preparation for a later Power BI dashboard

## Next Steps

Possible next steps:

- add a short Power BI preparation note
- document possible Power BI model structure
- add KPI ideas for a first dashboard
- extend the analysis with borough-level context
- add a methodology note explaining the focused Altona extract
- optionally add a notebook version of the analysis

## Tools Used

- Python 3.12
- pandas
- matplotlib
- PyCharm / DataSpell
- Git / GitHub

## License

MIT License.
