""" Callbacks for the login process"""

import dash
from dash import html
from dash.dependencies import Input, Output, State
from flask_login import login_user

from front.app import app
from back.api.auth import get_user_from_email
from front.functions.validity_functions import is_email_valid


# callback pour activer/désactiver le bouton de connexion
@app.callback(
    Output('login-button', 'disabled'),
    [Input('login-email', 'valid'), Input('login-password', 'value')]
)
def update_login_button_state(valid_email, password):
    if valid_email and password:  # Vérifie si les champs ne sont pas vides
        return False  # Active le bouton
    return True  # Désactive le bouton


# callback pour se connecter
@app.callback(
    Output('login-status', 'children'), Output('redirect-url', 'data'),
    Output('login-email', 'value'), Output('login-password', 'value'),
    [Input('login-button', 'n_clicks')],
    [State('login-email', 'value'), State('login-password', 'value'),]
)
def login_to_app(n_clicks, email, password):
    if n_clicks > 0:
        user = get_user_from_email(email)

        if not user or user.id == 0:
            return html.Div([
                html.P("Identifiants invalides", className='text-danger'),
            ]), dash.no_update, '', ''

        if user and user.check_password(password):
            login_user(user)
            return "Vous êtes connecté.", "/login", '', ''

        return html.Div([
            html.P("Identifiants invalides", className='text-danger'),
        ]), dash.no_update, '', ''
    return "", dash.no_update, dash.no_update, dash.no_update


@app.callback(
    Output('url', 'pathname'),
    [Input('redirect-url', 'data'), Input('redirect-logout', 'data')]
)
def redirect(redirect_login, redirect_logout):
    if redirect_login:
        return redirect_login
    if redirect_logout:
        return redirect_logout
    return dash.no_update


# vérifier la validité de l'email de connexion
@app.callback(
    [Output("login-email", "valid"),
     Output("login-email", "invalid"),
     Output("login-email-valid", "children"),
     Output("login-email-invalid", "children")],
    [Input("login-email", "value")],
)
def check_login_email_validity(email):
    if not email:
        return False, False, '', ''
    if not is_email_valid(email):
        return False, True, '', "Ceci n'est pas une adresse email."
    if email.endswith('@example.com'):
        return False, True, '', "Ceci n'est pas une adresse email valide."
    return True, False, '', ''
