from dash import html
import dash_bootstrap_components as dbc

title_container = dbc.Row(
    [
        dbc.Col(
            html.H1(
                "EEG Explorer ",
                className="text-lg-end text-md-end text-center"
            ),
            width=12, lg=6, md=6,
        ),
        dbc.Col(
            html.H3(
                "by Spectre Biotech",
                className="text-primary text-lg-start text-md-start text-center"
            ),
            width=12, lg=6, md=6,
        ),
    ], justify="center", className='mb-3', id="title-container"
)
