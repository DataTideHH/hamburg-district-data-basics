# Power BI Dashboard Plan

## Status

This document defines the intended semantic model and report logic before a local Power BI implementation is presented publicly. No completed `.pbix` file is claimed.

## Purpose

The first report should demonstrate:

- importing a documented and validated CSV
- preserving district-level grain
- defining measures with correct aggregation semantics
- comparing districts without inventing borough-wide values
- displaying source dates and limitations inside the report
- connecting analytical findings with a clear business-facing page

## Source and Grain

| Item | Value |
|---|---|
| Source table | `DistrictProfiles` |
| Source file | `data/processed/altona_district_profiles_2024.csv` |
| Grain | One row per district / Stadtteil |
| Current row count | 14 |
| Natural key | `district` within the fixed Altona scope |

A single-table model is appropriate for the first version. A star schema would add complexity without analytical benefit at the current grain and size.

## Aggregation Classes

### Additive columns

These can be summed across districts:

- `population`
- `area_km2`
- `general_practitioners_jan_2025`
- `pharmacies_dec_2024`
- `electric_cars_jan_2025`

Counts may still require population context for interpretation, but their arithmetic aggregation is valid.

### Derived measure from additive components

Overall population density must be calculated from totals:

```DAX
Total Population =
SUM(DistrictProfiles[population])
```

```DAX
Total Area km2 =
SUM(DistrictProfiles[area_km2])
```

```DAX
Aggregate Population Density =
DIVIDE([Total Population], [Total Area km2])
```

It must not use `AVERAGE(DistrictProfiles[population_density])`.

### District-level rates and averages

The following columns are suitable for district comparisons but not for an overall Altona KPI using a simple average:

- `under_18_percent`
- `over_64_percent`
- `unemployment_share_percent_dec_2024`
- `sgb2_share_percent_dec_2024`
- `avg_income_per_taxpayer_2021_eur`
- `private_cars_per_1000_jan_2025`

Correct borough-wide values would require their original numerators and denominators. Until those are available, the report should use:

- district-level bars, tables and scatterplots
- selected-district values
- explicitly labelled unweighted district medians where useful

## Measures

### Safe aggregate measures

```DAX
District Count =
DISTINCTCOUNT(DistrictProfiles[district])
```

```DAX
Total Population =
SUM(DistrictProfiles[population])
```

```DAX
Total Area km2 =
SUM(DistrictProfiles[area_km2])
```

```DAX
Aggregate Population Density =
DIVIDE([Total Population], [Total Area km2])
```

```DAX
Total Electric Cars Jan 2025 =
SUM(DistrictProfiles[electric_cars_jan_2025])
```

### Selected-district measures

These return a value only when one district is selected:

```DAX
Selected District Income 2021 =
SELECTEDVALUE(DistrictProfiles[avg_income_per_taxpayer_2021_eur])
```

```DAX
Selected District Unemployment Share Dec 2024 =
SELECTEDVALUE(DistrictProfiles[unemployment_share_percent_dec_2024])
```

```DAX
Selected District SGB II Share Dec 2024 =
SELECTEDVALUE(DistrictProfiles[sgb2_share_percent_dec_2024])
```

```DAX
Selected District Private Cars per 1000 Jan 2025 =
SELECTEDVALUE(DistrictProfiles[private_cars_per_1000_jan_2025])
```

### Explicit district-distribution measures

Where a summary of the 14 districts is useful, use an explicitly named median rather than implying an overall population statistic:

```DAX
Median District Unemployment Share Dec 2024 =
MEDIAN(DistrictProfiles[unemployment_share_percent_dec_2024])
```

```DAX
Median District SGB II Share Dec 2024 =
MEDIAN(DistrictProfiles[sgb2_share_percent_dec_2024])
```

```DAX
Median District Income per Taxpayer 2021 =
MEDIAN(DistrictProfiles[avg_income_per_taxpayer_2021_eur])
```

These are unweighted district medians, not borough-wide rates or averages.

## First Report Page

The initial implementation should use one page:

- [`reports/power-bi/altona-overview-page.md`](../reports/power-bi/altona-overview-page.md)

The page combines additive overview measures with district comparisons while keeping source dates visible.

## Visual and Interaction Principles

- use a district slicer only where it adds analytical value
- keep the page readable at standard laptop resolution
- show units and reporting periods in titles
- avoid red/green semantics unless a real threshold is defined
- do not label descriptive correlations as drivers or causes
- retain source and limitation notes on the page
- avoid decorative gauges and duplicated KPIs

## File Handling

A stable local report may later be documented under:

```text
reports/power-bi/
├── altona-overview-page.md
├── measures.md
└── screenshots/
    └── altona-overview.png
```

A `.pbix` file can remain outside version control if binary size or reviewability becomes inconvenient. A public screenshot and documented measures should be added only after the report is stable and reviewed for source, aggregation and privacy issues.
