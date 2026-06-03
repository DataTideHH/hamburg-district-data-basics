# Data Sources

## Primary planned source

**Hamburger Stadtteil-Profile: Berichtsjahr 2024**
Publisher: Statistikamt Nord
Source URL: https://www.statistik-nord.de/fileadmin/user_upload/Stadtteil-Profile-HH_BJ-2024.pdf

## Notes

This repository does not currently include raw source data.

The first implementation step will be to extract a small, clearly documented subset of indicators from the public source into a structured CSV file.

Planned initial indicators may include:

- district name
- borough
- population
- share of people under 18
- share of people aged 65 and older
- share of foreign residents
- unemployment rate
- income indicators where available

## Data handling decision

Raw source files are not committed by default.

Small derived CSV files may be committed later if they are clearly documented and suitable for reproducible learning purposes.

## Hamburg District Profiles 2024 — Altona Extract

This project uses a manually curated processed extract from the official Hamburg District Profiles 2024.

Source context:

- Publisher: Statistikamt Nord
- Dataset: Hamburger Stadtteil-Profile
- Reporting year: 2024
- Unit of analysis: Hamburg district / Stadtteil
- Current project scope: districts within the borough of Altona

Processed file:

```text
data/processed/altona_district_profiles_2024.csv
```

The processed dataset is intentionally small and focused. It is used for a first reproducible portfolio analysis with Python, pandas, matplotlib and written findings.

Selected districts:

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

Notes:

- The current CSV is a processed analysis extract, not the full official source dataset.
- The extract is intended for a first portfolio-ready exploratory analysis.
- The original source should be cited when reusing or extending the dataset.
- Future work can extend the analysis with additional indicators, borough-level context and a Power BI model.

