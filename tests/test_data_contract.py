from __future__ import annotations

import unittest
from pathlib import Path

import pandas as pd

from src.data_contract import DatasetValidationError, validate_dataset

DATA_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "processed"
    / "altona_district_profiles_2024.csv"
)


class DatasetContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.df = pd.read_csv(DATA_PATH)

    def test_committed_dataset_satisfies_contract(self) -> None:
        validate_dataset(self.df)

    def test_duplicate_district_is_rejected(self) -> None:
        invalid = self.df.copy()
        invalid.loc[1, "district"] = invalid.loc[0, "district"]
        with self.assertRaisesRegex(DatasetValidationError, "duplicate districts"):
            validate_dataset(invalid)

    def test_invalid_percentage_is_rejected(self) -> None:
        invalid = self.df.copy()
        invalid.loc[0, "sgb2_share_percent_dec_2024"] = 101.0
        with self.assertRaisesRegex(DatasetValidationError, "between 0 and 100"):
            validate_dataset(invalid)

    def test_wrong_borough_is_rejected(self) -> None:
        invalid = self.df.copy()
        invalid.loc[0, "borough"] = "Eimsbüttel"
        with self.assertRaisesRegex(DatasetValidationError, "borough must contain"):
            validate_dataset(invalid)

    def test_density_inconsistency_is_rejected(self) -> None:
        invalid = self.df.copy()
        invalid.loc[0, "population_density"] += 10
        with self.assertRaisesRegex(
            DatasetValidationError, "population density differs"
        ):
            validate_dataset(invalid)

    def test_unexpected_column_is_rejected(self) -> None:
        invalid = self.df.assign(extra_column=1)
        with self.assertRaisesRegex(DatasetValidationError, "unexpected columns"):
            validate_dataset(invalid)


if __name__ == "__main__":
    unittest.main()
