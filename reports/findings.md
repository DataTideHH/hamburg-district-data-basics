# Findings: Altona District Profiles

This report summarizes the descriptive analysis of selected district-profile indicators for the 14 districts in the borough of Altona, Hamburg.

The canonical machine-readable results are generated in:

- `reports/generated/summary_metrics.json`
- `reports/generated/district_rankings.csv`
- `reports/generated/correlation_summary.csv`

## Scope

- Grain: one row per district / Stadtteil
- Districts: 14
- Source context: Hamburger Stadtteil-Profile 2024, Statistikamt Nord
- Analysis type: descriptive comparison

The indicators use different reporting periods. The report therefore does not treat the extract as a single-date snapshot.

## Dataset Summary

- Total population: **281,136**
- Total area: **77.8 km²**
- Aggregate population density: **3,614 residents per km²**

Aggregate population density is calculated as:

```text
total population / total area
```

It is not an unweighted average of the 14 district-density values and is not described as a population-weighted mean.

## Population

The largest district by population is **Lurup** with 37,755 residents. The smallest is **Nienstedten** with 7,062 residents.

Absolute population should be interpreted together with area and density. Districts of similar population can represent very different settlement structures.

## Population Density

The highest district-level population density is **Sternschanze** with 15,338 residents per km². The lowest is **Rissen** with 984 residents per km².

This is one of the clearest structural differences within Altona: compact inner-city districts and lower-density western districts represent different urban contexts.

## Income and Social Indicators

Average income per taxpayer refers to **2021**. Unemployment and SGB II shares refer to **December 2024**.

- Highest average income per taxpayer: **Nienstedten**, €168,404
- Lowest average income per taxpayer: **Lurup**, €35,445
- Highest unemployment share: **Lurup**, 8.5%
- Lowest unemployment share: **Nienstedten**, 2.4%
- Highest SGB II share: **Lurup**, 14.7%
- Lowest SGB II share: **Nienstedten**, 1.0%

Across the 14 districts, average income per taxpayer is negatively correlated with:

- SGB II share: **-0.86**
- unemployment share: **-0.91**

These Pearson correlations describe association in a small cross-sectional dataset. They do not establish causal direction and combine indicators from different reporting periods.

## Mobility Indicators

Private-car rates and electric-car counts refer to **January 2025**.

- Highest private cars per 1,000 residents: **Nienstedten**, 502
- Lowest private cars per 1,000 residents: **Sternschanze**, 186
- Highest absolute electric-car count: **Othmarschen**, 1,371

The private-car rate is suitable for district comparison. Absolute electric-car counts are influenced by district population and should not be interpreted as a penetration rate.

## Data Quality Result

The committed dataset passes the documented contract:

- expected schema and order
- 14 unique expected districts
- Altona-only borough scope
- no missing values
- numeric analytical fields
- valid percentage domains
- positive and non-negative value rules
- population-density consistency within rounding tolerance

These rules verify structural and domain plausibility. They do not independently certify every source value against the original PDF.

## BI Aggregation Notes

The following can be aggregated directly:

- population
- area
- electric-car counts

Aggregate population density can be derived from additive components:

```text
SUM(population) / SUM(area_km2)
```

The following district-level averages or rates must not be presented as an overall Altona value using a simple average unless explicitly labelled as an unweighted district statistic:

- average income per taxpayer
- unemployment share
- SGB II share
- private cars per 1,000 residents

Correct overall values would require the original numerators and denominators.

## Interpretation Limits

- The dataset covers only Altona.
- The number of observations is small.
- Indicators refer to different dates.
- The source extract is descriptive and cross-sectional.
- Several metrics have different denominator populations.
- The analysis does not control for demographic structure, housing, land use or transport access.
- Correlations are descriptive, not causal.

## Next Milestones

1. Implement the documented Power BI overview page locally.
2. Review all visual labels and DAX measures against the aggregation rules.
3. Add a public-safe screenshot and final measure documentation after the report is stable.
4. Expand geographic scope only after the Altona workflow remains validated and reproducible.
