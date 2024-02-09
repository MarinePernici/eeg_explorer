# import os

# import pytest
# from dash import Dash
# from dotenv import load_dotenv
# from flask import Flask
# from flask_login import LoginManager, login_user, logout_user

# from back.models import User, db
# from front.app import app
# from front.callbacks.router import page_router
# from front.components.page_content import app_layout
# from front.pages.contact import contact_form_layout
# from front.pages.documentation import documentation_layout
# from front.pages.error_404 import error_404_layout
# from front.pages.explorer import explorer_layout
# from front.pages.forgot_password import forgot_password_layout
# from front.pages.home import home_layout
# from front.pages.login import login_layout, user_layout
# from front.pages.profile_delete import profile_delete_account_layout
# from front.pages.profile_edit import (profile_edit_email_layout,
#                                       profile_edit_layout,
#                                       profile_edit_password_layout)
# from front.pages.profile_history import profile_history_layout
# from front.pages.reset_password import reset_password_layout
# from front.pages.unauthorized import unauthorized_layout

# load_dotenv()  # Charge les variables d'environnement depuis '.env'

# @pytest.fixture
# def dash_env():
#     # Initialisation de Flask
#     server = Flask(__name__)
#     server.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
#     server.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

#     # Initialisation de SQLAlchemy
#     db.init_app(server)

#     # Configuration de Flask-Login
#     login_manager = LoginManager()
#     login_manager.init_app(server)

#     @login_manager.user_loader
#     def load_user(user_id):
#         return User.query.get(int(user_id))

#     # Création de l'Application Dash
#     app_dash = Dash(
#         __name__,
#         server=server,
#         suppress_callback_exceptions=True,
#         url_base_pathname='/',
#     )

#     # Configuration du Layout Dash
#     app_dash.layout = app_layout

#     yield app_dash


# # Fixture pour un utilisateur authentifié
# @pytest.fixture
# def authenticated_user(dash_env):
#     with dash_env.server.test_request_context():
#         # Créer ou récupérer un utilisateur test
#         test_user = User(
#             username='test_user',
#             email='test_user@spectre-biotech.com'
#         )
#         login_user(test_user)  # Authentifier l'utilisateur
#         yield
#         logout_user()  # Se déconnecter après le test


# # Fixture pour un utilisateur non authentifié
# @pytest.fixture
# def unauthenticated_user(dash_env):
#     with dash_env.server.test_request_context():
#         logout_user()  # Assurez-vous que l'utilisateur est déconnecté
#         yield


# # test the page_router function when the user is authenticated
# def test_page_router_home_with_authenticated_user(authenticated_user):
#     url = '/home'
#     layout_expected = home_layout
#     assert page_router(url) == layout_expected


# def test_page_router_launching_with_authenticated_user(authenticated_user):
#     url = '/'
#     layout_expected = home_layout
#     assert page_router(url) == layout_expected


# def test_page_router_explorer_with_authenticated_user(authenticated_user):
#     url = '/explorer'
#     layout_expected = explorer_layout
#     assert page_router(url) == layout_expected


# def test_page_router_login_with_authenticated_user(authenticated_user):
#     url = '/login'
#     layout_expected = user_layout
#     assert page_router(url) == layout_expected


# def test_page_router_profile_history_with_authenticated_user(authenticated_user):
#     url = '/profile/history'
#     layout_expected = profile_history_layout
#     assert page_router(url) == layout_expected


# def test_page_router_profile_edit_with_authenticated_user(authenticated_user):
#     url = '/profile/edit'
#     layout_expected = profile_edit_layout
#     assert page_router(url) == layout_expected


# def test_page_router_profile_edit_password_with_authenticated_user(authenticated_user):
#     url = '/profile/edit/password'
#     layout_expected = profile_edit_password_layout
#     assert page_router(url) == layout_expected


# def test_page_router_profile_edit_email_with_authenticated_user(authenticated_user):
#     url = '/profile/edit/email'
#     layout_expected = profile_edit_email_layout
#     assert page_router(url) == layout_expected


# def test_page_router_profile_delete_with_authenticated_user(authenticated_user):
#     url = '/profile/delete'
#     layout_expected = profile_delete_account_layout
#     assert page_router(url) == layout_expected


# def test_page_router_documentation_with_authenticated_user(authenticated_user):
#     url = '/documentation'
#     layout_expected = documentation_layout
#     assert page_router(url) == layout_expected


# def test_page_router_contact_with_authenticated_user(authenticated_user):
#     url = '/contact'
#     layout_expected = contact_form_layout
#     assert page_router(url) == layout_expected


# def test_page_router_forgot_password_with_authenticated_user(authenticated_user):
#     url = '/forgot-password'
#     layout_expected = forgot_password_layout
#     assert page_router(url) == layout_expected


# def test_page_router_reset_password_with_authenticated_user(authenticated_user):
#     url = '/reset_password/123456'
#     layout_expected = reset_password_layout
#     assert page_router(url) == layout_expected


# def test_page_router_error_404_with_authenticated_user(authenticated_user):
#     url = '/unknown_path'
#     layout_expected = error_404_layout
#     assert page_router(url) == layout_expected

# def test_page_router_profile_unknown_with_authenticated_user(authenticated_user):
#     url = '/profile/unknown'
#     layout_expected = error_404_layout
#     assert page_router(url) == layout_expected


# # test the page_router function when the user is not authenticated
# def test_page_router_home_with_unauthenticated_user(unauthenticated_user):
#     url = '/home'
#     layout_expected = home_layout
#     assert page_router(url) == layout_expected


# def test_page_router_launching_with_unauthenticated_user(unauthenticated_user):
#     url = '/'
#     layout_expected = home_layout
#     assert page_router(url) == layout_expected


# def test_page_router_explorer_with_unauthenticated_user(unauthenticated_user):
#     url = '/explorer'
#     layout_expected = unauthorized_layout
#     assert page_router(url) == layout_expected


# def test_page_router_profile_history_with_unauthenticated_user(unauthenticated_user):
#     url = '/profile/history'
#     layout_expected = unauthorized_layout
#     assert page_router(url) == layout_expected


# def test_page_router_profile_edit_with_unauthenticated_user(unauthenticated_user):
#     url = '/profile/edit'
#     layout_expected = unauthorized_layout
#     assert page_router(url) == layout_expected


# def test_page_router_profile_edit_password_with_unauthenticated_user(unauthenticated_user):
#     url = '/profile/edit/password'
#     layout_expected = unauthorized_layout
#     assert page_router(url) == layout_expected


# def test_page_router_profile_edit_email_with_unauthenticated_user(unauthenticated_user):
#     url = '/profile/edit/email'
#     layout_expected = unauthorized_layout
#     assert page_router(url) == layout_expected


# def test_page_router_profile_delete_with_unauthenticated_user(unauthenticated_user):
#     url = '/profile/delete'
#     layout_expected = unauthorized_layout
#     assert page_router(url) == layout_expected


# def test_page_router_documentation_with_unauthenticated_user(unauthenticated_user):
#     url = '/documentation'
#     layout_expected = unauthorized_layout
#     assert page_router(url) == layout_expected


# def test_page_router_contact_with_unauthenticated_user(unauthenticated_user):
#     url = '/contact'
#     layout_expected = contact_form_layout
#     assert page_router(url) == layout_expected


# def test_page_router_forgot_password_with_unauthenticated_user(unauthenticated_user):
#     url = '/forgot-password'
#     layout_expected = forgot_password_layout
#     assert page_router(url) == layout_expected


# def test_page_router_reset_password_with_unauthenticated_user(unauthenticated_user):
#     url = '/reset_password/123456'
#     layout_expected = reset_password_layout
#     assert page_router(url) == layout_expected


# def test_page_router_error_404_with_unauthenticated_user(unauthenticated_user):
#     url = '/unknown_path'
#     layout_expected = error_404_layout
#     assert page_router(url) == layout_expected


# def test_page_router_login_with_unauthenticated_user(unauthenticated_user):
#     url = '/login'
#     layout_expected = login_layout
#     assert page_router(url) == layout_expected

# def test_page_router_profile_unknown_with_unauthenticated_user(unauthenticated_user):
#     url = '/profile/unknown'
#     layout_expected = unauthorized_layout
#     assert page_router(url) == layout_expected
