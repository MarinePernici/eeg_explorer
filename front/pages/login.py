
import dash_bootstrap_components as dbc
from dash import html
from front.pages.title import title_container


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
            id='signup-name', type='text', placeholder="Nom d'utilisateur",
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

user_layout = html.Div(
    dbc.Container(
        [
            *title_container,
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div(
                                id="dynamic-username",
                                style={'fontSize': '1.5rem'}
                            ),
                            html.P(
                                'Vous êtes maintenant connecté à votre '
                                'compte EEG Explorer!',
                                style={'fontSize': '1rem'}
                            ),
                        ], width={"size": 12, "offset": 0},
                        className="text-center",
                    ),
                ], className="mb-1"
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src="../assets/img/explore.png",
                                    top=True,
                                    style={
                                        'max-width': '100%',
                                        'border-radius': '25px'
                                    }
                                ),
                                dbc.CardBody(
                                    dbc.Button(
                                        "Commencer l'exploration",
                                        color="primary",
                                        href="/explorer",
                                        style={
                                            'width': '100%',
                                            'min-height': '60px',
                                            'display': 'flex',
                                            'align-items': 'center',
                                            'justify-content': 'center'
                                        }
                                    ),
                                    className='px-0',
                                ),
                            ], style={'border': 'none'},
                        ), width=10, md=5, lg=2,
                        className="text-center mb-2"
                    ),
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src="../assets/img/history.png",
                                    top=True,
                                    style={
                                        'max-width': '100%',
                                        'border-radius': '25px'
                                    }
                                ),
                                dbc.CardBody(
                                    dbc.Button(
                                        "Consulter mon historique",
                                        color="primary",
                                        href="/profile/history",
                                        style={
                                            'width': '100%',
                                            'min-height': '60px',
                                            'display': 'flex',
                                            'align-items': 'center',
                                            'justify-content': 'center'
                                        }
                                    ),
                                    className='px-0',
                                ),
                            ], style={'border': 'none'},
                        ), width=10, md=5, lg=2,
                        className="text-center mb-2"
                    ),
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src="../assets/img/edit.png",
                                    top=True,
                                    style={
                                        'width': '100%',
                                        'border-radius': '25px'
                                    }
                                ),
                                dbc.CardBody(
                                    dbc.Button(
                                        "Voir mon profil",
                                        id="edit-profile-button",
                                        color="primary",
                                        href="/profile/edit",
                                        style={
                                            'width': '100%',
                                            'min-height': '60px',
                                            'display': 'flex',
                                            'align-items': 'center',
                                            'justify-content': 'center'
                                        }
                                    ),
                                    className='px-0',
                                ),
                            ], style={'border': 'none',},
                        ), width=10, md=5, lg=2,
                        className="text-center mb-2"
                    ),
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardImg(
                                    src="../assets/img/logout.png",
                                    top=True,
                                    style={
                                        'max-width': '100%',
                                        'border-radius': '25px'
                                        }
                                    ),
                                dbc.CardBody(
                                    dbc.Button(
                                        "Se déconnecter",
                                        id="logout-button",
                                        n_clicks=0,
                                        color="primary",
                                        href="/home",
                                        disabled=False,
                                        style={
                                            'width': '100%',
                                            'min-height': '60px',
                                            'display': 'flex',
                                            'align-items': 'center',
                                            'justify-content': 'center'
                                        }
                                    ),
                                    className='px-0',
                                ),
                            ], style={'border': 'none'},
                        ), width=10, md=5, lg=2,
                        className="text-center mb-2"
                    ),
                ], justify="evenly",
            ),
            dbc.Row(
                dbc.Col(
                    html.Div(id='logout-content', hidden=True),
                    width={"size": 8, "offset": 2},
                ),
            ),
        ],
        fluid=True,
        className="py-3",
    )
)
