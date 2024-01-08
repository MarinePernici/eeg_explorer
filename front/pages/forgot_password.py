import dash_bootstrap_components as dbc
from dash import html, dcc
from pages.title import title_container


forgot_password_layout = html.Div([
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
                        html.P("Pour réinitialiser votre mot de passe, veuillez renseigner votre adresse email de connexion."),
                        ], style={'text-align': 'justify'},
                    ),
                    width={"size": 6, "offset": 3, },
                    className="text-center"
                )
            ),
            dbc.Row(
                [
                    dbc.Col([
                        dbc.Input(id='user-email', type='email', placeholder='Adresse email de connexion', value=""),
                        dbc.FormFeedback("Email valide", type="valid", id='user-email-valid'),
                        dbc.FormFeedback("Email non reconnu", type="invalid", id='user-email-invalid'),
                    ],
                    width={"size": 6, "offset": 3, },
                    ),
                ],
                className="mb-3",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Button("Réinitialiser mon mot de passe", disabled=True, id='forgot-password-button', color="primary", n_clicks=0, style={'width': "100%"},),
                        width={"size": 3, "offset": 6, },
                    ),
                ],
                className="mb-3",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(id='forgot-password-message', style={'text-align': 'end'}),
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
