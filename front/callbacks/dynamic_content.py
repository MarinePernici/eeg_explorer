""" Callbacks to update the dynamic content on several pages"""

import dash
from dash import dcc
from dash.dependencies import Input, Output

from back.api.auth_routes import get_username, is_user_authenticated
from front.app import app


# Callback to update the dynamic content on several pages
@app.callback(
    Output('dynamic-username', 'children'),
    [Input('url', 'pathname')]
)
def update_dynamic_content(
    pathname: str
) -> str:
    """
    Update the dynamic content on several pages

    Args:
        pathname (str): current url path

    Returns:
        str: dynamic content to display
    """
    if pathname:
        if is_user_authenticated():
            return dcc.Markdown(
                    f"Bienvenue **{get_username()}**"
                )
    return dash.no_update
