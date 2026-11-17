# SWYNEX Internship - Task 2: Exploratory Data Analysis

## Dataset Overview

- Total cleaned records: 3000
- Records used for revenue analysis: 2740
- Total estimated revenue: 52,554,988.10

## Descriptive Statistics

### Quantity

|       |   Quantity |
|:------|-----------:|
| count |    2740    |
| mean  |       5    |
| std   |       2.62 |
| min   |       1    |
| 25%   |       3    |
| 50%   |       5    |
| 75%   |       7    |
| max   |       9    |

### Unit Price

|       |   UnitPrice |
|:------|------------:|
| count |     2740    |
| mean  |     3997.53 |
| std   |    15422.7  |
| min   |      100.06 |
| 25%   |     1376.98 |
| 50%   |     2559.24 |
| 75%   |     3779.27 |
| max   |   243764    |

### Revenue

|       |         Revenue |
|:------|----------------:|
| count |  2740           |
| mean  | 19180.7         |
| std   | 79977.7         |
| min   |   147.47        |
| 25%   |  4404.16        |
| 50%   |  9897.76        |
| 75%   | 19085.2         |
| max   |     2.05868e+06 |

## Category-wise Analysis

| Category    |   Orders |   Total_Quantity |   Total_Revenue |
|:------------|---------:|-----------------:|----------------:|
| Groceries   |      540 |             2718 |     1.28952e+07 |
| Electronics |      529 |             2604 |     1.18944e+07 |
| Furniture   |      526 |             2584 |     9.15448e+06 |
| Clothing    |      518 |             2650 |     8.88181e+06 |
| Stationery  |      545 |             2736 |     7.8467e+06  |
| Unknown     |       82 |              419 |     1.88234e+06 |

## City-wise Analysis

| City      |   Orders |    Total_Revenue |
|:----------|---------:|-----------------:|
| Kolkata   |      382 |      9.94704e+06 |
| Bengaluru |      371 |      9.90204e+06 |
| Delhi     |      380 |      7.88602e+06 |
| Chennai   |      384 |      6.82239e+06 |
| Mumbai    |      400 |      6.64195e+06 |
| Pune      |      377 |      5.60804e+06 |
| Hyderabad |      367 |      4.97531e+06 |
| Unknown   |       79 | 772189           |

## Monthly Sales Analysis

| Month   |   Orders |    Total_Revenue |
|:--------|---------:|-----------------:|
| 2025-01 |      193 |      3.141e+06   |
| 2025-02 |      174 |      2.02002e+06 |
| 2025-03 |      203 |      6.84017e+06 |
| 2025-04 |      221 |      3.27071e+06 |
| 2025-05 |      225 |      4.22229e+06 |
| 2025-06 |      217 |      3.07698e+06 |
| 2025-07 |      223 |      3.70014e+06 |
| 2025-08 |      189 |      3.84093e+06 |
| 2025-09 |      198 |      5.2912e+06  |
| 2025-10 |      206 |      2.96586e+06 |
| 2025-11 |      219 |      3.95093e+06 |
| 2025-12 |      213 |      5.84476e+06 |
| 2026-01 |      208 |      3.68199e+06 |
| 2026-02 |       24 | 370958           |
| 2026-03 |        6 | 105661           |
| 2026-04 |        7 |  86667.1         |
| 2026-05 |        2 |   9209.8         |
| 2026-06 |        2 |   9624.91        |
| 2026-07 |        3 |  20399.2         |
| 2026-08 |        1 |   9426.44        |
| 2026-09 |        1 |  20757.5         |
| 2026-10 |        2 |  31572.5         |
| 2026-11 |        1 |  19060.4         |
| 2026-12 |        2 |  24669.7         |

## Payment Mode Analysis

| PaymentMode   |   Orders |   Total_Revenue |
|:--------------|---------:|----------------:|
| Upi           |      521 |     1.1898e+07  |
| Cash          |      574 |     1.1156e+07  |
| Credit Card   |      561 |     9.98373e+06 |
| Debit Card    |      526 |     9.91068e+06 |
| Net Banking   |      472 |     8.36502e+06 |
| Unknown       |       86 |     1.24148e+06 |

## Quantity Status Analysis

| Quantity_Status          |   Records |
|:-------------------------|----------:|
| Valid                    |      2820 |
| Missing - Imputed        |        90 |
| Possible Return - Review |        63 |
| Zero Quantity - Review   |        27 |

## Key Insights

- 1. Groceries generated the highest revenue among product categories.
- 2. Kolkata generated the highest revenue among cities.
- 3. Upi was the highest revenue-generating payment mode.
- 4. 2025-03 recorded the highest monthly revenue in the available data.
- 5. 34 records were identified as potential UnitPrice outliers using the IQR method.
- 6. 63 records have negative quantities and need review.
- 7. 27 records have zero quantities and need review.

## Important Notes

- Revenue is calculated as Quantity multiplied by UnitPrice.
- Missing UnitPrice records are excluded from revenue calculations.
- Negative and zero quantities are excluded from revenue analysis and retained for review.
- Potential outliers are flagged for investigation, not automatically removed.
- The 2026 data may be incomplete, so monthly comparisons should be interpreted carefully.
