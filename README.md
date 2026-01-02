# Quantium Data Analytics Virtual Experience

## Project Overview
This project is part of the Quantium Data Analytics Virtual Experience. It involves setting up a local development environment, processing transaction data using Python, and conducting a simple analysis to answer a specific business question regarding sales performance.

The project demonstrates proficiency in:
- Python 3.9
- Data processing with Pandas
- Web application development with Dash
- Data analysis and cleaning

## Task 1: Local Development Environment Setup
The first phase of the project focuses on establishing a robust local development environment.

**Technologies Used:**
- **Python 3.9**: The core programming language.
- **Dash**: A framework for building analytical web applications.
- **Pandas**: A powerful library for data manipulation and analysis.

**Setup Steps:**
1.  **Clone Repository**: The starter repository was cloned to the local machine.
2.  **Environment Configuration**: A virtual environment was created to manage dependencies and isolate the project.
3.  **Dependency Installation**: Required packages (dash, pandas, plotly) were installed via `pip`.
4.  **Verification**: A basic Dash application (`app.py`) was created and executed to confirm that the environment is correctly configured and ready for further development.

## Task 2: Data Processing & Analysis (Soul Foods)
The second phase involves analyzing sales data for "Soul Foods" to address a strategic pricing question.

**Business Question:**
"Were sales higher before or after the Pink Morsel price increase on 15 January 2021?"

**Data Description:**
The raw data consists of three CSV files located in the `data/` directory. Each file contains transaction records with fields for product, price, quantity, date, and region.

**Data Processing Pipeline (`process_sales.py`):**
1.  **Combine Data**: Loaded and concatenated all daily sales CSV files into a single dataset.
2.  **Filter Product**: Filtered the dataset to include only transactions for the "Pink Morsel" product.
3.  **Feature Engineering**: Created a new `Sales` column by multiplying `quantity` by `price`.
4.  **Clean & Select**: Selected only the relevant columns (`Sales`, `Date`, `Region`), standardized column names, and sorted the records by date.
5.  **Export**: Saved the cleaned and processed data to `data/processed_sales.csv`.

**Analysis (`analyze_sales.py`):**
1.  **Segmentation**: Split the processed data into two periods:
    -   **Before**: Dates strictly before 15 January 2021.
    -   **After**: Dates on or after 15 January 2021.
2.  **Calculation**: Computed the total sales volume for each period.
3.  **Comparison**: Compared the totals to determine the impact of the price increase.

## How to Run the Project

1.  **Activate Environment**:
    Ensure your virtual environment is active.
    ```bash
    .\venv\Scripts\activate
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run Analysis**:
    Execute the analysis script to see the results.
    ```bash
    python analyze_sales.py
    ```

4.  **Run Dashboard (Optional)**:
    Launch the Dash application to visualize the data.
    ```bash
    python app.py
    ```

## Output
**Analysis Results**:
The `analyze_sales.py` script outputs a summary report to the terminal, detailing:
-   Total sales before the price increase.
-   Total sales after the price increase.
-   A conclusion stating whether sales increased or decreased.
-   Average daily sales figures for additional context.

**Data Artifacts**:
-   `data/processed_sales.csv`: The clean, filtered dataset used for analysis.
-   `data/cleaned_sales_data.csv`: A general cleaned dataset for the dashboard.
