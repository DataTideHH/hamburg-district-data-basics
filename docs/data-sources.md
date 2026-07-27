# Data Sources

## Main Source

This project uses a processed extract from the official Hamburg district-profile publication.

| Item | Value |
|---|---|
| Title | Hamburger Stadtteil-Profile |
| Reporting edition | 2024 |
| Publisher | Statistikamt Nord |
| Geographic scope | Hamburg |
| Current analysis scope | Districts within the borough of Altona |
| Data grain | One row per Stadtteil / district |
| Source format | PDF |
| Official source | https://www.statistik-nord.de/fileadmin/user_upload/Stadtteil-Profile-HH_BJ-2024.pdf |
| Documentation access date | 2026-06-08 |

## Processed Dataset

Current processed file:

```text
data/processed/altona_district_profiles_2024.csv
```

The file contains selected indicators for 14 Altona districts. It is a compact analysis extract, not a complete mirror of the source publication.

Supporting documentation:

- [`data-dictionary.md`](data-dictionary.md)
- [`extraction-method.md`](extraction-method.md)
- [`data-lineage.csv`](data-lineage.csv)

## Reporting Periods

The indicators do not all refer to the same point in time.

| Indicator group | Reporting period |
|---|---|
| District profile population, area and age structure | 2024 profile edition |
| Unemployment share | December 2024 |
| SGB II share | December 2024 |
| Average income per taxpayer | 2021 |
| General practitioners | January 2025 |
| Pharmacies | December 2024 |
| Private cars and electric cars | January 2025 |

The processed extract must therefore not be described as a single-date snapshot.

## Transformation Boundary

The repository:

- retains the district-level grain
- uses clear English technical column names
- includes units or reporting dates in column names where material
- preserves the published values without modelling missing denominators
- does not infer causal relationships
- does not redistribute the complete source PDF

The validation layer checks schema, domains and selected cross-field consistency. It does not replace source-value verification against the official publication.

## Reuse and Licensing

The repository's MIT License applies to original code and documentation.

The processed extract is derived from the cited official publication. Source data, publisher content and attribution remain subject to the publisher's applicable terms. Before expanding or redistributing larger source extracts, the relevant publisher notice and reuse conditions should be checked again.
