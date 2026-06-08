# Data Sources

## Main Source

This project uses a processed extract from the official Hamburg district profile data.

Source context:

- Title: Hamburger Stadtteil-Profile
- Reporting year: 2024
- Publisher: Statistikamt Nord
- Geographic scope: Hamburg
- Current analysis scope: districts within the borough of Altona
- Data granularity: Stadtteil / district level

## Processed Dataset

Current processed file:

    data/processed/altona_district_profiles_2024.csv

The file contains selected indicators for 14 Altona districts.

Current columns:

- district
- borough
- population
- area_km2
- population_density
- under_18_percent
- over_64_percent
- unemployment_share_percent_dec_2024
- sgb2_share_percent_dec_2024
- avg_income_per_taxpayer_2021_eur
- general_practitioners_jan_2025
- pharmacies_dec_2024
- private_cars_per_1000_jan_2025
- electric_cars_jan_2025

## Transformation Status

The current dataset is a processed analysis extract, not a full raw source mirror.

The project currently focuses on a small, readable CSV file that supports a first reproducible analysis workflow.

Current transformation principles:

- use clear English column names
- keep units in column names where useful
- keep reporting dates in column names when indicators refer to different years or months
- avoid publishing unnecessary raw source material
- document interpretation limits directly in the repository

## Time References

The indicators do not all refer to the same point in time.

Examples:

- district profiles: reporting year 2024
- unemployment share: December 2024
- SGB II share: December 2024
- average income per taxpayer: 2021
- general practitioners: January 2025
- pharmacies: December 2024
- private cars and electric cars: January 2025

This matters because the dataset combines indicators from different reporting dates.

## Licensing and Reuse Notes

Before adding larger raw files or redistributing full official source datasets, the exact source URL, publisher notice and reuse conditions should be checked and documented.

This repository currently uses a compact processed extract for learning and portfolio documentation.

## Analytical Limitations

The current dataset supports descriptive comparison only.

It should not be used for causal statements such as:

- income causes lower unemployment
- car ownership causes specific social outcomes
- density directly explains social structure

The dataset is useful for:

- descriptive comparison
- first ranking tables
- chart generation
- data-cleaning practice
- preparing later dashboard work

## Planned Improvements

Next source documentation improvements:

1. Add exact source URL.
2. Add source access date.
3. Add publisher license or reuse statement.
4. Add a data dictionary with original German indicator names.
5. Add notes on manual extraction or transformation steps.
