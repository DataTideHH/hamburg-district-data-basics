# Data Dictionary

This data dictionary describes the processed district-level analysis file:

```text
data/processed/altona_district_profiles_2024.csv
```

The dataset grain is **one row per district / Stadtteil** within the borough of Altona.

| Column | Meaning | Unit / format | Reporting period | Aggregation and validation notes |
|---|---|---|---|---|
| `district` | Hamburg district / Stadtteil name | text | 2024 profile edition | Unique; one of 14 expected Altona districts |
| `borough` | Hamburg borough / Bezirk | text | 2024 profile edition | Must equal `Altona` |
| `population` | Resident population | persons | 2024 profile edition | Positive; additive |
| `area_km2` | District area | km² | 2024 profile edition | Positive; additive |
| `population_density` | Published district population density | residents/km² | 2024 profile edition | Positive; checked against population / area within rounding tolerance; do not average for an overall density |
| `under_18_percent` | Residents under 18 | percent | 2024 profile edition | 0–100; district-level rate |
| `over_64_percent` | Residents aged 65 and older | percent | 2024 profile edition | 0–100; district-level rate |
| `unemployment_share_percent_dec_2024` | Unemployed persons among residents aged 15 to under 65 | percent | December 2024 | 0–100; overall Altona value requires original numerator and denominator |
| `sgb2_share_percent_dec_2024` | SGB II recipients as share of population | percent | December 2024 | 0–100; overall Altona value requires original numerator and denominator |
| `avg_income_per_taxpayer_2021_eur` | Average income per taxpayer | EUR | 2021 | Positive district-level average; overall Altona average requires taxpayer counts |
| `general_practitioners_jan_2025` | General practitioners | count | January 2025 | Non-negative; additive as a count, but service interpretation also needs population context |
| `pharmacies_dec_2024` | Pharmacies | count | December 2024 | Non-negative; additive as a count, but service interpretation also needs population context |
| `private_cars_per_1000_jan_2025` | Private cars per 1,000 residents | rate | January 2025 | Non-negative district-level rate; overall rate requires car and population counts |
| `electric_cars_jan_2025` | Electric cars | count | January 2025 | Non-negative; additive |

## Time and Aggregation Semantics

The dataset combines different reporting periods. Visuals and calculations must retain those dates in titles, labels or metadata.

Additive columns can be summed across districts. District-level averages, percentages and rates cannot automatically be averaged into a correct borough-wide KPI. Where the source numerator and denominator are unavailable, the project uses district comparisons, rankings or explicitly labelled district medians instead.

## Contract

The executable contract is maintained in [`../src/data_contract.py`](../src/data_contract.py). Source mappings and transformations are maintained in [`data-lineage.csv`](data-lineage.csv).
