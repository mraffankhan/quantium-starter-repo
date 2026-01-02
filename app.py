import dash
from dash import html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# 1. Load the cleaned dataset
data_path = 'data/cleaned_sales_data.csv'
try:
    df = pd.read_csv(data_path)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
except FileNotFoundError:
    print(f"Error: {data_path} not found. Please run process_data.py first.")
    df = pd.DataFrame(columns=['product', 'price', 'quantity', 'date', 'region', 'sales'])

# Initialize the Dash app
app = dash.Dash(__name__)

# Get unique regions for the filter
regions = sorted(df['region'].unique().tolist())
region_options = [{'label': 'All Regions', 'value': 'all'}] + [{'label': r.title(), 'value': r} for r in regions]

# 2. Define the Layout
app.layout = html.Div([
    html.H1("Pink Morsel Sales Dashboard", style={'textAlign': 'center'}),
    html.P("This dashboard visualizes sales data for the 'Pink Morsel' product across different regions.", 
           style={'textAlign': 'center', 'marginBottom': '20px'}),

    html.Div([
        html.Label("Select Region:"),
        dcc.RadioItems(
            id='region-filter',
            options=region_options,
            value='all',
            inline=True,
            style={'marginBottom': '20px'}
        )
    ], style={'textAlign': 'center'}),

    dcc.Graph(id='sales-line-chart'),
    dcc.Graph(id='sales-bar-chart')
])

# 3. Define Callback to update charts
@app.callback(
    [Output('sales-line-chart', 'figure'),
     Output('sales-bar-chart', 'figure')],
    [Input('region-filter', 'value')]
)
def update_charts(selected_region):
    # Filter data based on selection
    if selected_region == 'all':
        filtered_df = df
        title_suffix = "All Regions"
    else:
        filtered_df = df[df['region'] == selected_region]
        title_suffix = selected_region.title()

    # --- Line Chart: Sales over Time ---
    # Aggregate sales by date
    daily_sales = filtered_df.groupby('date')[['sales']].sum().reset_index()
    
    fig_line = px.line(
        daily_sales, 
        x='date', 
        y='sales', 
        title=f'Daily Sales Over Time - {title_suffix}',
        labels={'sales': 'Total Sales ($)', 'date': 'Date'}
    )
    fig_line.update_layout(transition_duration=500)

    # --- Bar Chart: Sales by Product (or Store if available, but Product is safer from schema) ---
    # Since the request asked for "sales by category/store", and we only have 'product' (which might be just Pink Morsel?)
    # Let's check if there are multiple products. If only one, a bar chart by region (if 'All' selected) 
    # or by something else would be better.
    # However, to be safe and simple, let's stick to the schema we know. 
    # If filtered by region, maybe we can show sales by correct product if there are multiple, 
    # OR if there's only one product, maybe we show just a total bar?
    # Actually, inspecting the data via 'process_data.py' logs: 
    # "product" column exists. Let's assume there might be variations or we just chart it.
    # If the user filtered by a specific region, showing "Sales by Product" is fine.
    # If "All" is selected, we could show "Sales by Region" as the bar chart.
    
    if selected_region == 'all':
        # Show sales by Region
        bar_data = filtered_df.groupby('region')[['sales']].sum().reset_index()
        x_col = 'region'
        title_bar = 'Total Sales by Region'
    else:
        # Show sales by Product (even if it's just one, it works)
        bar_data = filtered_df.groupby('product')[['sales']].sum().reset_index()
        x_col = 'product'
        title_bar = f'Total Sales by Product - {title_suffix}'
        
    fig_bar = px.bar(
        bar_data, 
        x=x_col, 
        y='sales', 
        title=title_bar,
        labels={'sales': 'Total Sales ($)'}
    )

    return fig_line, fig_bar

if __name__ == '__main__':
    app.run(debug=True)
