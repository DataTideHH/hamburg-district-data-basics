from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "altona_district_profiles_2024.csv"
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"


def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)

    expected_columns = {
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
    }

    missing_columns = expected_columns - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing expected columns: {sorted(missing_columns)}")

    return df


def print_basic_checks(df: pd.DataFrame) -> None:
    print("Altona district profile sample")
    print("=" * 32)
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print()
    print("Missing values per column:")
    print(df.isna().sum())
    print()

    print("Top 5 districts by population:")
    print(df.sort_values("population", ascending=False)[["district", "population"]].head())
    print()

    print("Top 5 districts by population density:")
    print(df.sort_values("population_density", ascending=False)[["district", "population_density"]].head())
    print()

    print("Top 5 districts by private cars per 1,000 residents:")
    print(
        df.sort_values("private_cars_per_1000_jan_2025", ascending=False)[
            ["district", "private_cars_per_1000_jan_2025"]
        ].head()
    )
    print()


def save_bar_chart(
    df: pd.DataFrame,
    value_column: str,
    title: str,
    x_label: str,
    output_file: str,
    ascending: bool = True,
) -> None:
    sorted_df = df.sort_values(value_column, ascending=ascending)

    plt.figure(figsize=(10, 6))
    plt.barh(sorted_df["district"], sorted_df[value_column])
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel("District")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / output_file, dpi=160)
    plt.close()


def save_scatter_plot(df: pd.DataFrame) -> None:
    plt.figure(figsize=(8, 6))
    plt.scatter(
        df["avg_income_per_taxpayer_2021_eur"],
        df["sgb2_share_percent_dec_2024"],
    )

    for _, row in df.iterrows():
        plt.annotate(
            row["district"],
            (
                row["avg_income_per_taxpayer_2021_eur"],
                row["sgb2_share_percent_dec_2024"],
            ),
            fontsize=8,
            xytext=(4, 4),
            textcoords="offset points",
        )

    plt.title("Income vs. SGB II share in Altona districts")
    plt.xlabel("Average income per taxpayer, 2021, EUR")
    plt.ylabel("SGB II share, Dec 2024, %")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "income_vs_sgb2_share_altona_2024.png", dpi=160)
    plt.close()


def main() -> None:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    df = load_data()
    print_basic_checks(df)

    save_bar_chart(
        df,
        "population",
        "Population by district in Altona",
        "Population",
        "population_by_district_altona_2024.png",
    )

    save_bar_chart(
        df,
        "population_density",
        "Population density by district in Altona",
        "Residents per km²",
        "population_density_by_district_altona_2024.png",
    )

    save_bar_chart(
        df,
        "private_cars_per_1000_jan_2025",
        "Private cars per 1,000 residents in Altona districts",
        "Private cars per 1,000 residents",
        "private_cars_per_1000_altona_2024.png",
    )

    save_scatter_plot(df)

    print("Saved figures to:")
    for file in sorted(FIGURES_DIR.glob("*.png")):
        print(f"- {file.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
