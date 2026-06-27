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
# PROFIT ANALYSIS
# -----------------------------

category_profit = (
    df.groupby("Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

print("========== CATEGORY PROFIT ==========\n")
print(category_profit)

# -----------------------------
# PLOT GRAPH
# -----------------------------

plt.figure(figsize=(8,5))

plt.bar(
    category_profit.index,
    category_profit.values
)

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")

# Save graph
GRAPH_PATH = os.path.join(
    BASE_DIR,
    "graphs",
    "profit_analysis.png"
)

plt.savefig(GRAPH_PATH)

plt.show()

print("\nGraph saved successfully!")
print(GRAPH_PATH)