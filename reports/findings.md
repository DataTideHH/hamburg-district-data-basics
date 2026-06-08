# Findings: Altona District Profiles 2024

This report summarizes the first descriptive analysis of selected district profile indicators for the borough of Altona, Hamburg.

## Scope

The analysis covers 14 districts in the borough of Altona.

The processed dataset is:

    data/processed/altona_district_profiles_2024.csv

The analysis is descriptive. It compares selected indicators across districts and does not make causal claims.

## Dataset Summary

- Number of districts: 14
- Total population in the processed dataset: 281,136
- Total area in the processed dataset: 77.8 km²
- Population-weighted average density: 3,614 residents per km²

## Population

The largest district by population is **Lurup** with 37,755 residents.

The smallest district by population is **Nienstedten** with 7,062 residents.

This shows that district size within the same borough varies considerably. For reporting and dashboard work, absolute values should therefore be interpreted alongside ratios such as population density or shares.

## Population Density

The highest population density is found in **Sternschanze** with 15,338 residents per km².

The lowest population density is found in **Rissen** with 984 residents per km².

This is one of the clearest structural differences inside Altona: compact inner-city districts and lower-density western districts represent very different urban contexts.

## Income and Social Indicators

The highest average income per taxpayer is shown for **Nienstedten** with 168,404 EUR.

The lowest average income per taxpayer is shown for **Lurup** with 35,445 EUR.

The highest unemployment share is shown for **Lurup** with 8.5 percent.

The lowest unemployment share is shown for **Nienstedten** with 2.4 percent.

The highest SGB II share is shown for **Lurup** with 14.7 percent.

The lowest SGB II share is shown for **Nienstedten** with 1.0 percent.

In this small dataset, average income is negatively correlated with SGB II share (-0.86) and with unemployment share (-0.91). This is a descriptive relationship only and should not be interpreted as causal.

## Mobility Indicators

The highest number of private cars per 1,000 residents is shown for **Nienstedten** with 502 cars per 1,000 residents.

The lowest number of private cars per 1,000 residents is shown for **Sternschanze** with 186 cars per 1,000 residents.

The highest absolute number of electric cars is shown for **Othmarschen** with 1,371 electric cars.

These mobility indicators should be interpreted carefully. District density, household structure, income levels, public transport access and land-use patterns may all influence car ownership.

## Generated Figures

The current analysis includes the following generated charts:

- reports/figures/population_by_district_altona_2024.png
- reports/figures/population_density_by_district_altona_2024.png
- reports/figures/income_vs_sgb2_share_altona_2024.png
- reports/figures/private_cars_per_1000_altona_2024.png

## Interpretation Limits

This analysis is a first descriptive portfolio workflow.

Important limitations:

- The dataset covers only one Hamburg borough.
- The number of observations is small.
- Indicators refer to different reporting dates.
- Some indicators are absolute counts, while others are rates or ratios.
- The analysis does not control for demographic structure, housing, land use or transport access.
- Correlations in this dataset are descriptive and not causal.

## Next Steps

Useful next improvements:

1. Add a data dictionary with original German indicator names.
2. Add exact official source URL and access date.
3. Extend the dataset to all Hamburg boroughs.
4. Add population density and social indicator comparison charts.
5. Prepare a Power BI version with a simple star-schema-style model.
