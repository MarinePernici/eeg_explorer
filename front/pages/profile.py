""" profile page layout"""

import dash_bootstrap_components as dbc
from dash import html
from pages.title import title_container

profile_layout = html.Div([
    dbc.Container(
        [
            title_container,
            dbc.Row(
                dbc.Col(
                    html.Div([
                        html.Div(
                            id="dynamic-username", style={'fontSize': '1.5rem'}
                        ),
                    ], style={'text-align': 'center'},
                    ),
                    width={"size": 12, "offset": 0, },
                    className="text-center"
                )
            ),
            dbc.Row([
                dbc.Col(
                    html.Img(
                        src="../assets/img/history.png",
                        style={
                            'max-width': '80%',
                            'max-height': '100%',
                            'border-radius': '25px',
                        },
                    ),
                    width={"size": 3, "offset": 0, },
                    className="text-center"
                ),
                dbc.Col(
                    html.Img(
                        src="../assets/img/edit.png",
                        style={
                            'max-width': '80%',
                            'max-height': '100%',
                            'border-radius': '25px',
                        },
                    ),
                    width={"size": 3, "offset": 0, },
                    className="text-center"
                ),
                dbc.Col(
                    html.Img(
                        src="../assets/img/logout.png",
                        style={
                            'max-width': '80%',
                            'max-height': '100%',
                            'border-radius': '25px',
                        },
                    ),
                    width={"size": 3, "offset": 0, },
                    className="text-center"
                ),
                dbc.Col(
                    html.Img(
                        src="../assets/img/delete.png",
                        style={
                            'max-width': '80%',
                            'max-height': '100%',
                            'border-radius': '25px',
                        },
                    ),
                    width={"size": 3, "offset": 0, },
                    className="text-center"
                ),
            ]),
            dbc.Row([
                dbc.Col(
                    dbc.Button(
                        "Consulter l'historique",
                        size='lg',
                        color="primary",
                        className="btn btn-lg",
                        href="/profile/history",
                        id="history-button",
                    ),
                    width={"size": 3, "offset": 0, },
                    className="text-center mt-3"
                ),
                dbc.Col(
                    dbc.Button(
                        "Modifier mon profil",
                        size='lg',
                        color="primary",
                        className="btn btn-lg",
                        href="/profile/edit",
                        id="edit-profile-button",
                    ),
                    width={"size": 3, "offset": 0, },
                    className="text-center mt-3"
                ),
                dbc.Col(
                    [
                        dbc.Button(
                            "Se déconnecter",
                            size='lg',
                            color="primary",
                            className="btn btn-lg",
                            href="/home",
                            id="logout-button",
                            n_clicks=0,
                        ),
                        html.Div(id='logout-content'),
                    ],
                    width={"size": 3, "offset": 0, },
                    className="text-center mt-3"
                ),
                dbc.Col(
                    dbc.Button(
                        "Supprimer mon compte",
                        size='lg',
                        color="primary",
                        className="btn btn-lg",
                        href="/profile/delete",
                        # id="delete-account-button",
                        # n_clicks=0,
                    ), width={"size": 3, "offset": 0, },
                    className="text-center mt-3"
                ),
            ]),
        ],
        fluid=True,
        className="py-3"
    )
])
