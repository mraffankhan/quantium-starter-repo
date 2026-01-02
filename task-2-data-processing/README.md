# Task 2: Data Processing & Analysis

## Purpose
This task involves data ingestion, cleaning, and processing to prepare the dataset for analysis.

## Data Source
The raw data consists of multiple CSV files located in the `data/` directory.
Each row represents a transaction for Soul Foods.

## Processing Script (`process_data.py`)
The script performs the following operations:
1.  **Ingest**: Loads all CSV files from `data/`.
2.  **Filter**: Retains only rows where the product is "Pink Morsel".
3.  **Transform**: Creates a generic `Sales` column (`quantity` * `price`).
4.  **Clean**: Removes unnecessary characters (e.g., '$'), handles missing values, and fixes data types.
5.  **Output**: Selects `Sales`, `Date`, and `Region` columns, sorts by date, and exports to `processed_sales.csv`.

## Output
**File**: `processed_sales.csv`
**Columns**:
-   `Sales`: Total transaction value/revenue (Float)
-   `Date`: Date of transaction (YYYY-MM-DD)
-   `Region`: Region of the store (String)

## How to Run
Ensure you are in the `task-2-data-processing` directory:
```bash
python process_data.py
```
