import dash
from dash import html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# --- Load Data ---
data_path = 'processed_sales.csv'
try:
    df = pd.read_csv(data_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
except FileNotFoundError:
    print(f"Error: {data_path} not found. Please ensure it exists in the current directory.")
    df = pd.DataFrame(columns=['Sales', 'Date', 'Region'])

# --- Styles ---
colors = {
    'background': '#f9f9f9',
    'text': '#2c3e50',
    'plot_bg': '#ffffff'
}

main_style = {
    'fontFamily': 'Segoe UI, Arial, sans-serif',
    'backgroundColor': colors['background'],
    'minHeight': '100vh',
    'padding': '40px'
}

header_style = {
    'textAlign': 'center',
    'color': colors['text'],
    'marginBottom': '30px'
}

card_style = {
    'backgroundColor': colors['plot_bg'],
    'borderRadius': '10px',
    'boxShadow': '0 4px 6px rgba(0,0,0,0.1)',
    'padding': '20px',
    'maxWidth': '1000px',
    'margin': '0 auto'
}

radio_style = {
    'display': 'flex',
    'justifyContent': 'center',
    'marginBottom': '20px',
    'fontSize': '18px'
}

# --- Initialize App ---
app = dash.Dash(__name__)

# --- Layout ---
app.layout = html.Div([
    
    # Header Section
    html.Header([
        html.H1("Pink Morsel Sales Analysis", style=header_style),
        html.P("Visualising the impact of the price increase on 15th January 2021.", 
               style={'textAlign': 'center', 'fontSize': '18px', 'marginBottom': '20px', 'color': '#555'})
    ], style=header_style),

    # Main Card Container
    html.Div([
        
        # Region Filter
        html.Div([
            html.Label("Select Region: ", style={'marginRight': '10px', 'fontWeight': 'bold'}),
            dcc.RadioItems(
                id='region-filter',
                options=[
                    {'label': 'All Regions', 'value': 'all'},
                    {'label': 'North', 'value': 'north'},
                    {'label': 'East', 'value': 'east'},
                    {'label': 'South', 'value': 'south'},
                    {'label': 'West', 'value': 'west'}
                ],
                value='all',
                labelStyle={'display': 'inline-block', 'marginRight': '15px', 'cursor': 'pointer'},
                inputStyle={'marginRight': '5px'}
            )
        ], style=radio_style),

        # Sales Chart
        dcc.Graph(id='sales-line-chart')

    ], style=card_style)

], style=main_style)


# --- Callbacks ---
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    # Filter data based on region
    if selected_region == 'all':
        filtered_df = df
        title_suffix = "All Regions"
    else:
        filtered_df = df[df['Region'] == selected_region]
        title_suffix = selected_region.title()

    # Aggregate sales by Date
    daily_sales = filtered_df.groupby('Date')[['Sales']].sum().reset_index()

    # Create Line Chart
    fig = px.line(
        daily_sales, 
        x='Date', 
        y='Sales', 
        title=f'Daily Sales Trend: {title_suffix}',
        labels={'Sales': 'Total Revenue ($)', 'Date': 'Date'}
    )

    # Styling the Chart
    fig.update_layout(
        plot_bgcolor=colors['plot_bg'],
        paper_bgcolor=colors['plot_bg'],
        font_color=colors['text'],
        title_font_size=24,
        hovermode="x unified"
    )

    # Add Price Increase Annotation (Vertical Line)
    price_increase_ts = pd.Timestamp('2021-01-15').timestamp() * 1000
    fig.add_vline(
        x=price_increase_ts, 
        line_width=2, 
        line_dash="dash", 
        line_color="#e74c3c", 
        annotation_text="Price Increase (15 Jan)", 
        annotation_position="top left"
    )

    return fig

if __name__ == '__main__':
    app.run(debug=True)
