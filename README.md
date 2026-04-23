# GDP-Analysis
Analyzing the relationship between factors pertaining to GDB and gender inequality across 100+ countries.
# GDP and Gender Labor Ratio Visualization Project

## Project Overview

This project explores the relationship between year-over-year changes in GDP and changes in the female-to-male labor force participation ratio across countries.

The project cleans raw GDP, Gender Inequality Index, and labor force ratio datasets, merges the cleaned GDP and labor ratio data, and creates an interactive Streamlit visualization where users can select a country and compare both trends over time.

## Files

- `cleaning.py`  
  Cleans the raw GDP, Gender Inequality Index, and labor ratio datasets. It outputs:
  - `gdp_clean.csv`
  - `gii_clean.csv`
  - `labor_ratio_clean.csv`

- `generateplotGDPvRatio.py`  
  Calculates year-over-year changes in GDP and labor ratio, then merges them into `merged.csv`. :contentReference[oaicite:0]{index=0}

- `Dropdown_ratiovGDP.py`  
  Runs the Streamlit app with a dropdown menu for country selection and plots GDP change against labor ratio change. :contentReference[oaicite:1]{index=1}

- `merged.csv`  
  Final merged dataset used for visualization.

## How It Works

1. Raw datasets are loaded.
2. Unnecessary columns and invalid country codes are removed.
3. Data is reshaped from wide format to long format.
4. GDP and labor ratio changes are calculated by country and year.
5. The cleaned datasets are merged.
6. A Streamlit dropdown lets users select a country and view the trends.

## Requirements

Install the needed libraries:

```bash
pip install pandas matplotlib streamlit numpy pycountry
