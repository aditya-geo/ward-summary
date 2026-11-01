# Ward Summary Tool

## Question
Which wards are the densest, and how much green space does each have?

## Data
Made-up numbers for 6 wards (practice data, not real).

## Method
Python with pandas: density = population / area; green share = green area / ward area x 100.
A bar chart is drawn with matplotlib.

## Result
Ward 5 has the highest density (about 33,729 people per km2).
The mean green share is about 9.9%.

## Limits
Made-up data, only 6 wards, no maps or spatial analysis yet.

## How to run
pip install pandas matplotlib
python ward_summary.py
