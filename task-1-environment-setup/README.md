# Task 1: Environment Setup Verification

## Purpose
This directory contains a minimal Dash application to verify that your local development environment is correctly configured.

## Environment Details
- **Python Version**: 3.9
- **Virtual Environment**: Recommended to isolate dependencies.

## Instructions
1.  **Install Dependencies**:
    Make sure you have `dash` and `pandas` installed (though this simple app only uses `dash`).
    ```bash
    pip install dash pandas plotly
    ```

2.  **Run the Verification App**:
    ```bash
    python app.py
    ```

3.  **Expected Output**:
    - The terminal should show that Dash is running.
    - Opening the provided localhost URL (usually `http://127.0.0.1:8050`) should display:
        - Header: "Dash Environment Setup Verification"
        - Text: "This is a simple app to verify that Dash and the Python environment are working correctly."

**Note**: This `app.py` does NOT load any data or visualizations. It is strictly for setup verification.
