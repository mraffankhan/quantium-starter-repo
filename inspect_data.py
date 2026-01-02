import pandas as pd
import os

def inspect_data():
    # Define file path
    file_path = 'data/daily_sales_data_0.csv'
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    # 1. Load the CSV into a DataFrame
    print(f"Loading data from {file_path}...")
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.\n")
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # 2. Inspect the DataFrame
    print("--- First 5 rows ---")
    print(df.head())
    print("\n")

    print("--- Column Names ---")
    print(df.columns.tolist())
    print("\n")

    print("--- Data Types ---")
    print(df.dtypes)
    print("\n")

    print("--- Basic Summary (Describe) ---")
    print(df.describe(include='all')) # include='all' to see non-numeric stats too
    print("\n")

    # 3. Check for Data Quality Issues
    print("--- Missing Values ---")
    print(df.isnull().sum())
    print("\n")
    
    # Check for duplicates
    duplicates = df.duplicated().sum()
    print(f"--- Duplicated Rows: {duplicates} ---\n")

    # Check for obvious quality issues (e.g. negative prices, quantity)
    # This assumes column names like 'price', 'quantity' might exist, but we do generic checks first.
    # We can inspect object columns for weird values if needed, but keeping it simple for now.

if __name__ == "__main__":
    inspect_data()
