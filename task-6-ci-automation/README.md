# Task 6: CI Automation

## Purpose
This task provides a Bash script to automate the execution of the Dash test suite. It is designed to be used in Continuous Integration (CI) pipelines or for local verification.

## Scripts
-   `run_tests.sh`: A script that:
    1.  Activates the Python virtual environment (`venv`).
    2.  Executes the pytest suite located in `task-5-dash-testing/`.
    3.  Returns exit code `0` on success and `1` on failure.

## Usage
### Local Execution
To run the automated test suite locally:

1.  Navigate to the `task-6-ci-automation` directory (or run from root):
    ```bash
    bash task-6-ci-automation/run_tests.sh
    ```
    *Note: Ensure you are running this in a Bash-compatible terminal (e.g., Git Bash on Windows, or standard terminal on Linux/macOS).*

### CI Pipeline
In a CI environment (e.g., GitHub Actions, Jenkins), configure your pipeline to run this script after dependencies are installed.

```yaml
# Example Step
- name: Run Dash Tests
  run: bash task-6-ci-automation/run_tests.sh
```
