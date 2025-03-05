import pandas as pd
from dash import Dash, dcc, html

data = pd.read_csv("geberit.csv", parse_dates=['time'])

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(data)

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="", className="header-emoji"),
                html.H1(
                    children="MAP-2 Analytics",
                    className="header-title",
                ),
                html.P(
                    children=(
                        "Analyze the behavior of temperature and humidity sensors"
                        " installed at MAP-2 in SLavuta"
                    ),
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["time"],
                                    "y": data["15-2 / Humidity"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}%<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Humidity",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
                    className="card",
                ),

                # ...

            ],
            className="wrapper",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["time"],
                                    "y": data["15-2 / Temperature"],
                                    "type": "lines",
                                    "hovertemplate": (
                                        "%{y:.2f}°<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Temperature",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
                    className="card",
                ),

                # ...

            ],
            className="wrapper",
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)

# app = Dash(__name__)