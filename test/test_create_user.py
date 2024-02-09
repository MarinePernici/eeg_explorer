# """ tests for the create_user function in the auth module """

# import os
# from unittest.mock import patch

# import pytest
# from dash import Dash
# from dotenv import load_dotenv
# from flask import Flask
# from flask_login import LoginManager
# from sqlalchemy.exc import SQLAlchemyError

# from back.api.auth import create_user, delete_user, get_user_from_email
# from back.models import User, db

# load_dotenv()  

# # def create_app (test=False):
# #     pass

# @pytest.fixture(scope='function')
# def test_client():
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

#     # app_dash = create_app(test=True)  # initialize the app with the test configuration

#     flask_app = app_dash.server
#     with flask_app.app_context():
#         db.session.begin_nested()  # create a savepoint for the test transactions 
#         yield flask_app.test_client()
#         db.session.rollback()  # rollback the test transactions

# # Test avec des données valides
# def test_create_user_success(test_client):
#     name = "TestUser"
#     email = "testuser@spectre-biotech.com"
#     password = "ValidPassword123!"
#     result, message = create_user(name, email, password)
#     message_expected = "Utilisateur créé avec succès. Vous pouvez maintenant vous connecter."
#     assert result == True
#     assert message == message_expected

#     user = User.query.filter_by(email=email).first()
#     assert user is not None
#     assert user.username == name
    
#     db.session.delete(user)
#     db.session.commit()

# # Test avec un email déjà enregistré
# def test_create_user_duplicate_email(test_client):
#     name = "AnotherUser"
#     email = "eeg_explorer@spectre-biotech.com"  # Email déjà enregistré
#     password = "AnotherValidPassword123!"
#     result, message = create_user(name, email, password)
#     message_expected = "Email déjà enregistré"
#     assert result == False
#     assert message == message_expected

#     user = User.query.filter_by(email=email).first()
#     assert user is not None
#     assert user.username != name
#     assert user.email == email


# # Test avec un mot de passe invalide
# def test_create_user_invalid_password(test_client):
#     name = "TestUserInvalidPwd"
#     email = "testuserinvalid@example.com"
#     password = "abc;--"  # Mot de passe invalide
#     result, message = create_user(name, email, password)
#     message_expected = "Mot de passe non sécurisé"
#     assert result == False
#     assert message == message_expected

#     user = User.query.filter_by(email=email).first()
#     assert user is None
#     if user:
#         db.session.delete(user)
#         db.session.commit()


# # Test avec un email invalide
# def test_create_user_invalid_email(test_client):
#     name = "TestUserInvalidEmail"
#     email = "invalidemail"  # Email invalide
#     password = "ValidPassword123!"
#     result, message = create_user(name, email, password)
#     message_expected = "Email invalide"
#     assert result == False
#     assert message == message_expected

#     user = User.query.filter_by(email=email).first()
#     assert user is None
#     if user:
#         db.session.delete(user)
#         db.session.commit()


# # test with an error during user creation
# def test_db_error_during_user_creation(test_client):
#     name = "TestUser"
#     email = "testotheruser@spectre-biotech.com"
#     password = "ValidPassword123!"
#     message_expected = "Erreur lors de l'enregistrement de l'utilisateur"

#     with patch('back.models.db.session.commit', side_effect=SQLAlchemyError):
#         result, message = create_user(name, email, password)
#         assert not result
#         assert message == message_expected

#     user = User.query.filter_by(email=email).first()
#     assert user is None
#     if user:
#         db.session.delete(user)
#         db.session.commit()
