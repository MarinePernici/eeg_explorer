""" callback for the navbar links"""

from dash.dependencies import Input, Output, State

from back.api.auth_routes import is_user_authenticated
from front.app import app

# callback pour activer/désactiver les liens du menu de navigation
@app.callback(
    Output("explorer_link", "disabled"),
    Output("history_link", "disabled"),
    Output("edit_link", "disabled"),
    Output("delete_link", "disabled"),
    Output("account_dropdown", "disabled"),
    [Input("url", "pathname")],
)
def update_navbar_links(pathname):
    if pathname and is_user_authenticated():
        return False, False, False, False, False
    # if pathname in ["/login", "/profile"] and n_clicks > 0:
    #     return False, False, False, False, False
    return True, True, True, True, True
