#!/usr/bin/env python
"""
This script takes the CSV data exported from the t2
moodtracker and formats it with one rating per column
for better processing.
"""

import argparse

PARSER = argparse.ArgumentParser(description='Format t2 CSV for further processing.')
PARSER.add_argument('t2file', type=str, help='CSV file exported from t2 modd tracker')
ARGS = PARSER.parse_args()

with open(ARGS.t2file, "r") as infile:
    pass
