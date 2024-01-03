
import dash_bootstrap_components as dbc
from dash import dcc, html
from front.layouts.title import title_container


login_layout = html.Div([
    dbc.Container(
        [
            dbc.Row(
                dbc.Col(
                    title_container, 
                    width={"size": 8, "offset": 2},
                ),
            ),
            dbc.Row([
                dbc.Col(
                    html.H2("Se connecter", style={'marginTop': 'auto'}),
                    width={"size": 5, "offset": 1},
                ),
                dbc.Col(
                    html.H2("Créer un Compte", style={'textAlign': 'center'}),
                    width={"size": 5, "offset": 0},
                ),
            ]),
            dbc.Row([
                dbc.Col(
                    html.P("Si vous avez déjà un compte utilisateur, veuillez vous connecter ici."),
                    width={"size": 5, "offset": 1},
                ),
                dbc.Col(
                    html.P("Si vous n'avez pas encore de compte utilisateur, veuillez en créer un ici*."),
                    width={"size": 5, "offset": 0},
                ),
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Input(id='login-email', type='email', placeholder='Adresse email'),
                    dbc.FormFeedback("Email valide", type="valid", id='login-email-valid'),
                    dbc.FormFeedback("Email non reconnu", type="invalid", id='login-email-invalid'),
                    html.Br(),
                    dbc.Input(id='login-password', type='password', placeholder='Mot de passe'),
                ], width={"size": 5, "offset": 1},),
                dbc.Col([
                    dbc.Input(id='signup-name', type='text', placeholder="Nom d'utilisateur", value=""),
                    dbc.FormFeedback("Ce nom d'utilisateur est accepté.", type="valid"),
                    dbc.FormFeedback("Ce nom d'utilisateur est déjà utilisé. Veuillez en choisir un autre.", type="invalid"),
                    html.Br(),
                    dbc.Input(id='signup-email', type='email', placeholder='Adresse email'),
                    dbc.FormFeedback("", type="valid", id='email-feedback-valid'),
                    dbc.FormFeedback("", type="invalid", id='email-feedback-invalid'),
                    html.Br(),
                    dbc.Input(id='signup-password', type='password', placeholder='Mot de Passe'),
                    dbc.FormFeedback("", type="valid", id='password-feedback-valid'),
                    dbc.FormFeedback("", type="invalid", id='password-feedback-invalid'),
                    dbc.FormText("Mot de passe : 12 caractères dont 1 minuscule, 1 majuscule, 1 chiffre et un caractère spécial", id='password-feedback', color='info'),
                ], width={"size": 5, "offset": 0},),
            ]),
            dbc.Row([
                dbc.Col(
                    dbc.Button('Se connecter', n_clicks=0, id='login-button', color='info', disabled=True, style={'marginBottom': 'auto'}),
                    width={"size": 5, "offset": 1},
                ),
                dbc.Col(
                    dbc.Button("Créer le compte", id='signup-button', color='info', disabled=True, ),
                    width={"size": 5, "offset": 0},
                ),
            ]),
            dbc.Row([
                dbc.Col(
                    html.Div(id='login-status'),
                    width={"size": 5, "offset": 1},
                ),
                dbc.Col(
                    html.Div(id='signup-status', children=[
                        "* La création de compte est ouverte aux membres de Spectre Biotech, pour plus d'informations, veuillez ",
                        html.A(
                            "contacter le support.",
                            href="/contact",
                            target="_blank",
                        ),
                    ], style={'marginBottom': 'auto', 'marginTop': '10px'}),
                    width={"size": 5, "offset": 0},
                ),
            ]),
            dbc.Row(
                dbc.Col(
                    html.A("Mot de passe oublié ?", href="/forgot-password", target="_blank", style={'marginLeft': 'auto'}),
                    width={"size": 5, "offset": 1},
                ),
            ),
        ],
        fluid=True,
        className="py-3 px-5",
        id="login-card-container",
        style={'display': 'block'},
    ),
    dbc.Container(
        [
            dbc.Row(
                dbc.Col(
                    title_container, 
                    width={"size": 8, "offset": 2},
                ),
            ),
            dbc.Row([
                dbc.Col(
                    html.Div(id="dynamic-username", style={'fontSize': '1.5rem'}),
                    width={"size": 6, "offset": 3},
                ),
            ]),
            dbc.Row([
                dbc.Col(
                    html.P("Commencez votre exploration :"),
                    width={"size": 4, "offset": 3},
                ),
                dbc.Col(
                    dbc.Button('Explorer', href='/explorer'),
                    width={"size": 2, "offset": 0},
                ),
            ]),
            dbc.Row([
                dbc.Col([
                    html.P("Consultez ou modifiez votre profil :"),
                ], width={"size": 4, "offset": 3},),
                dbc.Col([
                    dbc.Button('Profil', href='/profile'),
                ], width={"size": 2, "offset": 0},),
            ]),
            dbc.Row([
                dbc.Col(
                    html.P("Pour vous déconnectez :"),
                    width={"size": 4, "offset": 3},
                ),
                dbc.Col(
                    dbc.Button('Se déconnecter', n_clicks=0, id='logout-button', href="/home", style={'marginBottom': 'auto'}),
                    width={"size": 4, "offset": 2},
                ),
            ]),
            dbc.Row([
                dbc.Col(
                    html.Div(id='logout-content'),
                    width={"size": 6, "offset": 3},
                ),
            ]),
        ],
        fluid=True,
        className="py-3",
        id="login-card-container-logged",
        style={'display': 'none'},
    ),
])