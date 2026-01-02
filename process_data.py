import pandas as pd
import glob
import os

def process_data():
    # 1. Load all CSV files
    file_pattern = 'data/daily_sales_data_*.csv'
    files = glob.glob(file_pattern)
    
    if not files:
        print("No data files found.")
        return

    print(f"Found {len(files)} files: {files}")
    
    dfs = []
    for file in files:
        try:
            df = pd.read_csv(file)
            dfs.append(df)
        except Exception as e:
            print(f"Error reading {file}: {e}")

    if not dfs:
        print("No dataframes loaded.")
        return

    # Concatenate all dataframes
    full_df = pd.concat(dfs, ignore_index=True)
    print(f"Combined data shape: {full_df.shape}")

    # 2. handle missing values
    # For now, we'll just drop rows with any missing values as a safe default
    # but strictly speaking, we should investigate. Given the context, we want a clean dataset.
    initial_rows = len(full_df)
    full_df.dropna(inplace=True)
    dropped_rows_na = initial_rows - len(full_df)
    if dropped_rows_na > 0:
        print(f"Dropped {dropped_rows_na} rows with missing values.")

    # 3. Clean 'price' column: remove '$' and convert to numeric
    # It might be object type due to '$'
    if full_df['price'].dtype == 'object':
        full_df['price'] = full_df['price'].str.replace('$', '', regex=False)
    
    full_df['price'] = pd.to_numeric(full_df['price'], errors='coerce')
    
    # 4. Clean 'quantity' column
    full_df['quantity'] = pd.to_numeric(full_df['quantity'], errors='coerce')

    # Drop rows where price or quantity became NaN after coercion
    full_df.dropna(subset=['price', 'quantity'], inplace=True)
    
    # Convert quantity to integer (it might be float after NaNs were introduced then dropped, or just safe casting)
    full_df['quantity'] = full_df['quantity'].astype(int)

    # 5. Convert 'date' to datetime
    full_df['date'] = pd.to_datetime(full_df['date'])

    # 6. Remove Duplicates
    before_dedup = len(full_df)
    full_df.drop_duplicates(inplace=True)
    deduped = before_dedup - len(full_df)
    if deduped > 0:
        print(f"Dropped {deduped} duplicate rows.")

    # 7. Create derived column 'sales'
    full_df['sales'] = full_df['price'] * full_df['quantity']

    # Final Check
    print("\n--- Final Data Info ---")
    print(full_df.info())
    print("\n--- First 5 Rows ---")
    print(full_df.head())
    
    # Save clean data
    output_file = 'data/cleaned_sales_data.csv'
    full_df.to_csv(output_file, index=False)
    print(f"\nCleaned data saved to {output_file}")

if __name__ == "__main__":
    process_data()
