from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

RAW_FILE = ROOT / "data" / "raw" / "Sample_Superstore.csv"
OUTPUT_FILE = ROOT / "data" / "processed" / "cleaned_sales.csv"


def main():
    df = pd.read_csv(RAW_FILE, encoding="utf-8-sig")

    print("Original dataset shape:", df.shape)

    # Validate the source structure.
    required = [
        "Row ID", "Order ID", "Customer ID",
        "Order Date", "Ship Date", "Region",
        "Category", "Sales", "Quantity",
        "Discount", "Profit"
    ]

    missing_columns = set(required) - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")

    # Row ID should uniquely identify each order line.
    if df["Row ID"].duplicated().any():
        raise ValueError("Duplicate Row IDs detected.")

    # Parse the dates using the format confirmed in our dataset.
    for column in ["Order Date", "Ship Date"]:
        df[column] = pd.to_datetime(
            df[column],
            format="%d/%m/%y",
            errors="raise"
        )

    # Ensure numerical columns have the correct data types.
    numeric_columns = ["Sales", "Quantity", "Discount", "Profit"]
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="raise")

    # Check required values and business constraints.
    if df[required].isna().any().any():
        raise ValueError("Missing values found in required columns.")

    if (df["Sales"] < 0).any():
        raise ValueError("Unexpected negative sales values.")

    if (df["Quantity"] <= 0).any():
        raise ValueError("Unexpected non-positive quantities.")

    if not df["Discount"].between(0, 1).all():
        raise ValueError("Discount values must be between 0 and 1.")

    if (df["Ship Date"] < df["Order Date"]).any():
        raise ValueError("Shipping date precedes order date.")

    # Add useful analytical features.
    df["Order Year"] = df["Order Date"].dt.year
    df["Order Month"] = df["Order Date"].dt.strftime("%Y-%m")
    df["Shipping Days"] = (
        df["Ship Date"] - df["Order Date"]
    ).dt.days

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(
        OUTPUT_FILE,
        index=False,
        date_format="%Y-%m-%d"
    )

    # Verify the saved output.
    cleaned = pd.read_csv(OUTPUT_FILE, parse_dates=["Order Date", "Ship Date"])

    assert len(cleaned) == len(df)
    assert cleaned["Row ID"].is_unique
    assert cleaned["Sales"].notna().all()
    assert cleaned["Profit"].notna().all()

    print("\nCleaning completed successfully.")
    print("Rows retained:", len(cleaned))
    print("Columns after transformation:", len(cleaned.columns))
    print(f"Total revenue: ${cleaned['Sales'].sum():,.2f}")
    print(f"Total profit: ${cleaned['Profit'].sum():,.2f}")
    print("Output:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
