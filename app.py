import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# 1. Load the processed dataset
data_path = 'data/processed_sales.csv'
try:
    df = pd.read_csv(data_path)
    # 2. Convert Date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    # 3. Sort by Date
    df = df.sort_values('Date')
except FileNotFoundError:
    print(f"Error: {data_path} not found. Please run process_sales.py first.")
    # Create empty dataframe to prevent crash
    df = pd.DataFrame(columns=['Sales', 'Date', 'Region'])

# Initialize the Dash app
app = dash.Dash(__name__)

# --- Create Visualizations ---
# Aggregate sales by date to show clear daily trend
daily_sales = df.groupby('Date')[['Sales']].sum().reset_index()

# Create Line Chart
# We can also add a color breakdown by Region if desired, but "No additional filtering" 
# and "simple/clean" suggests focusing on the main question first. 
# However, splitting by region is standard practice. Let's make the main chart the total sales.
fig_line = px.line(
    daily_sales, 
    x='Date', 
    y='Sales', 
    title='Pink Morsel: Daily Sales Over Time',
    labels={'Sales': 'Total Sales ($)', 'Date': 'Date'}
)

# Optional: Add a vertical line for the price increase date (15 Jan 2021)
fig_line.add_vline(x=pd.Timestamp('2021-01-15').timestamp() * 1000, line_width=2, line_dash="dash", line_color="red", annotation_text="Price Increase")

# Define Layout
app.layout = html.Div([
    # Header
    html.Header([
        html.H1("Pink Morsel Sales Analysis", style={'textAlign': 'center', 'color': '#2c3e50'}),
        html.P("Visualising the impact of the price increase on 15th January 2021.", 
               style={'textAlign': 'center', 'fontSize': '18px', 'marginBottom': '30px'})
    ]),

    # Visualizations
    html.Div([
        dcc.Graph(
            id='sales-trend-line',
            figure=fig_line
        ) 
    ], style={'maxWidth': '1200px', 'margin': '0 auto'})

], style={'fontFamily': 'Arial, sans-serif', 'padding': '20px'})

if __name__ == '__main__':
    app.run(debug=True)
