# Data Directory

## Processed Data

The committed analysis dataset is:

```text
processed/altona_district_profiles_2024.csv
```

It contains one row per Altona district and is validated by `src/data_contract.py`.

## Raw Data

The complete source PDF is not committed. `raw/` remains reserved for local source material and is ignored by Git except for `.gitkeep`.

Source, extraction and lineage documentation:

- `../docs/data-sources.md`
- `../docs/extraction-method.md`
- `../docs/data-lineage.csv`

The repository's MIT License applies to original code and documentation. Underlying official statistics remain subject to the publisher's applicable terms.
