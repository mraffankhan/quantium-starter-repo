import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dash Environment Setup Verification"),
    html.P("This is a simple app to verify that Dash and the Python environment are working correctly.")
])

if __name__ == '__main__':
    app.run(debug=True)
