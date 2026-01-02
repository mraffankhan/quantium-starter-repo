# Quantium Data Analytics Virtual Experience

## Project Overview
This repository contains the completed tasks for the Quantium Data Analytics Virtual Experience. The project demonstrates the setup of a Python development environment, data processing pipelines, and the creation of a responsive Dash application to analyze sales trends.

## Project Structure
The project is organized into three specific tasks, each in its own directory:

### [Task 1: Environment Setup](./task-1-environment-setup)
**Directory**: `task-1-environment-setup/`
A minimal verification setup to ensure that Python, Dash, and Pandas are correctly installed and running.
-   Run `app.py` here to verify your local environment.

### [Task 2: Data Processing](./task-2-data-processing)
**Directory**: `task-2-data-processing/`
Contains the data ingestion and processing logic.
-   **Script**: `process_data.py` reads raw CSVs from `data/`, cleans the data, filters for "Pink Morsel", and exports it.
-   **Output**: `processed_sales.csv`.

### [Task 3: Dash Application](./task-3-dash-app)
**Directory**: `task-3-dash-app/`
The final analytical web application.
-   **App**: `app.py` loads the processed data and visualizes the sales trend.
-   **Goal**: To determine if sales were higher before or after the price increase on 15 Jan 2021.

## How to Navigate
1.  **Setup**: Start with Task 1 to confirm your tools are ready.
2.  **Process**: Run Task 2 to generate the clean dataset.
3.  **Visualize**: Run Task 3 to view the dashboard and insights.
