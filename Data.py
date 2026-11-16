
# ============================================================
# SWYNEX INTERNSHIP - TASK 1
# DATA CLEANING AND PREPARATION USING PYTHON & PANDAS
# ============================================================

# ================= 1. IMPORT LIBRARIES =================

import pandas as pd
import numpy as np
import re
from datetime import datetime


# ================= 2. LOAD DATASET =================

df = pd.read_csv("raw_sales_data.csv")

print("=" * 60)
print("INITIAL DATASET OVERVIEW")
print("=" * 60)

print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Shape:", df.shape)
print("\nColumn Names:", df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nExact Duplicate Records:", df.duplicated().sum())


# ================= 3. DETAILED DATA INSPECTION =================

print("\n" + "=" * 60)
print("DETAILED DATA INSPECTION")
print("=" * 60)

print("\nCity Values:")
print(df["City"].value_counts(dropna=False))

print("\nCategory Values:")
print(df["Category"].value_counts(dropna=False))

print("\nPayment Modes:")
print(df["PaymentMode"].value_counts(dropna=False))

print("\nQuantity Statistics:")
print(df["Quantity"].describe())

print("\nUnitPrice Sample Values:")
print(df["UnitPrice"].unique()[:20])

print("\nOrderDate Sample Values:")
print(df["OrderDate"].unique()[:20])

print("\nDuplicate Records Sample:")
print(df[df.duplicated(keep=False)].head(10))


# ================= 4. INVESTIGATE DATA QUALITY ISSUES =================

print("\n" + "=" * 60)
print("DATA QUALITY INVESTIGATION")
print("=" * 60)

print("\nNegative Quantity Count:")
print((df["Quantity"] < 0).sum())

print("\nZero Quantity Count:")
print((df["Quantity"] == 0).sum())

unit_price_text = df["UnitPrice"].astype("string").str.strip()

print("\nInvalid UnitPrice ('-') Count:")
print(unit_price_text.eq("-").sum())

print("\nCurrency Format Count:")
print(unit_price_text.str.contains("Rs.", regex=False, na=False).sum())

print("\nDuplicate OrderID Count:")
print(df["OrderID"].duplicated().sum())

print("\nMissing Values Percentage:")
print((df.isnull().sum() / len(df) * 100).round(2))

print("\nDate Format Patterns:")

dates = df["OrderDate"].astype("string").str.strip()

print(
    "ISO Format:",
    dates.str.match(r"^\d{4}-\d{2}-\d{2}$", na=False).sum()
)

print(
    "Hyphen Separated:",
    dates.str.match(r"^\d{1,2}-\d{1,2}-\d{2,4}$", na=False).sum()
)

print(
    "Slash Separated:",
    dates.str.match(r"^\d{1,2}/\d{1,2}/\d{2,4}$", na=False).sum()
)

print("\nNegative Quantity Records:")
print(df[df["Quantity"] < 0].head(10))

print("\nInvalid Price Records:")
print(df[unit_price_text.eq("-")].head(10))


# ================= 5. CREATE CLEAN DATASET =================

df_clean = df.copy()

original_rows = len(df_clean)

print("\n" + "=" * 60)
print("DATA CLEANING STARTED")
print("=" * 60)

print("\nOriginal Shape:", df_clean.shape)


# ---------- 5.1 REMOVE EXACT DUPLICATES ----------

duplicate_count = df_clean.duplicated().sum()

df_clean = df_clean.drop_duplicates().copy()

print("\nDuplicates Removed:", duplicate_count)
print("Shape After Removing Duplicates:", df_clean.shape)


# ---------- 5.2 CLEAN CITY NAMES ----------

df_clean["City"] = (
    df_clean["City"]
    .astype("string")
    .str.strip()
    .str.lower()
)

city_mapping = {
    "bangalore": "bengaluru",
    "new delhi": "delhi"
}

df_clean["City"] = (
    df_clean["City"]
    .replace(city_mapping)
    .str.title()
    .fillna("Unknown")
)


# ---------- 5.3 CLEAN CATEGORY NAMES ----------

df_clean["Category"] = (
    df_clean["Category"]
    .astype("string")
    .str.strip()
    .str.lower()
    .str.replace(r"\s+", "", regex=True)
)

category_mapping = {
    "furnitur": "furniture",
    "stationary": "stationery",
    "grocerys": "groceries",
    "grocery": "groceries",
    "clothings": "clothing",
    "electronis": "electronics",
    "electronic": "electronics"
}

df_clean["Category"] = (
    df_clean["Category"]
    .replace(category_mapping)
    .str.title()
    .fillna("Unknown")
)


# ---------- 5.4 CLEAN PAYMENT MODE ----------

df_clean["PaymentMode"] = (
    df_clean["PaymentMode"]
    .astype("string")
    .str.strip()
    .str.title()
    .fillna("Unknown")
)


# ---------- 5.5 CONVERT UNIT PRICE TO NUMERIC ----------

df_clean["UnitPrice"] = (
    df_clean["UnitPrice"]
    .astype("string")
    .str.strip()
    .str.replace(r"(?i)^Rs\.\s*", "", regex=True)
    .replace("-", np.nan)
)

df_clean["UnitPrice"] = pd.to_numeric(
    df_clean["UnitPrice"],
    errors="coerce"
)


# ---------- 5.6 STANDARDIZE ORDER DATE ----------

# Standard date format: DD/MM/YYYY
# ISO dates are also supported.
# Ambiguous dates are assumed to be DD/MM/YYYY.
# This assumption should be documented because the
# original source date convention is not confirmed.

ambiguous_dates = []

def parse_date(value):

    if pd.isna(value):
        return pd.NaT

    value = str(value).strip()

    parts = value.replace("-", "/").split("/")

    if len(parts) != 3:
        return pd.NaT

    first, second, year = parts

    try:

        # ISO format: YYYY-MM-DD
        if len(first) == 4:
            date_format = "%Y/%m/%d"

        else:
            first_num = int(first)
            second_num = int(second)

            if first_num > 12:
                # DD/MM/YYYY
                date_format = (
                    "%d/%m/%Y" if len(year) == 4
                    else "%d/%m/%y"
                )

            elif second_num > 12:
                # MM/DD/YYYY
                date_format = (
                    "%m/%d/%Y" if len(year) == 4
                    else "%m/%d/%y"
                )

            else:
                # Ambiguous date: assume DD/MM/YYYY
                ambiguous_dates.append(value)

                date_format = (
                    "%d/%m/%Y" if len(year) == 4
                    else "%d/%m/%y"
                )

        return pd.to_datetime(
            datetime.strptime(
                value.replace("-", "/"),
                date_format
            )
        )

    except (ValueError, TypeError):
        return pd.NaT


df_clean["OrderDate"] = df_clean["OrderDate"].apply(parse_date)

print("\nDate Standardization:")
print("Ambiguous Dates Assumed as DD/MM:", len(ambiguous_dates))
print("Invalid Dates:", df_clean["OrderDate"].isna().sum())


# ---------- 5.7 HANDLE QUANTITY ISSUES ----------

# Preserve original quantity status before imputation.

df_clean["Quantity_Status"] = np.select(
    [
        df_clean["Quantity"].isna(),
        df_clean["Quantity"] < 0,
        df_clean["Quantity"] == 0
    ],
    [
        "Missing - Imputed",
        "Possible Return - Review",
        "Zero Quantity - Review"
    ],
    default="Valid"
)

# Calculate median using positive quantities only.

valid_quantity_median = df_clean.loc[
    df_clean["Quantity"] > 0,
    "Quantity"
].median()

# Fill missing quantity values.

df_clean["Quantity"] = df_clean["Quantity"].fillna(
    valid_quantity_median
)


# ================= 6. FINAL DATA VALIDATION =================

print("\n" + "=" * 60)
print("FINAL DATA QUALITY REPORT")
print("=" * 60)

print("\n1. Original Records:", original_rows)
print("2. Final Records:", len(df_clean))
print("3. Duplicates Removed:", duplicate_count)

print("\n4. Final Dataset Shape:")
print(df_clean.shape)

print("\n5. Exact Duplicate Rows:")
print(df_clean.duplicated().sum())

print("\n6. Duplicate Order IDs:")
print(df_clean["OrderID"].duplicated().sum())

print("\n7. Missing Values:")
print(df_clean.isnull().sum())

print("\n8. Missing UnitPrice Values:")
print(df_clean["UnitPrice"].isna().sum())

print("\n9. Non-positive UnitPrice Values:")
print(df_clean["UnitPrice"].le(0).sum())

print("\n10. Negative Quantity:")
print((df_clean["Quantity"] < 0).sum())

print("\n11. Zero Quantity:")
print((df_clean["Quantity"] == 0).sum())

print("\n12. Data Types:")
print(df_clean.dtypes)

print("\n13. Date Range:")
print("Minimum:", df_clean["OrderDate"].min())
print("Maximum:", df_clean["OrderDate"].max())

print("\n14. Quantity Status:")
print(df_clean["Quantity_Status"].value_counts())

print("\n15. Final City Categories:")
print(df_clean["City"].value_counts())

print("\n16. Final Product Categories:")
print(df_clean["Category"].value_counts())


# ================= 7. SAVE CLEANED DATASET =================

if df_clean["OrderDate"].isna().sum() == 0:

    output_file = "cleaned_sales_data.csv"

    df_clean.to_csv(
        output_file,
        index=False,
        date_format="%d/%m/%Y"
    )

    print("\n" + "=" * 60)
    print("DATA CLEANING COMPLETED SUCCESSFULLY")
    print("=" * 60)

    print("\nCleaned dataset saved as:", output_file)

else:

    print("\nWARNING: Invalid dates found.")
    print("Please review dates before exporting the final dataset.")


# ================= 8. VERIFY EXPORTED CSV =================

if df_clean["OrderDate"].isna().sum() == 0:

    saved_df = pd.read_csv("cleaned_sales_data.csv")

    date_format_check = saved_df["OrderDate"].astype("string").str.fullmatch(
        r"\d{2}/\d{2}/\d{4}",
        na=False
    )

    print("\nEXPORTED CSV VERIFICATION")

    print("Saved Rows:", len(saved_df))
    print("Valid DD/MM/YYYY Dates:", date_format_check.sum())
    print("Invalid Date Formats:", (~date_format_check).sum())

    if date_format_check.all():
        print("CSV Date Format Verification: PASSED")
    else:
        print("CSV Date Format Verification: FAILED")
