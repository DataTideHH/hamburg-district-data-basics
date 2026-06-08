# Power BI Dashboard Plan

This document outlines a planned Power BI dashboard version of the Hamburg District Data Basics project.

The dashboard is not implemented yet. This file documents the intended analytical structure, data model and report pages before building the actual Power BI report.

## Purpose

The goal is to turn the processed Altona district profile dataset into a small Power BI report that demonstrates basic Data/BI workflow skills:

- importing a documented CSV dataset
- creating a simple semantic model
- defining basic measures and KPIs
- building clear dashboard pages
- separating descriptive analysis from interpretation
- documenting report limitations

## Current Dataset

Planned source file:

    data/processed/altona_district_profiles_2024.csv

Supporting documentation:

    docs/data-sources.md
    docs/data-dictionary.md
    reports/findings.md
    notebooks/01_altona_district_profiles_2024.ipynb

Current geographic scope:

- borough: Altona, Hamburg
- level: Stadtteil / district
- number of districts: 14

## Planned Data Model

For the first Power BI version, a simple single-table model is sufficient.

Table:

    DistrictProfiles

Planned key column:

    district

Selected fields:

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

A more advanced version could later split the model into dimension and fact-like tables, but this is not necessary for the first portfolio version.

## Planned Measures

Possible DAX measures:

    Total Population
    Total Area km2
    Average Population Density
    Average Income per Taxpayer
    Average Unemployment Share
    Average SGB II Share
    Total Electric Cars
    Average Private Cars per 1,000 Residents

Possible ranking measures:

    Population Rank
    Density Rank
    Income Rank
    SGB II Share Rank

## Planned Report Pages

### 1. Overview

Purpose:

Give a compact overview of Altona's district structure.

Possible visuals:

- card: total population
- card: total area
- card: number of districts
- bar chart: population by district
- bar chart: population density by district
- table: district, population, area, density

### 2. Social Indicators

Purpose:

Compare income, unemployment and SGB II indicators across districts.

Possible visuals:

- bar chart: average income per taxpayer
- bar chart: unemployment share
- bar chart: SGB II share
- scatter plot: average income vs. SGB II share
- table with conditional formatting

Important note:

This page must be described as descriptive analysis only. It must not imply causal relationships.

### 3. Mobility Indicators

Purpose:

Show private car ownership and electric car counts across districts.

Possible visuals:

- bar chart: private cars per 1,000 residents
- bar chart: electric cars
- scatter plot: population density vs. private cars per 1,000 residents
- table: district, density, private cars per 1,000 residents, electric cars

### 4. Interpretation and Limitations

Purpose:

Document the limits of the dataset directly inside the report.

Possible content:

- scope: Altona only
- small number of observations
- different reporting dates for indicators
- descriptive analysis only
- no causal modelling
- no full Hamburg-wide comparison yet

## Planned Dashboard Questions

The first dashboard should help answer simple descriptive questions:

- Which Altona districts have the highest and lowest population?
- Which districts have the highest population density?
- How do income, unemployment and SGB II shares differ across districts?
- Which districts have high or low private car ownership?
- Where are electric cars most common in absolute numbers?
- Which indicators require careful interpretation because of different reporting dates?

## Design Principles

The first report should stay simple:

- no unnecessary visuals
- clear page titles
- consistent number formats
- no overloaded color palette
- visible source and limitation notes
- focus on readability over visual effects

## File Handling Plan

A later Power BI version may use this folder structure:

    reports/power-bi/

Possible future files:

    reports/power-bi/screenshots/
    reports/power-bi/dashboard-notes.md

The actual Power BI file may be kept outside the repository if file size or binary versioning becomes inconvenient. In that case, the repository should document the report using screenshots and notes instead of relying on a binary .pbix file.

## Current Status

Status:

    Planned

The Python analysis, findings report, data dictionary and notebook are already present. The next step is to build a first Power BI report based on the processed CSV dataset.
