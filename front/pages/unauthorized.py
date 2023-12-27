import dash_bootstrap_components as dbc
from dash import html, dcc
from pages.title import title_container

unauthorized_layout = html.Div([
    dbc.Container([
        title_container,
        html.H2("Accès Restreint", className="mt-5"),
        html.Br(),
        html.P("Vous devez être connecté pour accéder à cette page."),
        html.P("Retournez sur la page de connexion pour vous connecter ou créer un compte"),
        dbc.Button("Se connecter / Créer un compte", href="/login", color="primary", className="mt-3"),
    ], className="text-center mt-3")
])