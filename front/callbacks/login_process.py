""" Callbacks for the login process"""

import dash
from dash import dcc, callback_context, html
from dash.dependencies import Input, Output, State

from back.api.auth_routes import (
    get_username, is_user_authenticated, is_email_registered,
    is_email_registered, login_process
)
from front.auth import is_email_valid, is_email_allowed, is_password_safe
from front.app import app


# callback pour activer/désactiver le bouton de connexion
@app.callback(
    Output('login-button', 'disabled'), Output('login-button', 'color'),
    [Input('login-email', 'valid'), Input('login-password', 'value')]
)
def update_login_button_state(valid_email, password):
    if valid_email and password :  # Vérifie si les champs ne sont pas vides
        return False, 'primary'  # Active le bouton
    return True, 'info'  # Désactive le bouton


# callback pour se connecter
@app.callback(
    Output('login-status', 'children'), Output('redirect-url', 'data'),
    Output('login-email', 'value'), Output('login-password', 'value'),
    [Input('login-button', 'n_clicks')],
    [State('login-email', 'value'), State('login-password', 'value'),]
)
def login_to_app(n_clicks, email, password):
    if n_clicks > 0:
        user_logged = login_process(email, password)

        if not user_logged:
            return html.Div([
                html.P("Identifiants invalides", className='text-danger'),
            ]), dash.no_update, '', ''

        return "Vous êtes connecté.", "/login", '', ''

    return "", dash.no_update, dash.no_update, dash.no_update



@app.callback(
    Output('url', 'pathname'),
    [Input('redirect-url', 'data')]
)
def redirect(pathname):
    return pathname if pathname else dash.no_update


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
    return True, False, '', ''


# # callback pour se connecter
# @app.callback(
#     Output('login-status', 'children'), Output('redirect-url', 'data'),
#     [Input('login-button', 'n_clicks'), Input('login-password', 'value'),],
#     [State('login-email', 'value'), State('login-password', 'value'),]
# )
# def login(n_clicks, password_edit, email, password):
#     ctx = callback_context
#     if not ctx.triggered:
#         raise dash.exceptions.PreventUpdate
    
#     trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

#     if trigger_id == 'login-button':
#         if n_clicks > 0:
#             user = User.query.filter_by(email=email).first()

#             if user.id == 0:   # Compte supprimé
#                 return "Identifiants invalides", dash.no_update

#             if user and user.check_password(password):
#                 login_user(user)
#                 return "Vous êtes connecté.", "/login"

#             return html.Div([
#                 html.P("Mot de passe invalide.", className='text-danger'),
#             ]), dash.no_update        
#         return "", dash.no_update
#     if trigger_id == 'login-password':
#         return "", dash.no_update