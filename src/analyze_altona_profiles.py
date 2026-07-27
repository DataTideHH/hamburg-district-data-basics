"""Run validation, analysis, artifact generation and chart creation."""

from __future__ import annotations

from src.analysis_workflow import (
    calculate_correlations,
    calculate_summary_metrics,
    load_dataset,
    write_figures,
    write_generated_outputs,
)


def main() -> None:
    df = load_dataset()
    summary = calculate_summary_metrics(df)
    correlations = calculate_correlations(df)
    generated_paths = write_generated_outputs(df)
    figure_paths = write_figures(df)

    print("Hamburg District Data Basics")
    print("=" * 29)
    print("Dataset validation: passed")
    print(f"Districts: {summary['district_count']}")
    print(f"Total population: {summary['total_population']:,}")
    print(f"Total area: {summary['total_area_km2']:.1f} km²")
    print(
        "Aggregate population density: "
        f"{summary['aggregate_population_density_per_km2']:,} residents/km²"
    )
    print()
    print("Descriptive Pearson correlations:")
    for row in correlations.itertuples(index=False):
        print(
            f"- {row.relationship}: {row.pearson_correlation:.2f} "
            f"(n={row.observations})"
        )
    print()
    print("Generated data artifacts:")
    for path in generated_paths:
        print(f"- {path}")
    print("Generated figures:")
    for path in figure_paths:
        print(f"- {path}")


if __name__ == "__main__":
    main()
