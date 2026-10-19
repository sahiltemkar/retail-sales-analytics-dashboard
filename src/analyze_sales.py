from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "processed" / "cleaned_sales.csv"
IMAGE_DIR = ROOT / "images"

df = pd.read_csv(
    DATA_FILE,
    parse_dates=["Order Date", "Ship Date"]
)

# Overall KPIs
revenue = df["Sales"].sum()
profit = df["Profit"].sum()
margin = profit / revenue * 100
orders = df["Order ID"].nunique()
customers = df["Customer ID"].nunique()

print("=== OVERALL PERFORMANCE ===")
print(f"Revenue: ${revenue:,.2f}")
print(f"Profit: ${profit:,.2f}")
print(f"Profit margin: {margin:.2f}%")
print(f"Unique orders: {orders:,}")
print(f"Unique customers: {customers:,}")

# Category analysis
category = df.groupby("Category").agg(
    Revenue=("Sales", "sum"),
    Profit=("Profit", "sum")
).sort_values("Revenue", ascending=False)

print("\n=== CATEGORY PERFORMANCE ===")
print(category.round(2).to_string())

# Regional analysis
region = df.groupby("Region").agg(
    Revenue=("Sales", "sum"),
    Profit=("Profit", "sum")
).sort_values("Profit", ascending=False)

print("\n=== REGIONAL PERFORMANCE ===")
print(region.round(2).to_string())

# Monthly sales trend
monthly = (
    df.set_index("Order Date")["Sales"]
      .resample("MS")
      .sum()
)

IMAGE_DIR.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(11, 5))
monthly.plot(ax=ax, linewidth=2)
ax.set_title("Monthly Retail Sales")
ax.set_xlabel("Order Month")
ax.set_ylabel("Revenue ($)")
ax.grid(alpha=0.25)
fig.tight_layout()

chart_path = IMAGE_DIR / "monthly_sales.png"
fig.savefig(chart_path, dpi=150)
plt.close(fig)

# Basic reconciliation checks
assert abs(df["Sales"].sum() - revenue) < 0.01
assert abs(df["Profit"].sum() - profit) < 0.01
assert abs(monthly.sum() - revenue) < 0.01

print("\nAnalysis completed successfully.")
print("Monthly chart saved to:", chart_path)
