import csv
import pandas as pd
# import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Output, Input

with open("hw1/R1.csv") as file:
  line = csv.reader(file)
  head = next(line)
  data = []
  for row in line:
    data.append([row[0], row[1]])

x_data = []
y_data = []

# Initialize empty figure with one scatter trace
fig = go.Figure()
fig.add_scatter(
    x=list(x_data), y=list(y_data), mode="lines", name="Random Data"
)

app = dash.Dash("HW1")
app.layout = html.Div(
    [
        html.H1("Live Updating Plotly Graph"),
        dcc.Graph(id="live-graph", figure=fig),
        dcc.Interval(
            id="interval-component", interval=100, n_intervals=0  # 1000ms = 1 second
        ),
    ]
)
@app.callback(
    Output("live-graph", "figure"), Input("interval-component", "n_intervals")
)
def update_graph(n):
    # Append new data point
    tmp = data.pop(0)
    x_data.append(tmp[0])
    y_data.append(tmp[1])  # simulate new data
    # Create new figure with updated data
    fig = go.Figure()
    fig.add_scatter(
        x=list(x_data), y=list(y_data), mode="lines", name="Random Data"
    )
    fig.update_layout(xaxis_title="Time (s)", yaxis_title="Speed In Current Wobj")
    return fig


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
