# Hamburg District Data Basics

**Public Hamburg district data · Altona case study · Python/pandas · data quality · exploratory analysis · BI-style interpretation · Power BI preparation**

This repository documents a small, reproducible Data/BI workflow based on official Hamburg district profile data. The current scope is deliberately limited to the **14 districts in the borough of Altona** so that the source, transformations, findings and limitations remain easy to review.

The project supports my learning path toward **Data/BI Analyst** roles with a focus on SQL, Python, Power BI, data quality, process-oriented analytics and the Microsoft Data Stack.

---

## Results at a Glance

The processed dataset covers **281,136 residents across 77.8 km²**.

| Indicator | Current descriptive result |
|---|---|
| Largest population | **Lurup** — 37,755 residents |
| Highest population density | **Sternschanze** — 15,338 residents/km² |
| Highest average income per taxpayer | **Nienstedten** — €168,404 |
| Highest unemployment share | **Lurup** — 8.5% |
| Highest SGB II share | **Lurup** — 14.7% |
| Highest private-car rate | **Nienstedten** — 502 cars per 1,000 residents |

Within this small dataset, average income is negatively correlated with SGB II share (**-0.86**) and unemployment share (**-0.91**). These are descriptive relationships only and do not establish causality.

The complete written interpretation is available in [`reports/findings.md`](reports/findings.md).

### Selected Analysis Outputs

<table>
<tr>
<td width="50%">
<img src="reports/figures/population_by_district_altona_2024.png" alt="Population by district in Altona, 2024">
</td>
<td width="50%">
<img src="reports/figures/population_density_by_district_altona_2024.png" alt="Population density by district in Altona, 2024">
</td>
</tr>
<tr>
<td width="50%">
<img src="reports/figures/income_vs_sgb2_share_altona_2024.png" alt="Average income compared with SGB II share in Altona districts">
</td>
<td width="50%">
<img src="reports/figures/private_cars_per_1000_altona_2024.png" alt="Private cars per 1,000 residents in Altona districts">
</td>
</tr>
</table>

---

## Business and BI Questions

The workflow supports descriptive questions such as:

- Which Altona districts differ most strongly by population size and density?
- How do income, unemployment share and SGB II share differ across districts?
- Which districts show unusually high or low private-car ownership?
- Which indicators are suitable for a compact Power BI report?
- Which interpretation limits must be made visible to report users?

The purpose is not to produce a complete urban-policy analysis. It is to demonstrate a transparent path from public source data to structured analysis, visual outputs and BI-oriented interpretation.

---

## Data Source and Scope

| Item | Value |
|---|---|
| Source | [Hamburger Stadtteil-Profile 2024](https://www.statistik-nord.de/fileadmin/user_upload/Stadtteil-Profile-HH_BJ-2024.pdf) |
| Publisher | Statistikamt Nord |
| Geographic grain | Hamburg district / Stadtteil |
| Current scope | 14 districts in the borough of Altona |
| Source access date | 8 June 2026 |
| Processed dataset | [`data/processed/altona_district_profiles_2024.csv`](data/processed/altona_district_profiles_2024.csv) |

Selected indicators include population, area, population density, age structure, unemployment share, SGB II share, average income per taxpayer, healthcare access and car ownership.

The indicators do not all refer to the same reporting date. Exact definitions, original context and time references are documented in:

- [`docs/data-sources.md`](docs/data-sources.md)
- [`docs/data-dictionary.md`](docs/data-dictionary.md)

---

## Reproducible Workflow

```text
official district-profile source
              |
              v
documented processed CSV extract
              |
              v
Python/pandas validation and analysis
              |
              v
descriptive summaries and rankings
              |
              v
matplotlib figures and written findings
              |
              v
Power BI dashboard preparation
```

The workflow currently:

1. documents the official source and reporting context
2. maintains a compact processed CSV extract
3. validates the local Python environment
4. loads and analyses the dataset with pandas
5. generates descriptive statistics, rankings and correlations
6. writes four reusable chart artifacts
7. documents findings and interpretation limits
8. prepares a later Power BI reporting layer

---

## Repository Structure

```text
hamburg-district-data-basics/
├── data/
│   └── processed/
│       └── altona_district_profiles_2024.csv
├── docs/
│   ├── data-dictionary.md
│   ├── data-sources.md
│   └── power-bi-dashboard-plan.md
├── notebooks/
│   └── 01_altona_district_profiles_2024.ipynb
├── reports/
│   ├── findings.md
│   └── figures/
│       ├── income_vs_sgb2_share_altona_2024.png
│       ├── population_by_district_altona_2024.png
│       ├── population_density_by_district_altona_2024.png
│       └── private_cars_per_1000_altona_2024.png
├── src/
│   ├── analyze_altona_profiles.py
│   └── check_environment.py
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Run Locally

The project targets Python 3.12.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python src/check_environment.py
python src/analyze_altona_profiles.py
```

On Windows PowerShell, activate the environment with:

```powershell
.\.venv\Scripts\Activate.ps1
```

The analysis script generates the figures under `reports/figures/`. Notebook-based exploration is available in [`notebooks/01_altona_district_profiles_2024.ipynb`](notebooks/01_altona_district_profiles_2024.ipynb).

---

## What This Demonstrates

- translating a public source into a documented analysis dataset
- defining dataset grain, scope and limitations
- using Python and pandas for descriptive analysis
- producing reusable report figures with matplotlib
- separating data, code, documentation and findings
- distinguishing descriptive relationships from causal claims
- preparing analytical outputs for a later BI report
- keeping a portfolio project small, reproducible and reviewable

---

## Power BI Status and Next Milestone

Power BI is **not presented as completed** in the current repository.

The planned reporting layer is documented in [`docs/power-bi-dashboard-plan.md`](docs/power-bi-dashboard-plan.md). A useful first version would include:

- KPI cards for population, density and selected social indicators
- district comparison charts
- a scatterplot for selected indicator relationships
- clear source, time-reference and limitation notes
- a simple explainable data model based on the processed CSV

The next substantive milestone is a small Power BI prototype with a reviewed public screenshot and documented measures. Expansion to all Hamburg boroughs should follow only after the Altona workflow and dashboard are stable.

---

## Interpretation Limits

This is a descriptive portfolio analysis, not a causal model.

Important limitations:

- only one Hamburg borough is included
- the dataset contains 14 observations
- indicators use different reporting dates
- absolute counts, rates and ratios must not be compared without context
- the workflow does not control for demographics, housing, land use or transport access
- correlations in this dataset do not establish causality

---

## License

This project is licensed under the terms in [`LICENSE`](LICENSE).
