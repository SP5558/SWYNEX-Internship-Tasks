# Sales Data Analysis – End-to-End Analytics Case Study

## 1. Project Overview

This project presents an end-to-end Data Analytics case study developed as part of the SWYNEX Technologies Internship Program.

The project focuses on analyzing sales data to identify business trends, evaluate sales performance, discover patterns, and generate meaningful business insights.

The complete workflow includes data cleaning, exploratory data analysis, data visualization, and interactive dashboard development.

## 2. Problem Statement

Businesses generate large amounts of sales data, but raw data often contains missing values, duplicate records, inconsistent formats, and quality issues.

The objective of this project is to transform raw sales data into meaningful information by:

- Improving data quality and consistency.
- Analyzing sales performance across different categories and cities.
- Identifying monthly revenue trends.
- Understanding payment mode performance.
- Highlighting unusual records and potential data anomalies.
- Presenting findings through an interactive Power BI dashboard.

## 3. Dataset Information

| Description | Details |
|---|---|
| Dataset | Sales Dataset |
| Original Records | 3,060 |
| Original Columns | 8 |
| Final Records | 3,000 |
| Final Columns | 9 |
| Data Format | CSV |

The dataset contains sales-related information such as Order ID, Customer ID, City, Category, Quantity, Unit Price, Order Date, and Payment Mode.

An additional `Quantity_Status` column was created during data cleaning.

## 4. Data Cleaning and Preparation

**Tools:** Python, Pandas, NumPy

The raw dataset was cleaned and prepared through the following steps:

- Removed 60 duplicate records.
- Standardized city names and product categories.
- Handled missing City, Category, and Payment Mode values.
- Imputed missing quantities using the median of positive quantities.
- Cleaned UnitPrice values and converted them into numeric format.
- Standardized date formats.
- Added a Quantity_Status column to identify unusual quantity records.
- Validated missing values, duplicate records, data types, and dates.

### Data Quality Results

| Metric | Result |
|---|---:|
| Original Records | 3,060 |
| Duplicate Records Removed | 60 |
| Final Records | 3,000 |
| Remaining Duplicate Rows | 0 |
| Missing UnitPrice Values | 90 |
| Negative Quantities Flagged | 63 |
| Zero Quantities Flagged | 27 |

Negative and zero quantities were retained for review rather than automatically removed.

## 5. Exploratory Data Analysis

**Tools:** Python, Pandas, NumPy, Matplotlib

Exploratory Data Analysis was performed using the cleaned dataset.

The analysis included:

- Category-wise revenue analysis.
- City-wise revenue analysis.
- Monthly sales trend analysis.
- Payment mode performance analysis.
- Quantity status distribution.
- Unit price outlier detection using the IQR method.

### Key Findings

- Groceries generated the highest revenue among product categories.
- Kolkata recorded the highest revenue among the analyzed cities.
- UPI generated the highest revenue among payment modes.
- March 2025 recorded the highest monthly revenue in the available data.
- Potential price outliers and unusual quantity records were identified for review.

Revenue analysis used 2,740 valid records after applying the analysis filters.

## 6. Interactive Power BI Dashboard

**Tools:** Power BI Desktop, Power Query, DAX

An interactive Sales Performance Dashboard was developed to present the key findings clearly.

### Dashboard KPIs

- Total Revenue
- Total Orders
- Total Quantity
- Average Order Value

### Dashboard Visualizations

- Monthly Revenue Trend
- Category-wise Revenue Analysis
- City-wise Revenue Analysis
- Payment Mode Analysis
- Quantity Analysis

### Interactive Features

- Year and Month filters.
- City filter.
- Category filter.
- Payment Mode filter.

**Dashboard Screenshot:**  
[View Dashboard Preview](https://uploads.onecompiler.io/44te9mtgg/1794984342150/Screenshot%202026-11-18%20114943.png)

## 7. Business Insights and Recommendations

Based on the analysis, the following observations and recommendations were identified:

1. **Category Performance:** Groceries generated the highest revenue. The business can further examine product-level performance within this category.
2. **City Performance:** Kolkata recorded the highest revenue. Further analysis can help identify the factors contributing to its performance.
3. **Payment Preferences:** UPI generated the highest revenue. The business can continue monitoring digital payment trends.
4. **Monthly Performance:** March 2025 recorded the highest monthly revenue. Comparing this period with other months may help identify seasonal patterns.
5. **Data Quality:** Negative quantities, zero quantities, missing prices, and potential outliers should be reviewed to improve future reporting accuracy.

## 8. Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Microsoft Power BI
- Power Query
- DAX
- CSV
- Git and GitHub

## 9. Project Structure

The complete implementation is organized across the following folders:

- `Task1-Data-Cleaning/` – Data cleaning and preparation.
- `Task2-EDA/` – Exploratory data analysis, charts, and report.
- `Task3-PowerBI-Dashboard/` – Interactive Power BI dashboard.
- `Task4-Final-Project/` – Final end-to-end analytics case study.

## 10. Conclusion

This project demonstrates an end-to-end Data Analytics workflow, starting from raw data cleaning and preparation to exploratory analysis and interactive dashboard development.

It helped strengthen practical skills in Python, Pandas, data validation, data visualization, Power BI, DAX, and business insight generation.

The final outcome is a structured analytics case study that transforms raw sales data into meaningful business findings.

## Internship Details

**Organization:** SWYNEX Technologies  
**Program:** Data Analytics Internship  
**Project:** Final Data Analytics Case Study  
**Author:** Sagar Patil

---

*This project was completed as part of my practical learning journey in Data Analytics.*
