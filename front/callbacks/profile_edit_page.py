""" Callbacks for the profile edit page"""

import dash
from dash.dependencies import Input, Output, State

from back.api.auth_routes import get_username, is_user_authenticated, get_email, get_id
from front.app import app
from front.auth import (
    get_user_from_id, is_email_allowed, is_email_valid,
    is_email_registered, edit_username, edit_email
)

# Callback to display the current username and email on the profile edit page
@app.callback(
    Output('profile-username', 'children'),
    Output('profile-email', 'children'),
    [
        Input('url', 'pathname'),
        Input('username-change-status', 'children'),
        Input('email-change-status', 'children')
    ],
)
def update_edit_content(pathname, username_status, email_status):
    """
    Display the current username and email on the profile edit page

    Args:
        pathname (str): current url path
        username_status (str): username change status
        email_status (str): email change status

    Returns:
        str: username and email to display
    """
    if pathname == '/profile/edit' and is_user_authenticated():
        return (
            f"Nom d'utilisateur actuel : {get_username()}",
            f"Email actuel : {get_email()}"
        )
    # if username_status == "Le nom d'utilisateur a été changé avec succès.":
    #     return (
    #         f"Nom d'utilisateur actuel : {get_username()}",
    #         f"Email actuel : {get_email()}"
    #     )
    # if email_status == "L'email a été changé avec succès.":
    #     return (
    #         f"Nom d'utilisateur actuel : {get_username()}",
    #         f"Email actuel : {get_email()}"
    #     )
    return dash.no_update


# callback pour modifier le nom d'utilisateur
@app.callback(
    Output('username-change-status', 'children'),
    [Input('edit-username-button', 'n_clicks')],
    [State('new-username', 'value')]
)
def change_username(n_clicks, new_username):
    if new_username and n_clicks > 0 and is_user_authenticated():
        user = get_user_from_id(get_id())

        if edit_username(user, new_username):
            return "Le nom d'utilisateur a été changé avec succès."
        return "Une erreur est survenue lors du changement de nom d'utilisateur."

    return ""

# callback pour modifier l'email
@app.callback(
    Output('email-change-status', 'children'),
    [Input('edit-email-button', 'n_clicks')],
    [State('new-email', 'value')]
)
def change_email(n_clicks, new_email):
    if new_email and n_clicks > 0 and is_user_authenticated():
        user = get_user_from_id(get_id())
        if not is_email_valid(new_email):
            return "Adresse email invalide."

        if is_email_registered(new_email):
            return "Un compte existe déjà avec cette adresse e-mail."

        if not is_email_allowed(new_email):
            return "Adresse email non autorisée. Vous ne pouvez pas créer de compte."

        if edit_email(user, new_email):
            return "L'email a été changé avec succès."
        return "Une erreur est survenue lors du changement d'email."

    return ""