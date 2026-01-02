# Task 3: Sales Visualization Dashboard

## Purpose
This task involves creating a Dash web application to visualize the sales data and answer the business question.

## Business Question
**"Were sales higher before or after the Pink Morsel price increase on 15 January 2021?"**

## Visualization
The dashboard displays a **Line Chart** of daily sales over time.
-   **X-Axis**: Date
-   **Y-Axis**: Total Sales (Revenue)
-   **Annotation**: A vertical red dashed line marks the date of the price increase (15 Jan 2021).

## How it Answers the Question
By visually plotting the trend, we can observe the immediate and long-term impact of the price change on sales volume. The chart allows stakeholders to compare the level and stability of sales before versus after the intervention.

## How to Run
Ensure you are in the `task-3-dash-app` directory and that `processed_sales.csv` is present.
```bash
python app.py
```
Open the localhost link (e.g., `http://127.0.0.1:8050`) in your browser.
