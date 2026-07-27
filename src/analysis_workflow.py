"""Reusable analysis and artifact-generation functions."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from src.data_contract import validate_dataset

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "altona_district_profiles_2024.csv"
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"
GENERATED_DIR = PROJECT_ROOT / "reports" / "generated"

RANKING_DEFINITIONS = (
    ("population", "population", "persons", "2024"),
    ("population_density", "population_density", "residents_per_km2", "2024"),
    (
        "average_income_per_taxpayer",
        "avg_income_per_taxpayer_2021_eur",
        "EUR",
        "2021",
    ),
    (
        "unemployment_share",
        "unemployment_share_percent_dec_2024",
        "percent",
        "2024-12",
    ),
    ("sgb2_share", "sgb2_share_percent_dec_2024", "percent", "2024-12"),
    (
        "private_cars_per_1000",
        "private_cars_per_1000_jan_2025",
        "cars_per_1000",
        "2025-01",
    ),
    ("electric_cars", "electric_cars_jan_2025", "cars", "2025-01"),
)


def load_dataset(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the processed CSV and enforce the documented dataset contract."""

    df = pd.read_csv(path)
    validate_dataset(df)
    return df


def _extreme_record(
    df: pd.DataFrame, column: str, *, highest: bool
) -> dict[str, Any]:
    index = df[column].idxmax() if highest else df[column].idxmin()
    return {
        "district": str(df.loc[index, "district"]),
        "value": float(df.loc[index, column]),
    }


def calculate_summary_metrics(df: pd.DataFrame) -> dict[str, Any]:
    """Calculate the portfolio's canonical summary metrics once."""

    total_population = int(df["population"].sum())
    total_area_km2 = round(float(df["area_km2"].sum()), 1)
    aggregate_population_density = round(total_population / total_area_km2)

    return {
        "district_count": int(len(df)),
        "total_population": total_population,
        "total_area_km2": total_area_km2,
        "aggregate_population_density_per_km2": aggregate_population_density,
        "population": {
            "highest": _extreme_record(df, "population", highest=True),
            "lowest": _extreme_record(df, "population", highest=False),
        },
        "population_density": {
            "highest": _extreme_record(df, "population_density", highest=True),
            "lowest": _extreme_record(df, "population_density", highest=False),
        },
        "average_income_per_taxpayer_2021_eur": {
            "highest": _extreme_record(
                df, "avg_income_per_taxpayer_2021_eur", highest=True
            ),
            "lowest": _extreme_record(
                df, "avg_income_per_taxpayer_2021_eur", highest=False
            ),
        },
        "unemployment_share_percent_dec_2024": {
            "highest": _extreme_record(
                df, "unemployment_share_percent_dec_2024", highest=True
            ),
            "lowest": _extreme_record(
                df, "unemployment_share_percent_dec_2024", highest=False
            ),
        },
        "sgb2_share_percent_dec_2024": {
            "highest": _extreme_record(
                df, "sgb2_share_percent_dec_2024", highest=True
            ),
            "lowest": _extreme_record(
                df, "sgb2_share_percent_dec_2024", highest=False
            ),
        },
        "private_cars_per_1000_jan_2025": {
            "highest": _extreme_record(
                df, "private_cars_per_1000_jan_2025", highest=True
            ),
            "lowest": _extreme_record(
                df, "private_cars_per_1000_jan_2025", highest=False
            ),
        },
        "electric_cars_jan_2025": {
            "highest": _extreme_record(df, "electric_cars_jan_2025", highest=True),
            "lowest": _extreme_record(df, "electric_cars_jan_2025", highest=False),
        },
    }


def build_rankings(df: pd.DataFrame) -> pd.DataFrame:
    """Create a long-format ranking table for reusable reporting."""

    frames: list[pd.DataFrame] = []
    for metric, column, unit, reporting_period in RANKING_DEFINITIONS:
        ranking = (
            df[["district", column]]
            .sort_values(column, ascending=False)
            .reset_index(drop=True)
            .rename(columns={column: "value"})
        )
        ranking.insert(0, "rank", range(1, len(ranking) + 1))
        ranking.insert(0, "metric", metric)
        ranking["unit"] = unit
        ranking["reporting_period"] = reporting_period
        frames.append(ranking)

    return pd.concat(frames, ignore_index=True)


def calculate_correlations(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate explicitly labelled descriptive Pearson correlations."""

    relationships = (
        (
            "income_vs_sgb2_share",
            "avg_income_per_taxpayer_2021_eur",
            "sgb2_share_percent_dec_2024",
        ),
        (
            "income_vs_unemployment_share",
            "avg_income_per_taxpayer_2021_eur",
            "unemployment_share_percent_dec_2024",
        ),
    )

    rows = []
    for relationship, x_column, y_column in relationships:
        rows.append(
            {
                "relationship": relationship,
                "x_column": x_column,
                "y_column": y_column,
                "pearson_correlation": round(
                    float(df[x_column].corr(df[y_column])), 2
                ),
                "observations": int(df[[x_column, y_column]].dropna().shape[0]),
                "interpretation": "descriptive association; not causal",
            }
        )
    return pd.DataFrame(rows)


def write_generated_outputs(
    df: pd.DataFrame, output_dir: Path = GENERATED_DIR
) -> tuple[Path, Path, Path]:
    """Write deterministic machine-readable metrics and rankings."""

    output_dir.mkdir(parents=True, exist_ok=True)
    summary_path = output_dir / "summary_metrics.json"
    rankings_path = output_dir / "district_rankings.csv"
    correlations_path = output_dir / "correlation_summary.csv"

    summary_path.write_text(
        json.dumps(calculate_summary_metrics(df), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    build_rankings(df).to_csv(rankings_path, index=False)
    calculate_correlations(df).to_csv(correlations_path, index=False)
    return summary_path, rankings_path, correlations_path


def save_bar_chart(
    df: pd.DataFrame,
    value_column: str,
    title: str,
    x_label: str,
    output_file: str,
    *,
    ascending: bool = True,
    output_dir: Path = FIGURES_DIR,
) -> Path:
    """Create one consistently formatted horizontal ranking chart."""

    output_dir.mkdir(parents=True, exist_ok=True)
    sorted_df = df.sort_values(value_column, ascending=ascending)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(sorted_df["district"], sorted_df[value_column])
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel("District")
    fig.tight_layout()

    path = output_dir / output_file
    fig.savefig(path, dpi=160)
    plt.close(fig)
    return path


def save_scatter_plot(
    df: pd.DataFrame, output_dir: Path = FIGURES_DIR
) -> Path:
    """Plot income (2021) against SGB II share (December 2024)."""

    output_dir.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(
        df["avg_income_per_taxpayer_2021_eur"],
        df["sgb2_share_percent_dec_2024"],
    )

    for _, row in df.iterrows():
        ax.annotate(
            row["district"],
            (
                row["avg_income_per_taxpayer_2021_eur"],
                row["sgb2_share_percent_dec_2024"],
            ),
            fontsize=8,
            xytext=(4, 4),
            textcoords="offset points",
        )

    ax.set_title("Average income (2021) vs. SGB II share (Dec 2024)")
    ax.set_xlabel("Average income per taxpayer, 2021, EUR")
    ax.set_ylabel("SGB II share, December 2024, %")
    fig.tight_layout()

    path = output_dir / "income_2021_vs_sgb2_share_dec_2024.png"
    fig.savefig(path, dpi=160)
    plt.close(fig)
    return path


def write_figures(df: pd.DataFrame, output_dir: Path = FIGURES_DIR) -> list[Path]:
    """Generate the complete documented figure set."""

    return [
        save_bar_chart(
            df,
            "population",
            "Population by district in Altona (2024 profile)",
            "Population",
            "population_by_district_altona_2024.png",
            output_dir=output_dir,
        ),
        save_bar_chart(
            df,
            "population_density",
            "Population density by district in Altona (2024 profile)",
            "Residents per km²",
            "population_density_by_district_altona_2024.png",
            output_dir=output_dir,
        ),
        save_bar_chart(
            df,
            "private_cars_per_1000_jan_2025",
            "Private cars per 1,000 residents (January 2025)",
            "Private cars per 1,000 residents",
            "private_cars_per_1000_altona_jan_2025.png",
            output_dir=output_dir,
        ),
        save_scatter_plot(df, output_dir=output_dir),
    ]
