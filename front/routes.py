""" app routes"""

from dash import dcc, html

from app import app

from pages.header import header
from pages.navbar import navbar
from pages.footer import footer

# Contenu principal
content = html.Div(id="page-content")

app.layout = html.Div(className='content-wrapper', children=[
    header,
    navbar,
    dcc.Store(id='redirect-url'),
    dcc.Location(id='url', refresh=False),
    content,
    footer
])


from front.callbacks.router import page_router

from front.callbacks.home_page import update_explorer_link

from front.callbacks.dynamic_content import update_dynamic_content

from front.callbacks.profile_edit_page import update_edit_content

from front.callbacks.login_process import (
    update_login_button_state,
    redirect,
    check_login_email_validity,
    login_to_app
)

from front.callbacks.signup_process import (
    update_signup_button_state,
    create_account,
    check_username_validity,
    check_email_validity,
    check_password_validity
)

from front.callbacks.logout_process import logout_from_app

from front.callbacks.reset_forgotten_password import (
    check_user_email_validity,
    update_forgot_password_button_state,
    send_reset_password_email,
    reset_password
)

from front.callbacks.edit_password_page import (
    check_new_password_validity,
    check_confirm_new_password_validity,
    update_edit_password_button_state,
    change_password
)

from front.callbacks.profile_edit_page import (
    change_username,
    change_email
)

from front.callbacks.explorer_page import ask_spectre_database


from front.callbacks.history_page import update_history_table, generate_file


from front.callbacks.delete_account_page import delete_account

from front.callbacks.contact_page import handle_form_submission
