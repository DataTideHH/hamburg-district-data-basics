"""Basic environment check for the Hamburg district data project."""

from __future__ import annotations

import sys

import matplotlib
import pandas as pd


def main() -> None:
    print("Hamburg District Data Basics")
    print("=" * 29)
    print(f"Python version: {sys.version.split()[0]}")
    print(f"pandas version: {pd.__version__}")
    print(f"matplotlib version: {matplotlib.__version__}")
    print()
    print("Environment check passed.")


if __name__ == "__main__":
    main()
