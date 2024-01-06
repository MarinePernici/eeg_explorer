""" Callbacks for the profile edit page"""

import dash
from dash.dependencies import Input, Output

from back.api.auth_routes import get_username, is_user_authenticated, get_email
from front.app import app

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
