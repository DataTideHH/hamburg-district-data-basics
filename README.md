# Hamburg District Data Basics

Initial exploratory data analysis scaffold for public Hamburg district profile data.

## Purpose

This repository is the starting point for a small, reproducible Data/BI learning project based on public Hamburg district data.

The goal is to practice:

- dataset documentation
- data source tracking
- basic exploratory data analysis
- clean project structure
- Python-based analysis workflows
- later Power BI / dashboard preparation

## Current Status

This repository is an initial scaffold.

No raw source data is committed yet. The next step is to document the selected source dataset, extract a small structured table and build a first basic analysis.

## Planned Data Source

The planned starting point is the public Hamburg district profile publication by Statistikamt Nord:

- Hamburger Stadtteil-Profile
- Berichtsjahr 2024
- public district-level profile data for Hamburg

The original PDF source is documented in `docs/data-sources.md`.

## Repository Structure

```text
hamburg-district-data-basics/
├── data/
│   ├── README.md
│   └── raw/
│       └── .gitkeep
├── docs/
│   └── data-sources.md
├── notebooks/
│   └── README.md
├── src/
│   ├── README.md
│   └── check_environment.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
