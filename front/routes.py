""" app routes"""

# from front.app import app
# from front.components.page_content import app_layout

# app.layout = app_layout

from front.callbacks.contact_page import handle_form_submission
from front.callbacks.delete_account_page import delete_account
from front.callbacks.dynamic_content import update_dynamic_content
from front.callbacks.edit_password_page import (
    change_password, check_confirm_new_password_validity,
    check_new_password_validity, update_edit_password_button_state)
from front.callbacks.edit_email_page import (
    change_email, check_confirm_new_email_validity,
    check_new_email_validity, update_edit_email_button_state)
from front.callbacks.explorer_page import ask_spectre_database
from front.callbacks.history_page import generate_file, update_history_table
from front.callbacks.home_page import update_explorer_link
from front.callbacks.login_process import (check_login_email_validity,
                                           login_to_app, redirect,
                                           update_login_button_state)
from front.callbacks.logout_process import logout_from_app
from front.callbacks.navbar_links import update_navbar_links
from front.callbacks.profile_edit_page import (change_username,
                                               update_edit_content)
from front.callbacks.reset_forgotten_password import (
    check_user_email_validity, reset_password, send_reset_password_email,
    update_forgot_password_button_state)
from front.callbacks.router import page_router
from front.callbacks.signup_process import (check_email_validity,
                                            check_password_validity,
                                            check_username_validity,
                                            create_account,
                                            update_signup_button_state)
