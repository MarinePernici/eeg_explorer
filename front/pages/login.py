
import dash_bootstrap_components as dbc
from dash import dcc, html
from pages.title import title_container


login_card = dbc.Card(
    [
        html.H2("Se connecter", style={'marginTop': '0 auto'}),
        html.P("Si vous avez déjà un compte utilisateur, veuillez vous connecter ici.", className="text-justify"),
        html.Br(),
        dbc.Input(id='login-email', type='email', placeholder='Adresse email'),
        dbc.FormFeedback("Email valide", type="valid", id='login-email-valid'),
        dbc.FormFeedback("Email non reconnu", type="invalid", id='login-email-invalid'),
        html.Br(),
        dbc.Input(id='login-password', type='password', placeholder='Mot de passe'),
        html.Br(),
        html.Br(),
        dbc.Button('Se connecter', n_clicks=0, id='login-button', disabled=True, style={'marginBottom': 'auto'}),
        html.Div(id='login-status'),
        html.Br(),
        html.A("Mot de passe oublié ?", href="/forgot-password", target="_blank", style={'marginLeft': 'auto'}),
    ], id="login-card", class_name="common-card-style", style={'display': 'flex'})


logged_card = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                html.Div(id="dynamic-username", style={'fontSize': '1.5rem'}),
                html.P('Vous êtes maintenant connecté à votre compte EEG Explorer!', style={'fontSize': '1rem'}),
            ], width={"size": 8, "offset": 2}, className="text-center",
            ),
        ], className="mb-3"),
        dbc.Row([
            dbc.Col(
                html.P("Commencez votre exploration :"),
                width={"size": 5, "offset": 2},
            ),
            dbc.Col(
                dbc.Button('Explorer', href='/explorer', style={'width': '100%'}),
                width={"size": 3, "offset": 0},
            ),
        ], className="mb-3"),
        dbc.Row([
            dbc.Col([
                html.P("Consultez ou modifiez les informations de votre compte :"),
            ], width={"size": 5, "offset": 2},),
            dbc.Col([
                dbc.Button('Mon compte', href='/profile', style={'width': '100%'}),
            ], width={"size": 3, "offset": 0},),
        ], className="mb-3"),
        dbc.Row([
            dbc.Col(
                html.P("Si vous souhaitez vous déconnecter :"),
                width={"size": 5, "offset": 2},
            ),
            dbc.Col(
                dbc.Button('Se déconnecter', n_clicks=0, id='logout-button', style={'marginBottom': 'auto', 'width': '100%'}),
                width={"size": 3, "offset": 0},
            ),
        ], className="mb-3"),
        dbc.Row([
            dbc.Col(
                html.Div(id='logout-content'),
                width={"size": 8, "offset": 2},
            ),
        ]),
    ],
    fluid=True,
    className="py-3",
    id="logged-card",
    # style={'display': 'flex'},
)


signup_card = dbc.Card([
    html.H2("Créer un Compte", style={'textAlign': 'center'}),
    html.P("Si vous n'avez pas encore de compte utilisateur, veuillez en créer un ici*."),
    dbc.Input(id='signup-name', type='text', placeholder="Nom d'utilisateur", value=""),
    dbc.FormFeedback("", type="valid", id='username-feedback-valid'),
    dbc.FormFeedback("", type="invalid", id='username-feedback-invalid'),
    html.Br(),
    dbc.Input(id='signup-email', type='email', placeholder='Adresse email'),
    dbc.FormFeedback("", type="valid", id='email-feedback-valid'),
    dbc.FormFeedback("", type="invalid", id='email-feedback-invalid'),
    html.Br(),
    dbc.Input(id='signup-password', type='password', placeholder='Mot de Passe'),
    dbc.FormFeedback("", type="valid", id='password-feedback-valid'),
    dbc.FormFeedback("", type="invalid", id='password-feedback-invalid'),
    dbc.FormText("Mot de passe : 12 caractères dont 1 minuscule, 1 majuscule, 1 chiffre et un caractère spécial", id='password-feedback', color='info'),
    html.Br(),
    dbc.Button("Créer le compte", id='signup-button', disabled=True, ),
    html.Div(id='signup-status', children=[
        "* La création de compte est ouverte aux membres de Spectre Biotech, pour plus d'informations, veuillez ",
        html.A(
            "contacter le support.",
            href="/contact",
            target="_blank",
        ),
    ], style={'marginBottom': 'auto', 'marginTop': '10px'}),
], id="signup-card", class_name="common-card-style", style={'display': 'flex'})


login_layout_logout = html.Div(
    [
        login_card,
        signup_card
    ],
    style={'display': 'flex'},
    id="login-card-container", className="common-container-style"
)

login_layout_login = html.Div(
    [
        logged_card,
    ],
    style={'display': 'flex'},
    id="login-card-container-logged", className="common-container-style"
)

login_layout = html.Div([
    dbc.Container(
        [
            *title_container,
            dbc.Row(
                dbc.Col(
                    login_layout_logout, width={"size": 10, "offset": 1},
                ),
            ),
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