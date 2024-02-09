import dash_bootstrap_components as dbc
from dash import html
from front.pages.title import title_container
from strgen import StringGenerator

profile_delete_account_layout = html.Div([
    dbc.Container(
        [
            *title_container,
            dbc.Row(
                dbc.Col(
                    html.Div([
                        html.Div(id="dynamic-username"),
                        html.P(
                            """Vous êtes ici sur la page de suppression de
                            votre compte. Une fois votre compte supprimé, vous 
                            ne pourrez
                            plus vous connecter à l'application ni accéder à
                            votre historique."""
                        ),
                        html.Br(),
                        ], style={'text-align': 'justify'},
                    ),
                    width={"size": 6, "offset": 3, },
                    className="text-center"
                )
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Input(
                            id='delete-account-password',
                            type='password',
                            placeholder='Entrez votre mot de passe',
                            value=""
                        ),
                        width={"size": 6, "offset": 3, },
                    ),
                ],
                className="mb-3",
            ),
            dbc.Row(
                [
                    dbc.Col([
                        html.P(
                            StringGenerator(r"[\l\d]{12}").render_list(3)[0],
                            id='delete-account-text-display'
                        ),
                        dbc.Input(
                            id='delete-account-text',
                            type='text',
                            placeholder="""Recopiez le texte ci-dessus pour
 supprimer votre compte""",
                            value=""
                        ),
                    ], width={"size": 6, "offset": 3, },),
                ],
                className="mb-3",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Button(
                                "Supprimer mon compte",
                                size='lg',
                                color="danger",
                                className="btn btn-lg mb-3",
                                id="delete-account-button",
                                n_clicks=0,

                            ),
                            html.Div(id='delete-confirm'),
                        ],
                        width={"size": 4, "offset": 4, },
                        className="text-center",
                    ),
                ],
                className="mb-3",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(children=[
                            """Lorsque vous supprimer votre compte, toutes vos
                            données personnelles (nom, email et mot de passe)
                            sont supprimés mais nous gardons les données
                            anonymisées de vos requêtes pour améliorer notre
                            application.""",
                            html.Br(),
                            """Si vous souhaitez supprimer toutes vos données,
                            veuillez nous en informer via le
                            """,
                            html.A(
                                "formulaire de contact",
                                href="/contact",
                                target="_blank",
                            ),
                            """ avant de supprimer votre compte."""
                        ]),
                        width={"size": 6, "offset": 3, },
                        style={'text-align': 'justify', 'font-size': 'small'},
                    ),
                ],
                # className="mb-3",
            ),
        ],
        fluid=True,
        className="py-3"
    )
])
