from dash import html
import dash_bootstrap_components as dbc

title_container = [
    dbc.Row(
        [
            dbc.Col(
                html.H1(
                    "EEG Explorer ",
                    className="text-center"
                ),
                width=12,
            ),
        ], justify="center", id="title-container",
    ),
    dbc.Row(
        dbc.Col(
            html.H4('Transformez vos questions en découvertes', className="text-center"),
            width=12,
        ), justify="center", className='text-primary mb-3', id="title-container",
    )
]
