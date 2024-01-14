""" Callbacks for the logout process"""

import dash
from dash import html
from dash.dependencies import Input, Output
from flask_login import logout_user

from front.app import app


# callback pour se déconnecter
@app.callback(
    Output('logout-content', 'children'),
    Output('redirect-logout', 'data'),
    [Input('logout-button', 'n_clicks')],
    prevent_initial_call=True,
)
def logout_from_app(n_clicks):
    if n_clicks > 0:
        logout_user()

        return html.Div([
                html.P("Vous n'êtes plus connecté."),
            ]), "/login"
    return dash.no_update, dash.no_update