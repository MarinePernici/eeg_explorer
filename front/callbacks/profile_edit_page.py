""" Callbacks for the profile edit page"""

import dash
from dash.dependencies import Input, Output, State

from back.api.auth_routes import get_username, is_user_authenticated, get_id
from front.app import app
from back.api.auth import (
    get_user_from_id, edit_username
)
from front.functions.validity_functions import is_username_valid

# Callback to display the current username on the profile edit page
@app.callback(
    Output('profile-username', 'children'),
    [
        Input('url', 'pathname'),
        Input('username-change-status', 'children'),
    ],
)
def update_edit_content(pathname, change_status):
    """
    Display the current username and email on the profile edit page

    Args:
        pathname (str): current url path
        username_status (str): username change status
        email_status (str): email change status

    Returns:
        str: username and email to display
    """
    if pathname == '/profile/edit' or change_status:
        if is_user_authenticated():
            return f"Nom d'utilisateur actuel : {get_username()}"

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


# vérifier la validité du nouveau nom
@app.callback(
    [Output("new-username", "valid"),
     Output("new-username", "invalid"),
     Output("new-username-feedback-valid", "children"),
     Output("new-username-feedback-invalid", "children")],
    [Input("new-username", "value")],
)
def check_username_validity(name):
    if not name:
        return False, False, '', ''
    
    validity, reason = is_username_valid(name)
    if not validity:
        return False, True, '', reason

    return True, False, reason, ''