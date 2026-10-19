# Retail Sales Analytics Dashboard

## Overview
An end-to-end retail sales analytics project using Python, Pandas, and Microsoft Power BI to analyze sales performance, profitability, product categories, and regional trends.

## Dataset
Sample Superstore dataset containing 9,994 retail order records, including order dates, customer segments, regions, products, sales, discounts, and profit.

## Tools and Technologies
- Python
- Pandas
- Matplotlib
- Microsoft Power BI
- DAX

## Data Preparation
- Validated required columns and record identifiers.
- Converted order and shipping dates into valid date formats.
- Checked numeric fields and business rules.
- Created Order Year, Order Month, and Shipping Days features.
- Exported the cleaned dataset for Power BI.

## Dashboard Features
- Total Revenue
- Total Profit
- Profit Margin
- Total Orders
- Monthly Sales Trend
- Revenue by Category
- Profit by Region
- Top 10 Products by Revenue
- Profit Margin by Category
- Interactive filters for region, order year, and category

## Key Metrics
- Revenue: $2,297,200.86
- Profit: $286,397.02
- Profit Margin: 12.47%
- Unique Orders: approximately 5,000

## Project Structure
- `data/raw/` — original dataset
- `data/processed/` — cleaned dataset
- `src/clean_data.py` — data cleaning and validation
- `src/analyze_sales.py` — exploratory analysis and chart generation
- `dashboard/` — Power BI PDF export and dashboard files
- `images/` — generated charts

## How to Run
1. Install Python 3.10 or later.
2. Install dependencies:
   `pip install pandas matplotlib`
3. Run the cleaning script:
   `python src/clean_data.py`
4. Run the analysis script:
   `python src/analyze_sales.py`
5. Open the Power BI `.pbix` file to explore the interactive dashboard.

## Notes
This project uses a sample retail dataset for portfolio and learning purposes.
