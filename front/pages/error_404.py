from dash import html
import dash_bootstrap_components as dbc


error_404_layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Img(
                    src="../assets/img/error_404.png", style={'width': '100%'}
                ),
                html.H2("Perdu dans l'espace ?"),
                html.P(
                    "Il semblerait que vous ayez exploré une page qui " +
                    "n'existe pas ou plus. Utilisez le bouton ci-dessous " +
                    "pour revenir en lieu sûr."
                ),
                dbc.Button(
                    "Retour à l'accueil",
                    href='/home',
                    color="primary",
                    size="lg"
                ),
            ], width=12, lg=6, align="center", style={'textAlign': 'center'})
        ], justify="center", align="center", className="h-100")
    ], fluid=True, className="py-5")
])
