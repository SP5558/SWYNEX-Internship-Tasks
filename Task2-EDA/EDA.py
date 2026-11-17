
# ============================================================
# SWYNEX INTERNSHIP - TASK 2
# EXPLORATORY DATA ANALYSIS (EDA)
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ================= 1. LOAD DATASET =================

BASE_DIR = Path(__file__).resolve().parent
df = pd.read_csv(
    BASE_DIR.parent / "Task1-Data-Cleaning" / "cleaned_sales_data.csv"
)

CHART_DIR = BASE_DIR / "charts"
CHART_DIR.mkdir(exist_ok=True)

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 60)

print("\nDataset Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 Records:")
print(df.head())

# ================= 2. DATA PREPARATION =================

df["OrderDate"] = pd.to_datetime(
    df["OrderDate"],
    format="%d/%m/%Y",
    errors="coerce"
)

df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Use only valid, positive quantities and prices
analysis_df = df[
    (df["Quantity_Status"] == "Valid") &
    (df["Quantity"] > 0) &
    (df["UnitPrice"] > 0) &
    (df["OrderDate"].notna())
].copy()

print("\nRows available for revenue analysis:", len(analysis_df))

# ================= 3. DESCRIPTIVE STATISTICS =================

print("\n" + "=" * 60)
print("DESCRIPTIVE STATISTICS")
print("=" * 60)

print("\nQuantity Statistics:")
print(analysis_df["Quantity"].describe())

print("\nUnit Price Statistics:")
print(analysis_df["UnitPrice"].describe())

print("\nRevenue Statistics:")
print(analysis_df["Revenue"].describe())

print("\nCategory Counts:")
print(df["Category"].value_counts())

print("\nCity Counts:")
print(df["City"].value_counts())

print("\nPayment Mode Counts:")
print(df["PaymentMode"].value_counts())

# ================= 4. CATEGORY ANALYSIS =================

category_sales = (
    analysis_df.groupby("Category")
    .agg(
        Orders=("OrderID", "count"),
        Total_Quantity=("Quantity", "sum"),
        Total_Revenue=("Revenue", "sum")
    )
    .sort_values("Total_Revenue", ascending=False)
)

print("\nCategory-wise Analysis:")
print(category_sales.round(2))

plt.figure(figsize=(10, 6))
category_sales["Total_Revenue"].plot(
    kind="bar",
    title="Revenue by Product Category"
)
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(CHART_DIR / "category_sales.png")
plt.close()

# ================= 5. CITY ANALYSIS =================

city_sales = (
    analysis_df.groupby("City")
    .agg(
        Orders=("OrderID", "count"),
        Total_Revenue=("Revenue", "sum")
    )
    .sort_values("Total_Revenue", ascending=False)
)

print("\nCity-wise Analysis:")
print(city_sales.round(2))

plt.figure(figsize=(10, 6))
city_sales["Total_Revenue"].plot(
    kind="bar",
    title="Revenue by City"
)
plt.xlabel("City")
plt.ylabel("Revenue")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(CHART_DIR / "city_sales.png")
plt.close()

# ================= 6. MONTHLY TREND ANALYSIS =================

analysis_df["Month"] = (
    analysis_df["OrderDate"].dt.to_period("M").astype(str)
)

monthly_sales = (
    analysis_df.groupby("Month")
    .agg(
        Orders=("OrderID", "count"),
        Total_Revenue=("Revenue", "sum")
    )
    .sort_index()
)

print("\nMonthly Sales Analysis:")
print(monthly_sales.round(2))

plt.figure(figsize=(12, 6))
monthly_sales["Total_Revenue"].plot(
    marker="o",
    title="Monthly Revenue Trend"
)
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(CHART_DIR / "monthly_sales.png")
plt.close()

# ================= 7. PAYMENT MODE ANALYSIS =================

payment_sales = (
    analysis_df.groupby("PaymentMode")
    .agg(
        Orders=("OrderID", "count"),
        Total_Revenue=("Revenue", "sum")
    )
    .sort_values("Total_Revenue", ascending=False)
)

print("\nPayment Mode Analysis:")
print(payment_sales.round(2))

plt.figure(figsize=(8, 6))
payment_sales["Total_Revenue"].plot(
    kind="bar",
    title="Revenue by Payment Mode"
)
plt.xlabel("Payment Mode")
plt.ylabel("Revenue")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(CHART_DIR / "payment_analysis.png")
plt.close()

# ================= 8. QUANTITY STATUS ANALYSIS =================

quantity_status = df["Quantity_Status"].value_counts()

print("\nQuantity Status:")
print(quantity_status)

plt.figure(figsize=(8, 6))
quantity_status.plot(
    kind="bar",
    title="Quantity Status Distribution"
)
plt.xlabel("Quantity Status")
plt.ylabel("Number of Records")
plt.xticks(rotation=25)
plt.tight_layout()
plt.savefig(CHART_DIR / "quantity_analysis.png")
plt.close()

# ================= 9. OUTLIER ANALYSIS =================

Q1 = analysis_df["UnitPrice"].quantile(0.25)
Q3 = analysis_df["UnitPrice"].quantile(0.75)

IQR = Q3 - Q1
upper_limit = Q3 + (1.5 * IQR)

price_outliers = analysis_df[
    analysis_df["UnitPrice"] > upper_limit
]

print("\nUnit Price Outlier Analysis:")
print("Q1:", round(Q1, 2))
print("Q3:", round(Q3, 2))
print("IQR:", round(IQR, 2))
print("Upper Limit:", round(upper_limit, 2))
print("Potential Price Outliers:", len(price_outliers))

print("\nTop 5 Potential Price Outliers:")
print(
    price_outliers[
        ["OrderID", "Category", "City", "UnitPrice", "OrderDate"]
    ].nlargest(5, "UnitPrice")
)

# ================= 10. KEY INSIGHTS =================

top_category = category_sales["Total_Revenue"].idxmax()
top_city = city_sales["Total_Revenue"].idxmax()
top_payment = payment_sales["Total_Revenue"].idxmax()
top_month = monthly_sales["Total_Revenue"].idxmax()

insights = [
    f"1. {top_category} generated the highest revenue among product categories.",
    f"2. {top_city} generated the highest revenue among cities.",
    f"3. {top_payment} was the highest revenue-generating payment mode.",
    f"4. {top_month} recorded the highest monthly revenue in the available data.",
    f"5. {len(price_outliers)} records were identified as potential UnitPrice outliers using the IQR method.",
    f"6. {len(df[df['Quantity_Status'] == 'Possible Return - Review'])} records have negative quantities and need review.",
    f"7. {len(df[df['Quantity_Status'] == 'Zero Quantity - Review'])} records have zero quantities and need review."
]

print("\n" + "=" * 60)
print("KEY BUSINESS INSIGHTS")
print("=" * 60)

for insight in insights:
    print(insight)

# ================= 11. SAVE EDA REPORT =================

report_path = BASE_DIR / "EDA_Report.md"

with open(report_path, "w", encoding="utf-8") as file:
    file.write("# SWYNEX Internship - Task 2: Exploratory Data Analysis\n\n")

    file.write("## Dataset Overview\n\n")
    file.write(f"- Total cleaned records: {len(df)}\n")
    file.write(f"- Records used for revenue analysis: {len(analysis_df)}\n")
    file.write(f"- Total estimated revenue: {analysis_df['Revenue'].sum():,.2f}\n\n")

    file.write("## Descriptive Statistics\n\n")
    file.write("### Quantity\n\n")
    file.write(analysis_df["Quantity"].describe().round(2).to_markdown())
    file.write("\n\n### Unit Price\n\n")
    file.write(analysis_df["UnitPrice"].describe().round(2).to_markdown())
    file.write("\n\n### Revenue\n\n")
    file.write(analysis_df["Revenue"].describe().round(2).to_markdown())
    file.write("\n\n## Category-wise Analysis\n\n")
    file.write(category_sales.round(2).to_markdown())

    file.write("\n\n## City-wise Analysis\n\n")
    file.write(city_sales.round(2).to_markdown())

    file.write("\n\n## Monthly Sales Analysis\n\n")
    file.write(monthly_sales.round(2).to_markdown())

    file.write("\n\n## Payment Mode Analysis\n\n")
    file.write(payment_sales.round(2).to_markdown())

    file.write("\n\n## Quantity Status Analysis\n\n")
    file.write(quantity_status.to_frame("Records").to_markdown())

    file.write("\n\n## Key Insights\n\n")
    for insight in insights:
        file.write(f"- {insight}\n")

    file.write("\n## Important Notes\n\n")
    file.write("- Revenue is calculated as Quantity multiplied by UnitPrice.\n")
    file.write("- Missing UnitPrice records are excluded from revenue calculations.\n")
    file.write("- Negative and zero quantities are excluded from revenue analysis and retained for review.\n")
    file.write("- Potential outliers are flagged for investigation, not automatically removed.\n")
    file.write("- The 2026 data may be incomplete, so monthly comparisons should be interpreted carefully.\n")
    file.write("- 90 records contain imputed quantity values and are excluded from revenue analysis under the current Valid-only filter.\n")
    file.write("- 2 records contain future dates (December 2026) relative to the analysis date of November 17, 2026. These records require verification.\n")


print("\nDate Range:")
print("Start Date:", df["OrderDate"].min())
print("End Date:", df["OrderDate"].max())

print("\nFuture Dated Records:")
print(df[df["OrderDate"] > pd.Timestamp.today()])
print("\nCharts saved in:", CHART_DIR)
print("EDA Report saved as:", report_path)
print("\nEDA COMPLETED SUCCESSFULLY!")

