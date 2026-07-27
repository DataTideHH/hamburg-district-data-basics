# Power BI Page Specification: Altona District Overview

## Status

**Documented design; local Power BI implementation and screenshot remain the next report milestone.**

## Audience

- recruiter or hiring manager reviewing Data/BI fundamentals
- operational or administrative stakeholder seeking a compact district comparison
- technical reviewer checking measure semantics and source transparency

## Page Question

> How do population structure, density and selected social indicators differ across Altona's 14 districts, and which values can be interpreted at district or borough level?

## Page Wireframe

```text
+-----------------------------------------------------------------------+
| Altona District Overview                         [District slicer]     |
| Source: Statistikamt Nord | mixed reporting periods | descriptive only|
+----------------+----------------+----------------+---------------------+
| District Count | Total Pop.     | Total Area     | Aggregate Density   |
| 14             | 281,136        | 77.8 km²       | 3,614 per km²       |
+----------------+----------------+----------------+---------------------+
| Population by District        | Population Density by District        |
| horizontal bar chart          | horizontal bar chart                  |
+-------------------------------+---------------------------------------+
| Income 2021 vs SGB II Dec 2024 scatterplot                            |
| labels: district | tooltip: unemployment, population, density         |
+-----------------------------------------------------------------------+
| Selected district detail table | reporting-period and limitation note |
+-----------------------------------------------------------------------+
```

## KPI Cards

| Card | Measure | Reason |
|---|---|---|
| District Count | `DISTINCTCOUNT(district)` | Valid distinct count at current grain |
| Total Population | `SUM(population)` | Additive count |
| Total Area | `SUM(area_km2)` | Additive area |
| Aggregate Population Density | `Total Population / Total Area` | Correctly derived from additive components |

Do not add cards for average income, unemployment share, SGB II share or private cars per 1,000 as borough-wide values. The source extract lacks the denominators needed for correct aggregation.

## Visuals

### Population by District

- visual: horizontal bar chart
- axis: `district`
- value: `population`
- sort: descending
- title: `Population by District — 2024 Profile`

### Population Density by District

- visual: horizontal bar chart
- axis: `district`
- value: `population_density`
- sort: descending
- title: `Population Density by District — 2024 Profile`

This visual compares published district densities. The card above uses the aggregate density measure derived from totals.

### Income vs. SGB II Share

- visual: scatterplot
- x-axis: `avg_income_per_taxpayer_2021_eur`
- y-axis: `sgb2_share_percent_dec_2024`
- details: `district`
- size: optional `population`
- title: `Average Income 2021 vs. SGB II Share Dec 2024`

Required subtitle or footnote:

> Descriptive district-level association across 14 observations; different reporting periods; not causal.

### Selected District Detail

A small table may show:

- district
- population
- area
- population density
- average income per taxpayer 2021
- unemployment share December 2024
- SGB II share December 2024
- private cars per 1,000 January 2025

Use full reporting dates in headers or tooltips.

## Interaction Rules

- selecting a district filters the detail table and highlights chart marks
- KPI totals remain page-context totals unless the intended behaviour is made explicit
- selected-district rate cards may appear only when exactly one district is selected
- no cross-highlighting should hide the source and limitation note

## Formatting

- population: whole numbers with thousands separator
- area: one decimal place and `km²`
- density: whole number and `residents/km²`
- currency: whole EUR with thousands separator
- percentage values: one decimal place and `%`
- use a restrained, accessible palette
- use the same district ordering where comparison across visuals benefits from consistency

## Visible Data Caveat

The page should contain this concise note:

> Indicators use different reporting periods. District-level averages and rates are shown for comparison and are not aggregated into borough-wide values without their original denominators. Correlations are descriptive, not causal.

## Acceptance Criteria

The page is ready for a public screenshot when:

- all four KPI measures match the generated summary metrics
- visual titles contain the correct reporting periods
- district labels are readable
- no simple average is used for district-level rates or averages
- source and limitation notes remain visible
- the report contains no private or manually entered values outside the documented dataset
