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
# TOP PRODUCTS ANALYSIS
# -----------------------------

top_products = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("========== TOP 10 PRODUCTS ==========\n")
print(top_products)

# -----------------------------
# PLOT GRAPH
# -----------------------------

plt.figure(figsize=(12,6))

plt.barh(
    top_products.index,
    top_products.values
)

plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product Name")

plt.gca().invert_yaxis()   # Highest sales at the top

plt.tight_layout()

GRAPH_PATH = os.path.join(
    BASE_DIR,
    "graphs",
    "top_products.png"
)

plt.savefig(GRAPH_PATH)

plt.show()

print("\nGraph saved successfully!")
print(GRAPH_PATH)