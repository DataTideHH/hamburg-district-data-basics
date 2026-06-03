# First Findings: Altona District Profiles 2024

This first analysis uses a small, focused extract from the official Hamburg District Profiles 2024.

Source: Statistikamt Nord / Hamburger Stadtteil-Profile, Berichtsjahr 2024  
Scope: Districts within the borough of Altona  
Unit of analysis: Hamburg district / Stadtteil

## Dataset

The processed dataset contains 14 districts in the borough of Altona:

- Altona-Altstadt
- Sternschanze
- Altona-Nord
- Ottensen
- Bahrenfeld
- Groß Flottbek
- Othmarschen
- Lurup
- Osdorf
- Nienstedten
- Blankenese
- Iserbrook
- Sülldorf
- Rissen

The selected indicators cover population, area, population density, age structure, unemployment, SGB II share, average income, basic health infrastructure, private car density and electric cars.

## Initial Observations

### 1. Population is concentrated in a few large districts

The largest districts in this sample are:

- Lurup: 37,755 residents
- Ottensen: 35,925 residents
- Bahrenfeld: 31,051 residents
- Altona-Altstadt: 29,680 residents
- Altona-Nord: 26,777 residents

This already shows that Altona is not one homogeneous urban area. It contains dense inner-city districts, residential western districts and large population centres such as Lurup.

### 2. Population density clearly separates inner-city districts from western districts

The highest population densities are found in:

- Sternschanze: 15,338 residents per km²
- Ottensen: 12,830 residents per km²
- Altona-Nord: 12,171 residents per km²
- Altona-Altstadt: 10,993 residents per km²

By contrast, western districts such as Rissen, Nienstedten and Blankenese have much lower population densities.

### 3. Car density is much higher in the western districts

The highest numbers of private cars per 1,000 residents are found in:

- Nienstedten: 502
- Blankenese: 489
- Rissen: 425
- Othmarschen: 415
- Groß Flottbek: 414

The lowest values appear in the dense inner-city districts such as Sternschanze, Altona-Nord and Altona-Altstadt.

### 4. Social indicators differ strongly across the borough

The highest SGB II shares in this sample are found in:

- Lurup: 14.7 %
- Bahrenfeld: 12.1 %
- Altona-Altstadt: 11.4 %
- Osdorf: 11.2 %
- Altona-Nord: 9.6 %

The lowest values are found in Nienstedten, Groß Flottbek, Blankenese and Othmarschen.

### 5. Income and SGB II share show a visible contrast

The highest average incomes per taxpayer are found in:

- Nienstedten
- Blankenese
- Groß Flottbek
- Othmarschen

These districts also show comparatively low SGB II shares. This is a useful starting point for a later Power BI dashboard because the contrast can be explained with simple KPI cards, rankings and scatter plots.

## Generated Figures

The script `src/analyze_altona_profiles.py` creates the following figures:

- `reports/figures/population_by_district_altona_2024.png`
- `reports/figures/population_density_by_district_altona_2024.png`
- `reports/figures/private_cars_per_1000_altona_2024.png`
- `reports/figures/income_vs_sgb2_share_altona_2024.png`

## Next Steps

- Add a short data source note in `docs/data-sources.md`.
- Extend the analysis with Power BI-ready notes.
- Build a small Power BI dashboard with district slicers, KPI cards and rankings.
- Add a short methodological note explaining that this is a focused Altona extract, not a full Hamburg-wide analysis.
