# Notebooks

This folder contains notebook-based exploratory analysis for the Hamburg District Data Basics project.

## Current Notebook

Notebook file:

    01_altona_district_profiles_2024.ipynb

This notebook explores selected district profile indicators for the borough of Altona, Hamburg.

It complements the script-based workflow in:

    src/analyze_altona_profiles.py

## Purpose

The notebook is intended as a readable portfolio artifact. It documents:

- dataset loading
- basic data checks
- summary metrics
- ranking tables
- exploratory charts
- interpretation limits

## How to Run

From the repository root, activate the virtual environment:

    source .venv/bin/activate

Then start Jupyter:

    jupyter notebook notebooks/01_altona_district_profiles_2024.ipynb

Alternatively, open the notebook in DataSpell, PyCharm Professional or VS Code.

## Notes

The notebook uses the processed dataset from:

    data/processed/altona_district_profiles_2024.csv

The script-based version of the analysis remains in:

    src/analyze_altona_profiles.py
