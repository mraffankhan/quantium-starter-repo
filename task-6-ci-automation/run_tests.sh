#!/bin/bash

echo "Running test suite..."

# Get the directory where this script is located
SCRIPT_DIR=$(dirname "$0")

# Define root directory relative to the script
# If script is in task-6, root is one level up
PROJECT_ROOT="$SCRIPT_DIR/.."

# Define virtual environment path
# Check for Windows or Unix style venv
if [ -f "$PROJECT_ROOT/venv/Scripts/activate" ]; then
    VENV_ACTIVATE="$PROJECT_ROOT/venv/Scripts/activate"
elif [ -f "$PROJECT_ROOT/venv/bin/activate" ]; then
    VENV_ACTIVATE="$PROJECT_ROOT/venv/bin/activate"
else
    echo "Error: Virtual environment not found in $PROJECT_ROOT/venv"
    exit 1
fi

# Activate virtual environment
source "$VENV_ACTIVATE"

# Define test path
TEST_PATH="$PROJECT_ROOT/task-5-dash-testing/tests/test_app.py"

# Run tests
echo "Executing pytest on $TEST_PATH"
python -m pytest "$TEST_PATH"

# Capture exit code
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo "All tests passed"
    exit 0
else
    echo "Tests failed"
    exit 1
fi
