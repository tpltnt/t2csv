#!/usr/bin/env python
"""
This script takes the CSV data exported from the t2
moodtracker and formats it with one rating per column
for better processing.
"""
import argparse
import csv

# parse commandline arguments
PARSER = argparse.ArgumentParser(description='Format t2 CSV for further processing.')
PARSER.add_argument('t2file', type=str, help='CSV file exported from t2 modd tracker')
PARSER.add_argument('--outfile', type=str, default='output.csv', help='CSV file to write to')
ARGS = PARSER.parse_args()

# scale metadata
SCALE = ""
LOW_END = ""
HIGH_END = ""

NEW_ROWS = []
TIMESTAMPS = set()

# read data from file
with open(ARGS.t2file, "r") as infile:
    READER = csv.reader(infile, delimiter=',', quotechar='"')
    for row in READER:
        if row[0] == 'group':
            continue

        # catch new rating scale (for the following data)
        if row[0] == 'scale':
            SCALE = row[0]
            LOW_END = row[1]
            HIGH_END = row[2]

        # actually process the result
        if row[0] == 'result':
            timestamp = row[1]
            rating = row[2]
            data = dict()
            data['low'] = LOW_END
            data['high'] = HIGH_END
            data['timestamp'] = timestamp
            data['rating'] = rating
            NEW_ROWS.append(data)
            TIMESTAMPS.add(timestamp)
        # TODO: process notes


# write data to file
with open(ARGS.outfile, "w") as outfile:
    DATAWRITER = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)

    # sort by timestamp
    for t in sorted(TIMESTAMPS):
        # check each row
        for d in NEW_ROWS:
            # for the current timestamp (to process)
            if t == d['timestamp']:
                DATAWRITER.writerow([
                    d['timestamp'],
                    d['low'],
                    d['high'],
                    d['rating']
                ])
