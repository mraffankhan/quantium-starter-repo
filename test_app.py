from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict
import dash
from app import app, update_charts

def test_layout_is_not_empty():
    """Simple smoke test to ensure layout is defined."""
    assert app.layout is not None
    assert isinstance(app.layout, dash.html.Div)

def test_callback_chart_updates():
    """Test that the callback returns figures."""
    # Mock inputs
    selected_region = 'all'
    
    # Run callback
    # We can invoke the python function directly for unit testing logic
    output = update_charts(selected_region)
    
    # Expect 2 outputs (Line Chart, Bar Chart)
    assert len(output) == 2
    
    line_chart = output[0]
    bar_chart = output[1]
    
    # Check that they are plotly figures (dictionaries or objects)
    # Dash callbacks return Figure objects usually when using px
    assert line_chart is not None
    assert bar_chart is not None
    
    # Check titles to verify correct filtering logic
    assert 'All Regions' in line_chart.layout.title.text

def test_callback_region_filtering():
    """Test callback with a specific region."""
    # Assuming 'East' or similar exists, but let's check generic logic 
    # relying on the function not crashing
    selected_region = 'Pink Morsel' # Wait, 'Pink Morsel' is a product, regions are 'north', 'east', etc. 
    # Valid regions from inspection: west, east, etc.
    # Let's try a dummy region that will return empty data but shouldn't crash
    selected_region = 'north'
    
    output = update_charts(selected_region)
    assert len(output) == 2
    
    line_chart = output[0]
    assert 'North' in line_chart.layout.title.text

if __name__ == "__main__":
    # verification script style
    try:
        test_layout_is_not_empty()
        print("test_layout_is_not_empty: PASS")
        
        test_callback_chart_updates()
        print("test_callback_chart_updates: PASS")
        
        test_callback_region_filtering()
        print("test_callback_region_filtering: PASS")
        
        print("\nAll basic smoke tests passed.")
    except AssertionError as e:
        print(f"Test Failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
