# Hamburg District Data Basics

**Public Hamburg district data · Altona case study · Python/pandas · exploratory analysis · data quality · BI-style interpretation · Power BI preparation**

This repository documents a small, reproducible Data/BI workflow based on public Hamburg district profile data.

The repository name is intentionally broader, but the current analysis scope is deliberately limited to the **Altona borough in Hamburg** as a first reproducible case study. This keeps the project small, transparent and easy to review before expanding it to additional districts or boroughs.

It is part of my broader **DataTideHH portfolio** and supports my learning path toward **Data/BI Analyst** roles with a focus on SQL, Python, Power BI, Microsoft Fabric/Azure fundamentals, data quality and process-oriented analytics.

---

## Why This Project Matters for Data/BI

Many practical Data/BI tasks start with public, operational or semi-structured source data and require a clear path from source understanding to useful interpretation.

This project demonstrates that workflow on a small and transparent local dataset:

- document the data source
- define the dataset scope
- prepare a structured CSV file
- describe indicators and limitations
- run reproducible Python/pandas analysis
- generate reusable charts
- document short findings
- prepare the result for later Power BI dashboard work

The goal is not to build a complete Hamburg-wide data platform yet. The goal is to show a clean and understandable workflow from public district data to BI-style questions and documented insights.

---

## Business and BI Questions

This project can support practical BI-style questions such as:

- Which Altona districts differ most strongly by population size or density?
- Which districts show higher or lower values for selected social indicators?
- How do income, SGB II share, unemployment share and car ownership differ across districts?
- Which indicators would be useful for a compact Power BI dashboard?
- What are the interpretation limits of a small district-level dataset?

These questions are descriptive. They help structure analysis and reporting, but they do not prove causal relationships.

---

## Current Scope

The current version focuses on selected district profile indicators for the **borough of Altona, Hamburg**.

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

The analysis is intentionally small and transparent. This makes it easier to review the data source, the processing steps, the generated charts and the written interpretation.

---

## Data Source

The analysis is based on a processed extract from the official Hamburg district profiles.

Source context:

| Item | Value |
|---|---|
| Source | Hamburger Stadtteil-Profile |
| Reporting year | 2024 |
| Publisher | Statistikamt Nord |
| Granularity | Hamburg city districts / Stadtteile |
| Current analysis focus | Altona borough |

The source documentation is maintained in:

```text
docs/data-sources.md
```

The data dictionary is maintained in:

```text
docs/data-dictionary.md
```

The processed analysis file is:

```text
data/processed/altona_district_profiles_2024.csv
```

---

## Dataset

The processed CSV contains **14 Altona districts**.

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

The dataset is intentionally limited. It is suitable for exploratory analysis, documentation practice and BI preparation, but not for broad policy conclusions without additional data and context.

---

## Analysis Workflow

The current workflow is:

1. document the public data source
2. maintain a processed CSV extract
3. validate the local Python environment
4. load the dataset with pandas
5. calculate descriptive summaries and rankings
6. generate selected charts with matplotlib
7. document findings and limitations
8. prepare a later Power BI dashboard concept

---

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
│   ├── data-dictionary.md
│   ├── data-sources.md
│   └── power-bi-dashboard-plan.md
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
```

---

## How to Run

Create and activate a virtual environment:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Check the environment:

```bash
python src/check_environment.py
```

Run the analysis:

```bash
python src/analyze_altona_profiles.py
```

---

## Outputs

The analysis script generates figures in:

```text
reports/figures/
```

The written findings are documented in:

```text
reports/findings.md
```

The notebook-based exploration is available in:

```text
notebooks/01_altona_district_profiles_2024.ipynb
```

The planned Power BI dashboard structure is documented in:

```text
docs/power-bi-dashboard-plan.md
```

---

## What This Demonstrates

This project demonstrates a practical early-stage Data/BI workflow:

- turning public source data into a structured analysis dataset
- documenting source context and limitations
- using Python and pandas for lightweight analysis
- creating descriptive statistics and rankings
- generating charts as reusable report artifacts
- separating data, scripts, documentation and reports
- preparing analysis outputs for BI/dashboard thinking
- keeping the project small enough to be understandable and maintainable

---

## BI Perspective

The project is currently Python/pandas-based, but it is structured to support a later Power BI version.

A useful next BI layer would include:

- a compact district overview page
- KPI cards for population, density and selected social indicators
- bar charts for district comparisons
- scatterplots for indicator relationships
- clear source and limitation notes
- a simple data model based on the processed CSV

Power BI is not presented as a completed part of this repository yet. It is the next reporting layer after the Python analysis, findings and dataset documentation.

---

## Interpretation Limits

This is a descriptive analysis, not a causal model.

The current dataset is small and limited to one Hamburg borough. Indicators should not be interpreted without understanding the source definitions, reporting year, granularity and local context.

The project should be read as a portfolio and learning project for reproducible Data/BI workflows, not as a complete urban policy analysis.

---

## Roadmap: From Altona Case Study to Hamburg BI Dashboard

Planned improvements are intentionally incremental:

1. improve the current Altona findings and chart descriptions
2. add simple data quality checks for missing values and indicator ranges
3. refine the Power BI dashboard plan
4. create a first Power BI dashboard based on the processed CSV
5. document the Power BI data model and dashboard pages
6. extend the analysis to additional Hamburg boroughs
7. later connect the project conceptually to Microsoft Fabric/Azure as a platform perspective

---

## Notes

This repository is intended as a practical, transparent and locally relevant Data/BI portfolio project.

It is deliberately small, documented and reproducible. That makes it useful for explaining data workflows to recruiters, internship providers and technical reviewers.
