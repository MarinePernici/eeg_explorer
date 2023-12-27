import dash_bootstrap_components as dbc
from dash import html, dcc
from pages.title import title_container
from strgen import StringGenerator

profile_layout = html.Div([
    dbc.Container(
        [
            dbc.Row(
                dbc.Col(
                    title_container, width={"size": 6, "offset": 3},
                ),
            ),
            dbc.Row(
                dbc.Col(
                    html.Div([
                        html.Div(id="dynamic-username", style={'fontSize':'1.5rem'}),  # Contenu dynamique
                        # html.P("Ceci est la page de profil de notre application."),
                        
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
                dbc.Col([
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
                ], width={"size": 3, "offset": 0, },
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

profile_edit_layout = html.Div([
    dbc.Container(
        [
            dbc.Row(
                dbc.Col(
                    title_container, width={"size": 6, "offset": 3},
                ),
            ),
            dbc.Row(
                dbc.Col(
                    html.Div([
                        html.Div(id="dynamic-username"),  # Contenu dynamique
                        html.P("Vous pouvez modifier vos coordonnées ici :"),
                        ], style={'text-align': 'justify'},
                    ),
                    width={"size": 8, "offset": 2, },
                    className="text-center"
                )
            ),
            dbc.Row(
                [
                    dbc.Col(
                        html.P(id='profile-username',),
                        width={"size": 3, "offset": 2, },
                    ),
                    dbc.Col(
                        dbc.Input(id='new-username', type='text', placeholder="Mon nouveau nom d'utilisateur", value=""),
                        width={"size": 3, "offset": 0, },
                    ),
                    dbc.Col(
                        dbc.Button("Modifier", id='edit-username-button', color="primary", n_clicks=0, style={'width': "100%"},),
                        width={"size": 2, "offset": 0, },
                    ),
                    dbc.Col(
                        html.Div(id='username-change-status'),
                        width={"size": 2, "offset": 0, },
                    ),
                ],
                className="mb-3",
            ),
            # Ligne pour l'email
            dbc.Row(
                [
                    dbc.Col(
                        html.P(id='profile-email'),
                        width={"size": 3, "offset": 2, },
                    ),
                    dbc.Col(
                        dbc.Input(id='new-email', type='email', placeholder='Ma nouvelle adresse email', value=""),
                        width=3,
                    ),
                    dbc.Col(
                        dbc.Button(
                            "Modifier",
                            id='edit-email-button',
                            color="primary",
                            n_clicks=0,
                            style={'width': "100%"},
                            ),
                        width=2,
                    ),
                    dbc.Col(
                        html.Div(id='email-change-status'),
                        width=2,
                    ),
                ],
                # justify="center",
                className="mb-3",
            ),
            # Ligne pour le mot de passe
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Input(placeholder="Pour modifier votre mot de passe vous devrez entrer votre mot de passe actuel", type="password", disabled=True),
                        width={"size": 6, "offset": 2, },
                    ),
                    dbc.Col(
                        dbc.Button("Modifier", color="primary", href="/profile/edit/password", style={'width': "100%"},),
                        width=2,
                    )
                ],
                className="mb-3",
            ),
        ],
        fluid=True,
        className="py-3"
    )
])

profile_edit_password_layout = html.Div([
    dbc.Container(
        [
            dbc.Row(
                dbc.Col(
                    title_container, width={"size": 6, "offset": 3},
                ),
            ),
            dbc.Row(
                dbc.Col(
                    html.Div([
                        html.Div(id="dynamic-username"),
                        html.P("Ceci est la page de modification du mot de passe."),
                        ], style={'text-align': 'justify'},
                    ),
                    width={"size": 6, "offset": 3, },
                    className="text-center"
                )
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Input(id='old-password', type='password', placeholder='Ancien mot de passe', value=""),
                        width={"size": 6, "offset": 3, },
                    ),
                ],
                className="mb-3",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Input(id='new-password', type='password', placeholder='Nouveau mot de passe', value=""),
                            dbc.FormFeedback("", type="valid", id='new-password-feedback-valid'),
                            dbc.FormFeedback("", type="invalid", id='new-password-feedback-invalid'),
                            dbc.FormText("Mot de passe sécurisé: 12 caractères dont 1 minuscule, 1 majuscule, 1 chiffre et un caractère spécial", id='new-password-feedback', color='info'),
                        ], width={"size": 6, "offset": 3, },
                    ),
                ],
                className="mb-3",
            ),
            dbc.Row(
                [
                    dbc.Col([
                        dbc.Input(id='confirm-new-password', type='password', placeholder='Confirmer le nouveau mot de passe', value=""),
                        dbc.FormFeedback("", type="valid", id='confirm-new-password-feedback-valid'),
                        dbc.FormFeedback("", type="invalid", id='confirm-new-password-feedback-invalid'),
                    ], width={"size": 6, "offset": 3, },
                    ),
                ],
                className="mb-3",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Button("Modifier", id='edit-password-button', color="primary", n_clicks=0, style={'width': "100%"},),
                        width={"size": 2, "offset": 5, },
                    ),
                ],
                className="mb-3",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(id='password-change-status', style={'text-align': 'center'}),
                        width={"size": 4, "offset": 4},
                    ),
                ],
                className="mb-3",
            ),
        ],
        fluid=True,
        className="py-3"
    )
])


profile_delete_account_layout = html.Div([
    dbc.Container(
        [
            dbc.Row(
                dbc.Col(
                    title_container, width={"size": 6, "offset": 3},
                ),
            ),
            dbc.Row(
                dbc.Col(
                    html.Div([
                        html.Div(id="dynamic-username"),
                        html.P("Ceci est la page de suppression de votre compte."),
                        html.P("Une fois votre compte supprimé, vous ne pourrez plus vous connecter à l'application ni accéder à votre historique."),
                        ], style={'text-align': 'justify'},
                    ),
                    width={"size": 6, "offset": 3, },
                    className="text-center"
                )
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Input(id='delete-account-password', type='password', placeholder='Entrez votre mot de passe', value=""),
                        width={"size": 6, "offset": 3, },
                    ),
                ],
                className="mb-3",
            ),
            dbc.Row(
                [
                    dbc.Col([
                        html.P(StringGenerator("[\l\d]{12}").render_list(3)[0], id='delete-account-text-display'),
                        dbc.Input(id='delete-account-text', type='text', placeholder='Recopiez le texte ci-dessus pour supprimer votre compte', value=""),
                    ], width={"size": 6, "offset": 3, },),
                ],
                className="mb-3",
            ),
            dbc.Row(
                [
                dbc.Col([
                    html.Div(id='delete-confirm'),
                    dbc.Button(
                        "Supprimer mon compte",
                        size='lg',
                        color="danger",
                        className="btn btn-lg",
                        id="delete-account-button",
                        n_clicks=0,

                    ),
                ], width={"size": 4, "offset": 4, },
                className="text-center"
                ),
                ],
                className="mb-3",
            ),

        ],
        fluid=True,
        className="py-3"
    )
])
