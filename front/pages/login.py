
import dash_bootstrap_components as dbc
from dash import dcc, html
from pages.title import title_container


login_card = dbc.Card(
    [
        html.H2("Se connecter", style={'marginTop': 'auto'}),
        html.Br(),
        html.Br(),
        html.P("Si vous avez déjà un compte utilisateur, veuillez vous connecter ici."),
        dbc.Input(id='login-email', type='email', placeholder='Adresse email'),
        dbc.FormFeedback("Email valide", type="valid", id='login-email-valid'),
        dbc.FormFeedback("Email non reconnu", type="invalid", id='login-email-invalid'),
        html.Br(),
        dbc.Input(id='login-password', type='password', placeholder='Mot de passe'),
        html.Br(),
        html.Br(),
        dbc.Button('Se connecter', n_clicks=0, id='login-button', color='info', disabled=True, style={'marginBottom': 'auto'}),
        html.Div(id='login-status'),
    ], id="login-card", class_name="common-card-style", style={'display': 'flex'})


logged_card = dbc.Card([
                html.H2("Bienvenue"),
                html.Div(id="dynamic-username"),
                html.P("Commencer à explorer la base de données :"),
                dbc.Button('Explorer', href='/explorer'),
                html.Br(),
                html.P("Allez sur la page de profil :"),
                dbc.Button('Modifier mon profil', href='/profile'),
                html.Br(),
                html.P("Si vous voulez vous déconnecter, clickez ici:"),
                dbc.Button('Se déconnecter', n_clicks=0, id='logout-button', href="/login", style={'marginBottom': 'auto'}),
                html.Div(id='logout-content'),

        ], id="logged-card", class_name="common-card-style", style={'display': 'flex'})

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
    dbc.Button("Créer le compte", id='signup-button', color='info', disabled=True, style={'marginBottom': 'auto'}),
    html.Div(id='signup-status'),
], id="signup-card", class_name="common-card-style", style={'display': 'flex'})


login_layout_logout = html.Div(
    [
        login_card,
        signup_card
    ],
    style={'display': 'flex'},
    id="home-card-container", className="common-container-style"
)

login_layout_login = html.Div(
    [
        logged_card,
    ],
    style={'display': 'none'},
    id="home-card-container-logged", className="common-container-style"
)

information_container = html.Div(
    [
        # html.P("Bienvenue sur EEG Explorer."),
        html.Br(),
        html.P(
            children =[
                "* La création de compte est ouverte aux membres de Spectre Biotech, pour plus d'informations, veuillez ",
                html.A(
                    "contacter le support.",
                    href="/contact",
                    target="_blank",
                ),
            ],
        )
    ],
    id="information-container",
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
        dbc.Row(
            dbc.Col(
                login_layout_login, width={"size": 10, "offset": 1},
            ),
        ),
        dbc.Row(
            dbc.Col(
                information_container, width={"size": 10, "offset": 1},
            ),
        ),
    ],
    fluid=True,
    className="py-3"
    )
])