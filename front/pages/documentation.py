from dash import html
import dash_bootstrap_components as dbc
from pages.title import title_container


documentation_layout = html.Div([
    dbc.Container([
        *title_container,
        dbc.Row(
            dbc.Col([
                html.H2(
                    "Documentation de la base de données Spectre Biotech",
                    className="mb-3 text-start"
                ),
                html.P(
                    """Vous trouverez ci-dessous le schéma représentant les
                    différentes informations que vous pouvez trouver dans la
                    base de données de Spectre Biotech et leurs relations."""
                ),
            ], width=12
            )
        ),
        dbc.Row([
            dbc.Col([
                html.Img(
                    src="../assets/img/documentation.svg",
                    style={'width': '100%'},
                    className="my-3"
                ),
            ],)
        ],)
    ], fluid=True, className="py-3")
])
