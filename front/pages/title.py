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
            # dbc.Col(
            #     html.H3(
            #         "by SPECTRE Biotech.",
            #         className="text-lg-start text-md-start text-center"
            #     ),
            #     width=12, lg=6, md=6,
            # ),
        ], justify="center", className="title-container",
    ),
    dbc.Row(
        dbc.Col(
            html.H4('Transformez vos questions en découvertes', className="text-center"),
            width=12,
        ), justify="center", className='text-primary mb-3 title-container',
    )
]
