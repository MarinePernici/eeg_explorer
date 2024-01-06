""" Callbacks for the home page"""

from dash.dependencies import Input, Output

from back.api.auth_routes import is_user_authenticated
from front.app import app


# callback to change the link of the start exploration button
@app.callback(
    Output('start-exploration-button', 'href'),
    [Input('url', 'pathname')],
)
def update_explorer_link(
    pathname: str,
) -> str:
    """ Update the link of the start exploration button depending on the
    user authentication status

    Args:
        pathname (str): current url path

    Returns:
        str: new link of the start exploration button (explorer page if
            user is authenticated, login page otherwise)
    """
    if pathname == '/home' and is_user_authenticated():
        return '/explorer'
    return '/login'
