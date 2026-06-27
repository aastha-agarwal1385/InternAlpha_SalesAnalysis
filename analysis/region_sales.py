import os
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# LOAD DATASET
# -----------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "Sample - Superstore.csv"
)

df = pd.read_csv(
    DATASET_PATH,
    encoding="latin1"
)

# -----------------------------
# REGION SALES ANALYSIS
# -----------------------------

region_sales = (
    df.groupby("Region")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("========== REGION SALES ==========\n")
print(region_sales)

# -----------------------------
# PLOT GRAPH
# -----------------------------

plt.figure(figsize=(8,5))

plt.bar(
    region_sales.index,
    region_sales.values
)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

# Save graph
GRAPH_PATH = os.path.join(
    BASE_DIR,
    "graphs",
    "region_sales.png"
)

plt.savefig(GRAPH_PATH)

plt.show()

print("\nGraph saved successfully!")
print(GRAPH_PATH)