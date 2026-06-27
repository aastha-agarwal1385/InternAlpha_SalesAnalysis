import os
import pandas as pd

# -----------------------------
# DATA LOADING
# -----------------------------

# Get project root folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build dataset path
csv_path = os.path.join(
    BASE_DIR,
    "dataset",
    "Sample - Superstore.csv"
)

print("Dataset Path:")
print(csv_path)

print("\nDoes file exist?")
print(os.path.exists(csv_path))

# Load dataset
df = pd.read_csv(
    csv_path,
    encoding="latin1"
)

# -----------------------------
# DATA EXPLORATION
# -----------------------------

print("\n========== DATASET OVERVIEW ==========")

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())

print("\nSummary Statistics:")
print(df.describe())

print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nTotal Profit:")
print(df["Profit"].sum())