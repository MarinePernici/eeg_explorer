""" Layout for the home page of the application."""

import dash_bootstrap_components as dbc
from dash import html, dcc
from pages.title import title_container

home_layout = html.Div([
    dbc.Container(
        [
            *title_container,
            dbc.Row([
                
                dbc.Col([
                    html.Div(
                        style={
                            'display': 'flex',  # Utiliser Flexbox
                            'align-items': 'center',  # Centrer verticalement
                            'justify-content': 'center',  # Centrer horizontalement
                            'background-color': '#1a1950',  # Fond coloré
                            'border-radius': '5px',  # Arrondir les coins
                            'height': '100%', # Hauteur 100%
                        },
                        children=html.Img(
                            src='../assets/img/logo.png',
                            style={
                                'max-width': '100%',
                                'max-height': '100%',
                                'border-radius': '5px',
                            },
                        ),
                    ),
                ], width=5, lg=3, md=3,
                className="mb-3 ms-3 d-flex flex-column justify-content-center ",
                style={'background-color': '#1a1950', 'border-radius': '5px',}
                ),
                dbc.Col(
                    html.Div(
                        dcc.Markdown("""
                            Découvrez **EEG Explorer**, une application permettant
                            d'explorer simplement des données EEG à l'aide de
                            questions en langage naturel.

                            - **Pourquoi EEG Explorer ?**

                            EEG Explorer a été développé comme prototype afin
                            d'expérimenter une interface permettant à des utilisateurs
                            non techniques d'interroger une base de données sans avoir
                            à écrire directement de requêtes SQL.

                            L'application utilise un modèle de langage pour transformer
                            les questions de l'utilisateur en requêtes SQL, interroger
                            une base PostgreSQL de démonstration contenant des données
                            EEG fictives, puis présenter les résultats à l'utilisateur.

                            - **Explorer les données**

                            Posez une question en langage naturel et EEG Explorer
                            se charge de la traduire en requête pour explorer les
                            données disponibles.
                        """,
                            className='custom-list-style'
                        ), style={'text-align': 'justify'},
                    ),
                    width=12, lg=7, md=7, 
                    className="mb-3 d-flex flex-column justify-content-center"
                )
            ], style={'vertical-align': 'middle'}, className="d-flex align-items-stretch", justify="center",),
            dbc.Row([
                dbc.Col(
                    dbc.Button(
                        "Commencer l'exploration",
                        size='lg',
                        color="primary",
                        className="btn btn-lg",
                        href="/explorer",
                        id="start-exploration-button",
                        style={'width': '100%'},
                    ), width=12, lg={'size': 3, 'offset': 8}, md={'size': 3, 'offset': 8}, className='d-flex align-items-center mb-3',
                ),
            ], 
            # justify="end"
            ),
        ],
        fluid=True,
        className="py-3"
    )
])
