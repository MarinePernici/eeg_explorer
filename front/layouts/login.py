
import dash_bootstrap_components as dbc
from dash import dcc, html
from front.layouts.title import title_container


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
        dbc.Button('Se connecter', n_clicks=0, id='login-button', color='info', disabled=True, style={'marginBottom': 'auto'}),
        html.Script("""
            document.getElementById('login-button').addEventListener('click', function() {
                var email = document.getElementById('login-email').value;
                var password = document.getElementById('login-password').value;
                fetch('/api/login', {
                    method: 'POST',
                    body: JSON.stringify({email: email, password: password}),
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                .then(response => response.json())
                .then(data => {
                    if (data.token) {
                        localStorage.setItem('auth_token', data.token);  // Stockage du token
                    }
                });
            });
        """),
        html.Div(id='login-status'),
        html.Br(),
        html.A("Mot de passe oublié ?", href="/forgot-password", target="_blank", style={'marginLeft': 'auto'}),
    ], id="login-card", class_name="common-card-style", style={'display': 'flex'})


# logged_card = dbc.Card([
#                 html.H2("Bienvenue"),
#                 html.Div(id="dynamic-username"),
#                 html.P("Commencer à explorer la base de données :"),
#                 dbc.Button('Explorer', href='/explorer'),
#                 html.Br(),
#                 html.P("Allez sur la page de profil :"),
#                 dbc.Button('Modifier mon profil', href='/profile'),
#                 html.Br(),
#                 html.P("Si vous voulez vous déconnecter, clickez ici:"),
#                 dbc.Button('Se déconnecter', n_clicks=0, id='logout-button', href="/home", style={'marginBottom': 'auto'}),
#                 html.Div(id='logout-content'),

#         ], id="logged-card", class_name="common-card-style", style={'display': 'flex'})

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
                html.P("Consultez ou modifiez votre les informations de votre compte :"),
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
                dbc.Button('Se déconnecter', n_clicks=0, id='logout-button', href="/home", style={'marginBottom': 'auto', 'width': '100%'}),
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
    html.Br(),
    dbc.Button("Créer le compte", id='signup-button', color='info', disabled=True, ),
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
            dbc.Row(
                dbc.Col(
                    title_container, width={"size": 8, "offset": 2},
                ),
            ),
            dbc.Row(
                dbc.Col(
                    login_layout_logout, width={"size": 10, "offset": 1},
                ),
            ),
            # dbc.Row(
            #     dbc.Col(
            #         login_layout_login, width={"size": 10, "offset": 1},
            #     ),
            # ),
        ],
        fluid=True,
        className="py-3"
    )
])

user_layout = html.Div([
    dbc.Container(
        [
            dbc.Row(
                dbc.Col(
                    title_container, width={"size": 8, "offset": 2},
                ),
            ),
            # dbc.Row(
            #     dbc.Col(
            #         login_layout_logout, width={"size": 10, "offset": 1},
            #     ),
            # ),
            dbc.Row(
                dbc.Col(
                    login_layout_login, width={"size": 10, "offset": 1},
                ),
            ),
        ],
        fluid=True,
        className="py-3"
    )
])
