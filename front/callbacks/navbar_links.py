""" callback for the navbar links"""

from dash.dependencies import Input, Output

from back.api.auth_routes import is_user_authenticated
from front.app import app


# callback pour activer/désactiver les liens du menu de navigation
@app.callback(
    Output("explorer_link", "disabled"),
    Output("history_link", "disabled"),
    Output("edit_link", "disabled"),
    Output("delete_link", "disabled"),
    Output("account_dropdown", "disabled"),
    Output("login_link", "children"),
    [Input("url", "pathname")],
)
def update_navbar_links(pathname: str):
    """
    Enable/disable the links in the navigation menu

    Args:
        pathname (str): current url path

    Returns:
        bool: state of the links
    """
    if pathname and is_user_authenticated():
        return False, False, False, False, False, "Se déconnecter"
    return True, True, True, True, True, "Se connecter"
