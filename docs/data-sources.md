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
- Source file type: PDF

Official source URL:

    https://www.statistik-nord.de/fileadmin/user_upload/Stadtteil-Profile-HH_BJ-2024.pdf

Access date for this repository documentation:

    2026-06-08

## Processed Dataset

Current processed file:

    data/processed/altona_district_profiles_2024.csv

The file contains selected indicators for 14 Altona districts.

Current columns are documented in:

    docs/data-dictionary.md

## Source Coverage

The official PDF covers Hamburg city districts across all boroughs.

This repository currently uses only selected indicators for the Altona borough. The current project scope is intentionally limited in order to keep the first workflow readable and maintainable.

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

The repository uses a compact processed extract for learning and portfolio documentation.

Before adding larger raw files or redistributing full official source datasets, the exact publisher notice and reuse conditions should be checked again directly on the official source page or related Statistikamt Nord publication notes.

The project therefore does not mirror the full PDF as a raw data file.

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

1. Add a more detailed source retrieval note if additional indicators are extracted.
2. Add all original German indicator labels for any expanded dataset.
3. Add a full Hamburg-wide processed dataset later.
4. Document Power BI data-model assumptions when a dashboard version is added.
