import dash_bootstrap_components as dbc
from dash import html, dcc
from front.pages.title import title_container

profile_history_layout=html.Div([
    dbc.Container(
        [
            *title_container,
            dbc.Row(
                dbc.Col(
                    html.Div([
                        html.Div(id="dynamic-username", style={'fontSize': '1.5rem'}),  # Contenu dynamique
                        html.P("Sur cette page, vous pouvez accéder à l'ensemble de votre historique : les questions que vous avez posées et les réponses obtenues sont classées de la plus ancienne à la plus récente."),
                        html.P("En bas de page, vous pouvez choisir de télécharger votre historique dans un fichier Excel ou CSV."),
                        ], style={'text-align': 'justify'},
                    ),
                    width={"size": 10, "offset": 1, },
                    className="center"
                )
            ),
            dbc.Row(
                dcc.Loading(
                    dbc.Col(
                        dbc.Table(
                            [
                                # Table header
                                html.Thead(
                                    html.Tr(
                                        [
                                            html.Th("Date"),
                                            html.Th("Requête"),
                                            html.Th("Réponse"),
                                        ],
                                    ),
                                ),
                                # Table body
                                html.Tbody(id='history-table'),
                            ],
                            bordered=True,
                            color="secondary",
                            hover=True,
                            responsive=True,
                            striped=True,
                        ),
                        width={"size": 10, "offset": 1, },
                    ),
                    type="circle",    
                ),
            ),
            dbc.Row(
                dbc.Col([
                    dbc.Label("Choisissez le format dans lequel vous voulez télécharger votre historique :", style={'textAlign': 'justify'}),
                    dbc.RadioItems(
                        id='format-select',
                        options=[
                            {'label': 'Excel', 'value': 'xlsx'},
                            {'label': 'CSV', 'value': 'csv'},
                        ],
                        # value='xlsx',  # Valeur par défaut
                        style={'marginBottom': '10px', 'textAlign': 'center'},
                        inline=True,
                        label_style={"marginRight": "10px"},
                    ),

                    # Bouton de téléchargement
                    dbc.Button('Télécharger mon historique', id='download-button', style={'width': '50%'}, n_clicks=0, disabled=True),

                    # Composant dcc.Download pour le téléchargement du fichier
                    dcc.Download(id='download-data')
                ], width={"size": 6, "offset": 3, }, className="text-center"),
            ),
        ],
        fluid=True,
        className="py-3"
    )
])