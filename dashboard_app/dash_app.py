from django_plotly_dash import DjangoDash
from dash import dcc
from dash import Dash, html
import plotly.graph_objects as go

app = DjangoDash("SimpleDashApp")


# Example data for plotting
x_data = [1, 2, 3, 4, 5]
y_data = [10, 15, 13, 17, 14]

app.layout = html.Div([
    html.H1("Dashboard"),
    dcc.Graph(
        id='example-graph',
        figure=go.Figure(
            data=[
                go.Scatter(x=x_data, y=y_data, mode='lines+markers', name='Sample Line')
            ],
            layout=go.Layout(
                title='Simple Line Plot',
                xaxis_title='X Axis',
                yaxis_title='Y Axis'
            )
        )
    )
])