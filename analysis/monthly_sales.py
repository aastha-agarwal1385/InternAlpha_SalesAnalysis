import os
import pandas as pd
import matplotlib.pyplot as plt

# Locate dataset
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "Sample - Superstore.csv"
)

# Load dataset
df = pd.read_csv(
    DATASET_PATH,
    encoding="latin1"
)

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Group sales by month
monthly_sales = (
    df.groupby(df["Order Date"].dt.month)["Sales"]
      .sum()
)

print("========== MONTHLY SALES ==========\n")
print(monthly_sales)

# Plot graph
plt.figure(figsize=(10,6))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)

# Save graph
GRAPH_PATH = os.path.join(
    BASE_DIR,
    "graphs",
    "monthly_sales.png"
)

plt.savefig(GRAPH_PATH)

plt.show()

print("\nGraph saved successfully!")
print(GRAPH_PATH)