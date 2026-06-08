# Data Dictionary

This data dictionary describes the processed analysis file used in this repository.

Processed file:

    data/processed/altona_district_profiles_2024.csv

Source context:

- Source title: Hamburger Stadtteil-Profile
- Reporting year: 2024
- Publisher: Statistikamt Nord
- Current analysis scope: Altona borough, Hamburg
- Geographic level: Stadtteil / district

## Columns

| Column | Meaning | Unit / Format | Source indicator / note |
|---|---|---|---|
| district | Hamburg district / Stadtteil name | text | German district name from the official profile |
| borough | Hamburg borough / Bezirk | text | Current analysis uses Altona |
| population | Resident population | persons | Bevölkerung |
| area_km2 | District area | square kilometres | Fläche in km² |
| population_density | Population density | residents per km² | Einwohner:innen je km² |
| under_18_percent | Share of residents under 18 | percent | Unter 18-Jährige, in % der Bevölkerung |
| over_64_percent | Share of residents aged 65 and older | percent | 65-Jährige und Ältere, in % der Bevölkerung |
| unemployment_share_percent_dec_2024 | Share of unemployed persons | percent | Arbeitslose, in % der 15- bis unter 65-Jährigen, December 2024 |
| sgb2_share_percent_dec_2024 | Share of SGB II recipients | percent | Leistungsempfänger:innen nach SGB II, in % der Bevölkerung, December 2024 |
| avg_income_per_taxpayer_2021_eur | Average income per taxpayer | EUR | Einkommen je Steuerpflichtigen in Euro, 2021 |
| general_practitioners_jan_2025 | General practitioners | count | Allgemeinärztinnen/-ärzte, January 2025 |
| pharmacies_dec_2024 | Pharmacies | count | Apotheken, December 2024 |
| private_cars_per_1000_jan_2025 | Private cars per 1,000 residents | cars per 1,000 residents | Private PKW je 1 000 der Bevölkerung, January 2025 |
| electric_cars_jan_2025 | Electric cars | count | Elektro-PKW, January 2025 |

## Notes on Time References

The indicators do not all refer to the same reporting date.

Important examples:

- average income per taxpayer refers to 2021
- unemployment share refers to December 2024
- SGB II share refers to December 2024
- general practitioners refer to January 2025
- pharmacies refer to December 2024
- private cars and electric cars refer to January 2025

This matters for interpretation. The processed CSV is useful for descriptive comparison, but it should not be treated as a single-day snapshot.

## Interpretation Notes

The dataset is intentionally small and limited to 14 districts in the borough of Altona.

It supports:

- descriptive comparison
- ranking tables
- basic visualizations
- first portfolio documentation
- preparation for Power BI modelling

It does not support:

- causal claims
- full Hamburg-wide comparison
- detailed socio-economic modelling
- time-series analysis

## Planned Improvements

Possible next improvements:

1. Add all Hamburg boroughs.
2. Add original German source labels for a broader indicator set.
3. Add a structured Power BI model later.
4. Add source extraction notes when more data is added.
