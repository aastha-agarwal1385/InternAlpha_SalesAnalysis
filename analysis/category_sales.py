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
# CATEGORY SALES ANALYSIS
# -----------------------------

category_sales = (
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("========== CATEGORY SALES ==========\n")
print(category_sales)

# -----------------------------
# PLOT GRAPH
# -----------------------------

plt.figure(figsize=(8,5))

plt.bar(
    category_sales.index,
    category_sales.values
)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

# Save graph
GRAPH_PATH = os.path.join(
    BASE_DIR,
    "graphs",
    "category_sales.png"
)

plt.savefig(GRAPH_PATH)

plt.show()

print("\nGraph saved successfully!")
print(GRAPH_PATH)