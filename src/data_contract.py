"""Dataset contract and validation rules for the Altona district extract."""

from __future__ import annotations

from collections.abc import Iterable

import pandas as pd

EXPECTED_COLUMNS = (
    "district",
    "borough",
    "population",
    "area_km2",
    "population_density",
    "under_18_percent",
    "over_64_percent",
    "unemployment_share_percent_dec_2024",
    "sgb2_share_percent_dec_2024",
    "avg_income_per_taxpayer_2021_eur",
    "general_practitioners_jan_2025",
    "pharmacies_dec_2024",
    "private_cars_per_1000_jan_2025",
    "electric_cars_jan_2025",
)

EXPECTED_DISTRICTS = frozenset(
    {
        "Altona-Altstadt",
        "Sternschanze",
        "Altona-Nord",
        "Ottensen",
        "Bahrenfeld",
        "Groß Flottbek",
        "Othmarschen",
        "Lurup",
        "Osdorf",
        "Nienstedten",
        "Blankenese",
        "Iserbrook",
        "Sülldorf",
        "Rissen",
    }
)

NUMERIC_COLUMNS = EXPECTED_COLUMNS[2:]
PERCENT_COLUMNS = (
    "under_18_percent",
    "over_64_percent",
    "unemployment_share_percent_dec_2024",
    "sgb2_share_percent_dec_2024",
)
POSITIVE_COLUMNS = (
    "population",
    "area_km2",
    "population_density",
    "avg_income_per_taxpayer_2021_eur",
)
NON_NEGATIVE_COLUMNS = (
    "general_practitioners_jan_2025",
    "pharmacies_dec_2024",
    "private_cars_per_1000_jan_2025",
    "electric_cars_jan_2025",
)


class DatasetValidationError(ValueError):
    """Raised when the processed dataset violates the documented contract."""


def _format_values(values: Iterable[object]) -> str:
    return ", ".join(str(value) for value in sorted(values, key=str))


def _invalid_row_labels(df: pd.DataFrame, mask: pd.Series) -> list[str]:
    """Return district names when available, otherwise stable row labels."""

    if "district" in df.columns:
        return (
            df.loc[mask, "district"]
            .fillna("<missing district>")
            .astype(str)
            .tolist()
        )
    return [f"row {index}" for index in df.index[mask].tolist()]


def validate_dataset(df: pd.DataFrame, *, density_tolerance: float = 1.0) -> None:
    """Validate schema, domain rules and basic cross-field consistency.

    All detected problems are collected and returned in one exception so that a
    reviewer can see the complete validation result instead of fixing errors one
    at a time.
    """

    errors: list[str] = []

    actual_columns = tuple(df.columns)
    if actual_columns != EXPECTED_COLUMNS:
        missing = set(EXPECTED_COLUMNS) - set(actual_columns)
        unexpected = set(actual_columns) - set(EXPECTED_COLUMNS)
        if missing:
            errors.append(f"missing columns: {_format_values(missing)}")
        if unexpected:
            errors.append(f"unexpected columns: {_format_values(unexpected)}")
        if not missing and not unexpected:
            errors.append("columns are not in the documented order")

    if len(df) != len(EXPECTED_DISTRICTS):
        errors.append(f"expected {len(EXPECTED_DISTRICTS)} rows, found {len(df)}")

    if "district" in df.columns:
        duplicates = df.loc[df["district"].duplicated(), "district"].tolist()
        if duplicates:
            errors.append(f"duplicate districts: {_format_values(duplicates)}")

        actual_districts = set(df["district"].dropna())
        missing_districts = EXPECTED_DISTRICTS - actual_districts
        unexpected_districts = actual_districts - EXPECTED_DISTRICTS
        if missing_districts:
            errors.append(
                f"missing expected districts: {_format_values(missing_districts)}"
            )
        if unexpected_districts:
            errors.append(
                f"unexpected districts: {_format_values(unexpected_districts)}"
            )

    if "borough" in df.columns:
        borough_values = set(df["borough"].dropna())
        if borough_values != {"Altona"}:
            errors.append(
                "borough must contain only 'Altona'; found: "
                f"{_format_values(borough_values)}"
            )

    missing_counts = df.isna().sum()
    columns_with_missing = missing_counts[missing_counts > 0]
    if not columns_with_missing.empty:
        details = ", ".join(
            f"{column}={int(count)}"
            for column, count in columns_with_missing.items()
        )
        errors.append(f"missing values detected: {details}")

    for column in NUMERIC_COLUMNS:
        if column in df.columns and not pd.api.types.is_numeric_dtype(df[column]):
            errors.append(f"column '{column}' must be numeric")

    for column in PERCENT_COLUMNS:
        if column in df.columns and pd.api.types.is_numeric_dtype(df[column]):
            invalid = _invalid_row_labels(df, ~df[column].between(0, 100))
            if invalid:
                errors.append(
                    f"column '{column}' must be between 0 and 100; invalid districts: "
                    f"{_format_values(invalid)}"
                )

    for column in POSITIVE_COLUMNS:
        if column in df.columns and pd.api.types.is_numeric_dtype(df[column]):
            invalid = _invalid_row_labels(df, df[column] <= 0)
            if invalid:
                errors.append(
                    f"column '{column}' must be greater than zero; invalid districts: "
                    f"{_format_values(invalid)}"
                )

    for column in NON_NEGATIVE_COLUMNS:
        if column in df.columns and pd.api.types.is_numeric_dtype(df[column]):
            invalid = _invalid_row_labels(df, df[column] < 0)
            if invalid:
                errors.append(
                    f"column '{column}' must not be negative; invalid districts: "
                    f"{_format_values(invalid)}"
                )

    density_columns = {"population", "area_km2", "population_density"}
    if density_columns.issubset(df.columns):
        calculated_density = df["population"] / df["area_km2"]
        density_difference = (calculated_density - df["population_density"]).abs()
        invalid = _invalid_row_labels(df, density_difference > density_tolerance)
        if invalid:
            errors.append(
                "population density differs from population / area by more than "
                f"{density_tolerance}; invalid districts: {_format_values(invalid)}"
            )

    if errors:
        raise DatasetValidationError(
            "Dataset validation failed:\n- " + "\n- ".join(errors)
        )
