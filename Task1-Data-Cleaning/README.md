# SWYNEX – Data Cleaning & Preparation

## Project Overview

This project focuses on cleaning and preparing a raw sales dataset using Python and Pandas as part of **SWYNEX Internship – Task 1: Data Cleaning & Preparation**.

The objective was to identify and handle missing values, duplicate records, inconsistent text values, incorrect data types, invalid prices, and inconsistent date formats to improve overall data quality.

## Tools & Technologies

- Python
- Pandas
- NumPy
- VS Code

## Dataset Information

- **Dataset:** Raw Sales Data
- **Original Records:** 3,060
- **Original Columns:** 8
- **Final Records:** 3,000
- **Final Columns:** 9

## Data Quality Issues Identified

The original dataset contained:

- Missing values in City, Category, Quantity, and PaymentMode.
- 60 duplicate records.
- Inconsistent city names and capitalization.
- Inconsistent product category names and spelling mistakes.
- UnitPrice values containing `Rs.` prefixes and `-` entries.
- Mixed date formats (ISO, DD-MM-YYYY, MM/DD/YYYY, etc.).
- Negative and zero quantities.

## Data Cleaning & Preparation Steps

1. **Duplicate Removal:** Removed 60 exact duplicate records.
2. **City Standardization:** Standardized city names, including Mumbai, Delhi, Pune, Chennai, Kolkata, Hyderabad, and Bengaluru.
3. **Category Standardization:** Corrected inconsistent category names such as `Furnitur`, `Stationary`, and `Electronis`.
4. **Missing Values:** Replaced missing City, Category, and PaymentMode values with `Unknown`.
5. **Quantity Handling:** Filled missing quantities using the median of positive quantities.
6. **Quantity Validation:** Added a `Quantity_Status` column to identify valid, imputed, possible return, and zero-quantity records.
7. **Price Cleaning:** Removed `Rs.` prefixes, converted UnitPrice into numeric format, and treated `-` as a missing value.
8. **Date Standardization:** Converted dates into a consistent DD/MM/YYYY format.
9. **Data Validation:** Checked duplicate records, missing values, data types, and exported CSV date formats.

## Important Data Handling Decisions

- Negative quantities were retained and flagged as `Possible Return - Review` because they may represent product returns.
- Zero quantities were retained and flagged as `Zero Quantity - Review`.
- Missing UnitPrice values were kept as missing instead of assigning fabricated prices.
- Ambiguous dates were interpreted using the DD/MM assumption when both day and month values were 12 or below. This assumption could not be independently verified from the source dataset.
- Missing quantities were imputed using the median of positive quantity values.

## Final Data Quality Results

| Metric | Result |
|---|---:|
| Original Records | 3,060 |
| Duplicate Records Removed | 60 |
| Final Records | 3,000 |
| Remaining Duplicate Rows | 0 |
| Remaining Duplicate Order IDs | 0 |
| Missing UnitPrice Values | 90 |
| Invalid Dates | 0 |
| Negative Quantities Flagged | 63 |
| Zero Quantities Flagged | 27 |
| Exported Date Format Validation | Passed |

## Project Structure

```text
SWYNEX-Internship-Tasks/
│
└── Task1-Data-Cleaning/
    ├── README.md
    ├── Data.py
    ├── raw_sales_data.csv
    ├── cleaned_sales_data.csv
    └── requirements.txt
```

## How to Run the Project

**Step 1: Clone the repository**

```bash
git clone https://github.com/SP5558/SWYNEX-Internship-Tasks.git
```

**Step 2: Navigate to the Task 1 folder**

```bash
cd SWYNEX-Internship-Tasks/Task1-Data-Cleaning
```

**Step 3: Install dependencies**

```bash
pip install -r requirements.txt
```

**Step 4: Run the Python script**

```bash
python Data.py
```

The cleaned dataset will be generated as `cleaned_sales_data.csv` inside the Task 1 folder.

## Key Learning Outcomes

- Understanding real-world data quality issues.
- Handling missing and duplicate records using Pandas.
- Standardizing inconsistent categorical values.
- Cleaning and converting numeric columns.
- Handling mixed date formats.
- Validating cleaned datasets.
- Exporting clean datasets for further analysis.

## Internship

**Organization:** SWYNEX Technologies  
**Task:** Task 1 – Data Cleaning & Preparation  
**Technology:** Python, Pandas, NumPy

---

**Author:** Sagar Patil
