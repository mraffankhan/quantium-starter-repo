import pandas as pd

def analyze_sales_impact():
    # 1. Load the processed data
    file_path = 'data/processed_sales.csv'
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Please run process_sales.py first.")
        return

    # 2. Convert Date column
    df['Date'] = pd.to_datetime(df['Date'])

    # 3. Split data into Before and After periods
    # Price increase date: 15 January 2021
    cutoff_date = pd.Timestamp('2021-01-15')
    
    before_price_increase = df[df['Date'] < cutoff_date]
    after_price_increase = df[df['Date'] >= cutoff_date]

    # 4. Calculate Total Sales
    sales_before = before_price_increase['Sales'].sum()
    sales_after = after_price_increase['Sales'].sum()

    # Calculate Average Daily Sales for better comparison (just in case timeframes differ)
    # The prompt asked for "Total Sales" primarily, but average is good context.
    # We will stick to prompt's primary request for clarity, but adding average helps if durations differ.
    days_before = (cutoff_date - df['Date'].min()).days
    days_after = (df['Date'].max() - cutoff_date).days + 1 # +1 to include the last day
    
    avg_sales_before = sales_before / days_before if days_before > 0 else 0
    avg_sales_after = sales_after / days_after if days_after > 0 else 0

    
    # Compare
    difference = sales_after - sales_before
    percentage_change = (difference / sales_before) * 100 if sales_before > 0 else 0

    # Write to file for safe reading
    with open('analysis_output.txt', 'w', encoding='utf-8') as f:
        f.write("--- Sales Analysis Report ---\n")
        f.write(f"Price Increase Date: {cutoff_date.date()}\n")
        f.write("-" * 30 + "\n")
        f.write(f"Total Sales BEFORE price increase: ${sales_before:,.2f}\n")
        f.write(f"Total Sales AFTER  price increase: ${sales_after:,.2f}\n")
        f.write("-" * 30 + "\n")
        
        if sales_after > sales_before:
            f.write(f"Conclusion: Sales were HIGHER after the price increase.\n")
            f.write(f"Increase: ${difference:,.2f} (+{percentage_change:.2f}%)\n")
        elif sales_after < sales_before:
            f.write(f"Conclusion: Sales were LOWER after the price increase.\n")
            f.write(f"Decrease: ${abs(difference):,.2f} ({percentage_change:.2f}%)\n")
        else:
            f.write("Conclusion: Sales were EXACTLY THE SAME.\n")
            
        f.write("\n(Note: This simple comparison of totals works best if the time periods are roughly equal length.\n")
        f.write(f" Days Before: {days_before}, Days After: {days_after})\n")
        f.write(f" Avg Daily Sales Before: ${avg_sales_before:,.2f}\n")
        f.write(f" Avg Daily Sales After:  ${avg_sales_after:,.2f}\n")
    
    # Also print to stdout
    print(open('analysis_output.txt', 'r', encoding='utf-8').read())

if __name__ == "__main__":
    analyze_sales_impact()
