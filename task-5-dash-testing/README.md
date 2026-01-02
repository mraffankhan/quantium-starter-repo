# Task 5: Dash App Testing

## Purpose
This task establishes a testing framework to verify that the improved Dash application (from Task 4) functions correctly. It ensures component presence without modifying the original application code.

## Test Suite
The tests use `pytest` and `dash.testing` to launch the application in a headless browser and assert that key UI elements are loaded.

**Tests Implemented:**
1.  **Header Presence**: Confirms the H1 title is rendered.
2.  **Visualization Presence**: Confirms the Graph component (`#sales-line-chart`) is rendered.
3.  **Region Picker Presence**: Confirms the RadioItems component (`#region-filter`) is rendered.

## How to Run Tests
1.  Ensure you have the necessary testing libraries installed:
    ```bash
    pip install pytest dash[testing]
    ```
2.  Navigate to this directory:
    ```bash
    cd task-5-dash-testing
    ```
3.  Run `pytest`:
    ```bash
    pytest
    ```

**Note**: These tests require a WebDriver (e.g., ChromeDriver for Google Chrome) to be installed and available in your system PATH. If you encounter errors related to "browser not found" or "connection refused", please ensure you have a valid WebDriver installed.
