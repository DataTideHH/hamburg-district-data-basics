"""Validate the minimum runtime used by the project."""

from __future__ import annotations

import sys

import matplotlib
import pandas as pd

MINIMUM_PYTHON = (3, 12)


def main() -> None:
    print("Hamburg District Data Basics")
    print("=" * 29)
    print(f"Python version: {sys.version.split()[0]}")
    print(f"pandas version: {pd.__version__}")
    print(f"matplotlib version: {matplotlib.__version__}")

    if sys.version_info < MINIMUM_PYTHON:
        required = ".".join(str(part) for part in MINIMUM_PYTHON)
        raise RuntimeError(f"Python {required} or newer is required")

    print("Environment check passed.")


if __name__ == "__main__":
    main()
