import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# Load the processed dataset
data_path = 'processed_sales.csv'
try:
    df = pd.read_csv(data_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
except FileNotFoundError:
    print(f"Error: {data_path} not found. Please ensure it exists in the current directory.")
    df = pd.DataFrame(columns=['Sales', 'Date', 'Region'])

# Initialize the Dash app
app = dash.Dash(__name__)

# Create Line Chart
# Aggregate sales by date
daily_sales = df.groupby('Date')[['Sales']].sum().reset_index()

fig_line = px.line(
    daily_sales, 
    x='Date', 
    y='Sales', 
    title='Pink Morsel Sales: Daily Trend',
    labels={'Sales': 'Total Revenue ($)', 'Date': 'Date'}
)

# Add vertical line for Price Increase (15 Jan 2021)
# Using numeric timestamp for compatibility
price_increase_date = pd.Timestamp('2021-01-15').timestamp() * 1000
fig_line.add_vline(
    x=price_increase_date, 
    line_width=2, 
    line_dash="dash", 
    line_color="red", 
    annotation_text="Price Increase"
)

# Layout
app.layout = html.Div([
    html.Header([
        html.H1("Pink Morsel Sales Analysis", style={'textAlign': 'center', 'color': '#333'}),
        html.P("Analysis of sales performance before and after the price increase on 15 Jan 2021.",
               style={'textAlign': 'center'})
    ]),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig_line
    )
], style={'fontFamily': 'sans-serif', 'maxWidth': '1000px', 'margin': '0 auto', 'padding': '20px'})

if __name__ == '__main__':
    app.run(debug=True)
