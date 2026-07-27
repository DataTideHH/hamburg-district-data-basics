# Extraction Method

## Purpose

This document records how the current Altona district extract was created and how future updates should be reviewed. It provides a source-to-processed-data audit trail without redistributing the complete official PDF.

## Current Method

The current CSV is a manually curated extract from the official **Hamburger Stadtteil-Profile 2024** PDF.

The workflow used for the portfolio dataset is:

1. identify the Altona district rows in the official district-profile tables
2. select a bounded indicator set relevant to descriptive Data/BI analysis
3. transfer the published values into a structured CSV
4. convert technical column names to English while retaining source meaning
5. include units and material reporting dates in column names
6. compare the completed rows against the source tables
7. run automated schema, domain and density-consistency validation
8. generate analytical artifacts from the validated CSV

No OCR-derived raw dump or complete PDF table export is committed.

## Transformation Rules

| Source characteristic | Processed treatment |
|---|---|
| German district names | Preserved, including umlauts and punctuation |
| German indicator labels | Mapped to documented English column names |
| Decimal comma in source context | Stored as decimal point in CSV numeric fields |
| Thousands separators | Removed before numeric storage |
| Percent values | Stored as numeric percentage points, for example `8.5` |
| Counts | Stored as non-negative integers |
| Area | Stored in square kilometres |
| Population density | Stored as published residents per km² and checked against population / area |
| Different reporting dates | Retained in column names and lineage documentation |

## Review Controls

The current extract is reviewed through two different control layers.

### Source-transfer review

- confirm district names and row alignment
- compare selected values with the official source
- verify units and reporting dates
- review the source-to-column mapping

### Automated validation

- exact schema and column order
- expected district set
- unique districts
- Altona-only borough values
- no missing values
- numeric type checks
- percentage ranges
- positive and non-negative domains
- population-density consistency within rounding tolerance

Automated validation can identify structural and plausibility problems. It cannot prove that every manually transferred source value is correct; that still requires source comparison.

## Update Procedure

A future source refresh should:

1. preserve the previous dataset or tag the previous repository state
2. record the new publication title, URL and access date
3. update reporting periods in column names where necessary
4. update `docs/data-lineage.csv`
5. run all tests and the complete analysis workflow
6. inspect changed rankings, correlations and figures
7. document material methodological changes

## Known Limitation

The current repository does not provide page-level source coordinates for every value. The lineage file documents the source indicator, reporting period, unit and transformation. Page or table references should be added during a future source refresh if a stable page mapping is confirmed.
