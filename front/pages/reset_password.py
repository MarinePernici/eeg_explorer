import dash_bootstrap_components as dbc
from dash import html, dcc
from pages.title import title_container

reset_password_layout = html.Div([
    dbc.Container([
        dbc.Row(
            dbc.Col(title_container, width={"size": 6, "offset": 3})
        ),
        dbc.Row(
            dbc.Col(html.H2("Réinitialisation du Mot de Passe"), width={"size": 6, "offset": 3})
        , className="mb-3"),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Input(id='new-password-reset', type='password', placeholder='Nouveau mot de passe', value=""),
                        dbc.FormFeedback("", type="valid", id='new-password-reset-feedback-valid'),
                        dbc.FormFeedback("", type="invalid", id='new-password-reset-feedback-invalid'),
                        dbc.FormText("Mot de passe sécurisé: 12 caractères dont 1 minuscule, 1 majuscule, 1 chiffre et un caractère spécial", id='new-password-feedback', color='info'),
                    ], width={"size": 6, "offset": 3, },
                ),
            ],
            className="mb-3",
        ),
        dbc.Row(
            [
                dbc.Col([
                    dbc.Input(id='confirm-new-password-reset', type='password', placeholder='Confirmer le nouveau mot de passe', value=""),
                    dbc.FormFeedback("", type="valid", id='confirm-new-password-reset-feedback-valid'),
                    dbc.FormFeedback("", type="invalid", id='confirm-new-password-reset-feedback-invalid'),
                ], width={"size": 6, "offset": 3, },
                ),
            ],
            className="mb-3",
        ),
        dbc.Row(
            dbc.Col(dbc.Button("Réinitialiser", id='reset-password-button', color="primary", n_clicks=0), width={"size": 2, "offset": 5})
        , className="mb-3"),
        dbc.Row(
            dbc.Col(html.Div(id='reset-password-message'), width={"size": 6, "offset": 3})
        , className="mb-3",),
        # dcc.Location(id='url', refresh=False),  # Pour capturer et utiliser l'URL actuelle
    ],
    fluid=True,
    className="py-3"
    )
])