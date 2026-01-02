import pandas as pd
import glob
import os

def process_and_combine_data():
    # 1. Load Sales Data
    # Get list of all daily sales CSV files
    file_pattern = 'data/daily_sales_data_*.csv'
    files = glob.glob(file_pattern)

    if not files:
        print("No data files found.")
        return

    # Load and combine all CSVs
    dfs = []
    for file in files:
        try:
            df = pd.read_csv(file)
            dfs.append(df)
        except Exception as e:
            print(f"Error reading {file}: {e}")
            
    if not dfs:
        print("No valid data loaded.")
        return

    full_df = pd.concat(dfs, ignore_index=True)

    # 2. Filter for "Pink Morsel"
    # Normalize product name to lowercase just in case for filtering, 
    # ensuring we match 'pink morsel' correctly.
    full_df['product'] = full_df['product'].str.lower().str.strip()
    pink_morsel_df = full_df[full_df['product'] == 'pink morsel'].copy()

    # 3. Clean Price Column
    # Remove '$' and convert to float
    pink_morsel_df['price'] = pink_morsel_df['price'].astype(str).str.replace('$', '', regex=False)
    pink_morsel_df['price'] = pd.to_numeric(pink_morsel_df['price'], errors='coerce')

    # Clean Quantity Column
    pink_morsel_df['quantity'] = pd.to_numeric(pink_morsel_df['quantity'], errors='coerce')

    # Drop any rows with NaN in price or quantity after cleaning
    pink_morsel_df.dropna(subset=['price', 'quantity'], inplace=True)

    # 4. Create "Sales" Column
    pink_morsel_df['sales'] = pink_morsel_df['quantity'] * pink_morsel_df['price']

    # 5. Select Specific Columns
    # Assuming 'date' and 'region' exist and are named correctly in source.
    # Source cols verified previously: product, price, quantity, date, region
    pink_morsel_df = pink_morsel_df[['sales', 'date', 'region']]

    # 6. Clean Column Names (Capitalize)
    pink_morsel_df.rename(columns={'sales': 'Sales', 'date': 'Date', 'region': 'Region'}, inplace=True)

    # 7. Sort by Date
    pink_morsel_df['Date'] = pd.to_datetime(pink_morsel_df['Date'])
    pink_morsel_df.sort_values(by='Date', inplace=True)

    # 8. Save to CSV
    output_path = 'data/processed_sales.csv'
    pink_morsel_df.to_csv(output_path, index=False)
    print(f"Successfully processed data. Saved to {output_path}")
    print(pink_morsel_df.head())

if __name__ == "__main__":
    process_and_combine_data()
