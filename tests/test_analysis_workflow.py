from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from src.analysis_workflow import (
    build_rankings,
    calculate_correlations,
    calculate_summary_metrics,
    load_dataset,
    write_generated_outputs,
)


class AnalysisWorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.df = load_dataset()

    def test_summary_metrics_match_documented_results(self) -> None:
        summary = calculate_summary_metrics(self.df)
        self.assertEqual(summary["district_count"], 14)
        self.assertEqual(summary["total_population"], 281_136)
        self.assertEqual(summary["total_area_km2"], 77.8)
        self.assertEqual(summary["aggregate_population_density_per_km2"], 3_614)
        self.assertEqual(summary["population"]["highest"]["district"], "Lurup")
        self.assertEqual(
            summary["population_density"]["highest"]["district"],
            "Sternschanze",
        )

    def test_rankings_have_one_row_per_metric_and_district(self) -> None:
        rankings = build_rankings(self.df)
        self.assertEqual(len(rankings), 7 * 14)
        population = rankings[rankings["metric"] == "population"]
        self.assertEqual(population.iloc[0]["district"], "Lurup")
        self.assertEqual(int(population.iloc[0]["rank"]), 1)

    def test_correlations_are_explicitly_descriptive(self) -> None:
        correlations = calculate_correlations(self.df)
        values = dict(
            zip(
                correlations["relationship"],
                correlations["pearson_correlation"],
                strict=True,
            )
        )
        self.assertEqual(values["income_vs_sgb2_share"], -0.86)
        self.assertEqual(values["income_vs_unemployment_share"], -0.91)
        self.assertTrue(
            correlations["interpretation"].str.contains("not causal").all()
        )

    def test_generated_outputs_are_written(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            paths = write_generated_outputs(self.df, Path(temp_dir))
            self.assertTrue(all(path.exists() for path in paths))
            summary = json.loads(paths[0].read_text(encoding="utf-8"))
            self.assertEqual(summary["total_population"], 281_136)


if __name__ == "__main__":
    unittest.main()
