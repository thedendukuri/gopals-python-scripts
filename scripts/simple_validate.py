#!/usr/bin/env python3
"""
Minimal CSV inspection script for the repo starter.

Usage:
    python scripts/simple_validate.py path/to/file.csv

This script does a lightweight check (load with pandas, report shape and missing values)
and exits with code 0 on success or 2 on load error.
"""
import sys
import argparse
import pandas as pd

def inspect_csv(path, sep=","):
    df = pd.read_csv(path, sep=sep)
    print(f"Loaded: {path}")
    print(f"Rows: {len(df)}, Columns: {len(df.columns)}")
    print("Missing values per column:")
    print(df.isna().sum())
    return df

def main(argv=None):
    parser = argparse.ArgumentParser(description="Quick CSV inspection")
    parser.add_argument("csv", help="Path to CSV file")
    parser.add_argument("--sep", default="", help="CSV separator (default: ,)")
    args = parser.parse_args(argv)
    try:
        inspect_csv(args.csv, sep=args.sep)
        return 0
    except Exception as e:
        print("Error loading or inspecting CSV:", e, file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())