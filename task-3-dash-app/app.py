import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# 1. Load the processed dataset
data_path = 'processed_sales.csv'
try:
    df = pd.read_csv(data_path)
    # 2. Convert Date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    # 3. Sort by Date
    df = df.sort_values('Date')
except FileNotFoundError:
    print(f"Error: {data_path} not found. Please run process_sales.py first.")
    df = pd.DataFrame(columns=['Sales', 'Date', 'Region'])

# Initialize the Dash app
app = dash.Dash(__name__)

# --- Create Visualization ---
# Aggregate sales by date
daily_sales = df.groupby('Date')[['Sales']].sum().reset_index()

fig_line = px.line(
    daily_sales, 
    x='Date', 
    y='Sales', 
    title='Pink Morsel: Daily Sales',
    labels={'Sales': 'Total Revenue ($)', 'Date': 'Date'}
)

# Define Layout (Basic)
app.layout = html.Div([
    html.Header([
        html.H1("Pink Morsel Sales Analysis"),
        html.P("Visualising the impact of the price increase.")
    ]),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig_line
    )
])

if __name__ == '__main__':
    app.run(debug=True)
