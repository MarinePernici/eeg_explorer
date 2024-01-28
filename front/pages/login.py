
import dash_bootstrap_components as dbc
from dash import html
from pages.title import title_container


login_card = dbc.Card(
    [
        html.H2("Se connecter"),
        html.Br(),
        html.Br(),
        html.P("Si vous avez déjà un compte utilisateur, veuillez vous connecter ici.", style={'marginRight': 'auto'}),
        dbc.Input(id='login-email', type='email', placeholder='Adresse email'),
        dbc.FormFeedback("Email valide", type="valid", id='login-email-valid'),
        dbc.FormFeedback("Email non reconnu", type="invalid", id='login-email-invalid'),
        html.Br(),
        dbc.Input(id='login-password', type='password', placeholder='Mot de passe'),
        html.Br(),
        dbc.Button('Se connecter', n_clicks=0, id='login-button', disabled=True, className="w-50 mb-auto"),
        html.Div(id='login-status', className="mt-2"),
        html.Br(),
        html.A("Mot de passe oublié ?", href="/forgot-password", target="_blank", style={'marginLeft': 'auto'}),
    ], id="login-card", class_name="common-card-style", style={'display': 'flex'}
)

signup_card = dbc.Card(
    [
        html.H2("Créer un Compte"),
        html.P(
            """Si vous n'avez pas encore de compte utilisateur, veuillez 
            en créer un ici*.""",
            className="me-auto"
        ),
        dbc.Input(
            id='signup-name', type='text', placeholder="Nom d'utilisateur"
        ),
        dbc.FormFeedback(type="valid", id='username-feedback-valid'),
        dbc.FormFeedback(type="invalid", id='username-feedback-invalid'),
        html.Br(),
        dbc.Input(
            id='signup-email', type='email', placeholder='Adresse email'
        ),
        dbc.FormFeedback(type="valid", id='email-feedback-valid'),
        dbc.FormFeedback(type="invalid", id='email-feedback-invalid'),
        html.Br(),
        dbc.Input(
            id='signup-password',
            type='password',
            placeholder='Mot de Passe'
        ),
        dbc.FormFeedback(type="valid", id='password-feedback-valid'),
        dbc.FormFeedback(type="invalid", id='password-feedback-invalid'),
        dbc.FormText(
            """Mot de passe : 12 caractères dont 1 minuscule, 1 majuscule,
            1 chiffre et un caractère spécial""",
            id='password-feedback',
            color='info',
            className="me-auto"),
        html.Br(),
        dbc.Button(
            "Créer le compte",
            id='signup-button',
            disabled=True,
            className="w-50"
        ),
        html.Div(
            id='signup-status',
            children=[
                """* La création de compte est ouverte aux membres de Spectre
                Biotech, pour plus d'informations, veuillez """,
                html.A(
                    "contacter le support.",
                    href="/contact",
                    target="_blank",
                ),
            ], className="mb-auto mt-2",
        ),
    ],
    class_name="common-card-style",
)

card_group = dbc.CardGroup(
    [
        signup_card,
        login_card,
    ]
)

login_layout_logout = dbc.Row(
    dbc.Col(card_group, width=12, lg=10),
    id="login-card-container",
    className="common-container-style",
    justify="center"
)


login_layout = html.Div([
    dbc.Container(
        [
            *title_container,
            login_layout_logout,
        ],
        fluid=True,
        className="py-3"
    )
])

user_layout = html.Div([
    dbc.Container(
        [
            *title_container,
            dbc.Row([
                dbc.Col([
                    html.Div(id="dynamic-username", style={'fontSize': '1.5rem'}),
                    html.P('Vous êtes maintenant connecté à votre compte EEG Explorer!', style={'fontSize': '1rem'}),
                ], width={"size": 8, "offset": 2}, className="text-center",
                ),
            ], className="mb-1"),
            dbc.Row([
                dbc.Col(
                    html.Img(
                        src="../assets/img/explore.png",
                        style={
                            'max-width': '80%',
                            'max-height': '100%',
                            'border-radius': '25px',
                        },
                    ),
                    width={"size": 2, "offset": 0, },
                    className="text-center"
                ),
                dbc.Col(
                    html.Img(
                        src="../assets/img/history.png",
                        style={
                            'max-width': '80%',
                            'max-height': '100%',
                            'border-radius': '25px',
                        },
                    ),
                    width={"size": 2, "offset": 0, },
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
                    width={"size": 2, "offset": 0, },
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
                    width={"size": 2, "offset": 0, },
                    className="text-center"
                ),
            ], justify="center"),
            dbc.Row([
                dbc.Col(
                    dbc.Button(
                        "Commencer l'exploration",
                        # size='lg',
                        color="primary",
                        # className="btn",
                        href="/explorer",
                        # id="delete-account-button",
                        # n_clicks=0,
                        style={
                            'max-width': '80%',
                            'max-height': '100%',
                        },
                    ), width={"size": 2, "offset": 0, },
                    className="text-center mt-3"
                ),
                dbc.Col(
                    dbc.Button(
                        "Consulter mon historique",
                        # size='lg',
                        color="primary",
                        # className="btn btn-lg",
                        href="/profile/history",
                        id="history-button",
                        style={
                            'max-width': '80%',
                            'max-height': '100%',
                        },
                    ),
                    width={"size": 2, "offset": 0, },
                    className="text-center mt-3"
                ),
                dbc.Col(
                    dbc.Button(
                        "Voir mon profil",
                        # size='lg',
                        color="primary",
                        # className="btn btn-lg",
                        href="/profile/edit",
                        id="edit-profile-button",
                        style={
                            'width': '80%',
                            'height': '100%',
                            'display': 'flex',
                            'align-items': 'center',
                            'justify-content': 'center',
                        },
                    ),
                    width={"size": 2, "offset": 0, },
                    className="d-flex justify-content-center mt-3",
                ),
                dbc.Col(
                    dbc.Button(
                        "Se déconnecter",
                        # size='lg',
                        color="primary",
                        # className="btn btn-lg",
                        href="/home",
                        id="logout-button",
                        n_clicks=0,
                        style={
                            'width': '80%',
                            'height': '100%',
                            'display': 'flex',
                            'align-items': 'center',
                            'justify-content': 'center',
                        },

                    ),
                    width={"size": 2, "offset": 0, },
                    className="d-flex justify-content-center mt-3",
                ),
            ], justify="center"),
            dbc.Row(
                dbc.Col(
                    html.Div(id='logout-content'),
                    width={"size": 8, "offset": 2},
                ),
            ),
        ],
        fluid=True,
        className="py-3"
    )
])