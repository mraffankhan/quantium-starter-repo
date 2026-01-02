import sys
import os
import pytest
from dash.testing.application_runners import import_app
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup ChromeDriver automatically
# This ensures the test can run without manually adding chromedriver to PATH
os.environ['PATH'] += os.pathsep + os.path.dirname(ChromeDriverManager().install())

# Add the Task 4 directory to the system path so we can import the app
# Get the current directory of this test file
current_dir = os.path.dirname(os.path.abspath(__file__))
# Go up two levels (tests -> task-5 -> root) then down to task-4
task4_dir = os.path.join(current_dir, '..', '..', 'task-4-improved-dash-app')
sys.path.append(task4_dir)

# Change working directory so app can find the csv file
os.chdir(task4_dir)

from app import app

def test_001_header_exists(dash_duo):
    """
    Test 1: Verify the header is present and contains correct text.
    """
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("h1", "Pink Morsel Sales Analysis", timeout=10)
    
    # Assert that the header element exists
    header = dash_duo.find_element("h1")
    assert header is not None

def test_002_visualization_exists(dash_duo):
    """
    Test 2: Verify the visualization (Graph) is present.
    """
    dash_duo.start_server(app)
    # Dash graphs usually have an id. In app.py it is 'sales-line-chart'
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)
    
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

def test_003_region_picker_exists(dash_duo):
    """
    Test 3: Verify the region picker (RadioItems) is present.
    """
    dash_duo.start_server(app)
    # In app.py the id is 'region-filter'
    dash_duo.wait_for_element("#region-filter", timeout=10)
    
    radio = dash_duo.find_element("#region-filter")
    assert radio is not None
