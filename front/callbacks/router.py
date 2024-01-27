""" Callbacks to display the layout according to the url"""

from dash.dependencies import Input, Output

from back.api.auth_routes import is_user_authenticated
from front.app import app
from front.pages.contact import contact_form_layout
from front.pages.error_404 import error_404_layout
from front.pages.explorer import explorer_layout
from front.pages.forgot_password import forgot_password_layout
from front.pages.home import home_layout
from front.pages.login import login_layout, user_layout
from front.pages.profile import profile_layout
from front.pages.profile_delete import profile_delete_account_layout
from front.pages.profile_edit import (
    profile_edit_layout, profile_edit_password_layout, profile_edit_email_layout
)
from front.pages.profile_history import profile_history_layout
from front.pages.reset_password import reset_password_layout
from front.pages.unauthorized import unauthorized_layout

# dictionary of the routes
routes = {
    '/': home_layout,
    '/home': home_layout,
    '/login': login_layout,
    '/explorer': explorer_layout,
    '/contact': contact_form_layout,
    '/forgot-password': forgot_password_layout,
    '/profile/history': profile_history_layout,
    '/profile/edit': profile_edit_layout,
    '/profile/edit/password': profile_edit_password_layout,
    '/profile/edit/email': profile_edit_email_layout,
    '/profile/delete': profile_delete_account_layout,
    '/profile': profile_layout
}

# list of the protected paths
protected_paths = ['/explorer', '/profile']

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def page_router(pathname: str) -> str:
    """
    Display the layout according to the url

    Args:
        pathname (str): current url path

    Returns:
        str: layout to display
    """
    # management of the authentication status of the user for protected paths
    if any(
        pathname.startswith(path) for path in protected_paths
    ) and not is_user_authenticated():
        return unauthorized_layout

    # redirect to user page if user is authenticated
    if pathname == '/login' and is_user_authenticated():
        return user_layout

    # management of the reset password page
    if pathname.startswith('/reset_password/'):
        return reset_password_layout

    # main router
    return routes.get(pathname, error_404_layout)
