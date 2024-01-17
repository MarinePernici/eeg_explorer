import dash_bootstrap_components as dbc
from dash import html, dcc
from pages.title import title_container

rounded_border_style = {
    'border-radius': '15px',  # 15px est un exemple, ajustez selon vos besoins
    'overflow': 'hidden',
    'box-shadow': '3px 3px 10px rgba(0,0,0,0.2)',
    'background-color': '#1a1950',
    'margin-bottom': '10px',
}

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
                        html.Div(
                            id="dynamic-username", style={'fontSize': '1.5rem'}
                        ),  # Contenu dynamique
                        ], style={'text-align': 'justify'},
                    ),
                    width={"size": 10, "offset": 1, },
                    className="text-center"
                ), align="center",
            ),
            dbc.Row(
                dbc.Col(
                    dcc.Graph(
                        id='profile-graph',
                        figure={
                            'layout': {
                                'title': "Vous n'avez pas encore fait de requêtes"
                            }
                        },
                        config={
                            'displayModeBar': False
                        },
                    ),
                    width={"size": 10, "offset": 1, }, style=rounded_border_style,
                ),
            ),
            dbc.Row(
                dbc.Col(
                    html.Div([
                        html.Hr(),
                        html.P(
                            "C'est ici que vous pouvez consulter et/ou " +
                            "modifier vos coordonnées personnelles:"
                        ),
                        ], style={'text-align': 'justify'},
                    ),
                    width={"size": 10, "offset": 1, },
                    className="text-center"
                ), align="center", className="mb-3", style={'fontSize': '1.2rem', 'fontWeight': 'bold'},
            ),      
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(id='profile-username'),
                        width={"size": 4, "offset": 1, }, align="center",
                    ),
                    dbc.Col(
                        [
                            dbc.Input(
                                id='new-username',
                                type='text',
                                placeholder="Mon nouveau nom d'utilisateur",
                                value=""
                            ),
                            dbc.FormFeedback("", type="valid", id='new-username-feedback-valid', style={'fontSize': '0.7rem'}),
                            dbc.FormFeedback("", type="invalid", id='new-username-feedback-invalid', style={'fontSize': '0.7rem'}),
                        ], width={"size": 3, "offset": 0, },
                    ),
                    dbc.Col(
                        dbc.Button(
                            "Modifier mon nom",
                            id='edit-username-button',
                            color="primary",
                            n_clicks=0,
                            style={'width': "100%"},
                        ),
                        width={"size": 3, "offset": 0, },
                    ),
                    # dbc.Col(
                    #     html.Div(id='username-change-status'),
                    #     width={"size": 1, "offset": 0, },
                    # ),
                ],
                className="mb-3", align="center",
            ),
            dbc.Row(
                dbc.Col(
                    html.Div(id='username-change-status', style={'color': '#43ac6a'}),
                    width={"size": 10, "offset": 1, },
                ), id='username-change-margin',
            ),
            # Ligne pour l'email
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Input(placeholder="Pour modifier votre email vous devrez entrer votre mot de passe actuel", type="password", disabled=True),
                        width={"size": 7, "offset": 1, },
                    ),
                    dbc.Col(
                        dbc.Button("Modifier mon email", color="primary", href="/profile/edit/email", style={'width': "100%"},),
                        width=3,
                    )
                ],
                className="mb-3", align="center",
            ),
            # Ligne pour le mot de passe
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Input(placeholder="Pour modifier votre mot de passe vous devrez entrer votre mot de passe actuel", type="password", disabled=True),
                        width={"size": 7, "offset": 1, },
                    ),
                    dbc.Col(
                        dbc.Button("Modifier mon mot de passe", color="primary", href="/profile/edit/password", style={'width': "100%"},),
                        width=3,
                    )
                ],
                className="mb-3", align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Input(
                            placeholder="Si vous souhaitez supprimer votre compte veuillez vous diriger vers cette page",
                            type="text",
                            disabled=True
                        ),
                        width={"size": 7, "offset": 1, },
                    ),                    
                    dbc.Col(
                        dbc.Button(
                            "Supprimer mon compte",
                            color="danger",
                            href="/profile/delete",
                            style={'width': "100%"},
                        ),
                        width=3,
                    ),
                ],
                className="mb-3", align="center",
            ),
            # dbc.Row(
            #     dbc.Col(
            #         dcc.Graph(
            #             id='profile-graph',
            #             figure={
            #                 'layout': {
            #                     'title': "Vous n'avez pas encore fait de requêtes"
            #                 }
            #             }
            #         ),
            #         width={"size": 8, "offset": 2, },
            #     ),
            # ),
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
                        dbc.Button("Modifier", id='edit-password-button', disabled=True, color="primary", n_clicks=0, style={'width': "100%"},),
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


profile_edit_email_layout = html.Div([
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
                        html.P("Ceci est la page de modification de votre email."),
                        ], style={'text-align': 'justify'},
                    ),
                    width={"size": 6, "offset": 3, },
                    className="text-center"
                )
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Input(id='password', type='password', placeholder='Votre mot de passe', value=""),
                        width={"size": 6, "offset": 3, },
                    ),
                ],
                className="mb-3",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Input(id='new-email', type='email', placeholder='Votre nouvel email', value=""),
                            dbc.FormFeedback("", type="valid", id='new-email-feedback-valid'),
                            dbc.FormFeedback("", type="invalid", id='new-email-feedback-invalid'),
                        ], width={"size": 6, "offset": 3, },
                    ),
                ],
                className="mb-3",
            ),
            dbc.Row(
                [
                    dbc.Col([
                        dbc.Input(id='confirm-new-email', type='email', placeholder='Confirmer le nouvel email', value=""),
                        dbc.FormFeedback("", type="valid", id='confirm-new-email-feedback-valid'),
                        dbc.FormFeedback("", type="invalid", id='confirm-new-email-feedback-invalid'),
                    ], width={"size": 6, "offset": 3, },
                    ),
                ],
                className="mb-3",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Button("Modifier", id='edit-email-button', disabled=True, color="primary", n_clicks=0, style={'width': "100%"},),
                        width={"size": 2, "offset": 5, },
                    ),
                ],
                className="mb-3",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(id='email-change-status', style={'text-align': 'center'}),
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
