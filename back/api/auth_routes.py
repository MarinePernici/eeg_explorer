""" This module contains the functions used to manage the users """

from flask_login import current_user, login_user
from back.models import User
import os
from passlib.hash import argon2


def is_user_authenticated():
    return current_user.is_authenticated

def get_username():
    return current_user.username

def get_email():
    return current_user.email

def get_id():
    return current_user.id

# def is_username_registered(name):
#     existing_username = User.query.filter_by(username=name).first()
#     return existing_username is not None

# def is_email_registered(email):
#     existing_user = User.query.filter_by(email=email).first()
#     return existing_user is not None

# def create_user(name, email, password):

#     if is_email_registered(email):
#         return False

#     # create a user instance
#     user = User(username=name, email=email)
#     user.set_password(password)

#     # add user in the database
#     try:
#         db.session.add(user)
#         db.session.commit()
#         return True
#     except Exception as e:
#         print("Erreur lors de la création de l'utilisateur:", e)
#         db.session.rollback()
#         return False


# def create_deleted_user():
#     deleted_user = User.query.filter_by(username='deletedUser').first()
#     if not deleted_user:
#         # generate a strong random password
#         random_password = os.urandom(24).hex()
#         hashed_password = argon2.hash(random_password)

#         deleted_user = User(
#             id=0,
#             username='deletedUser',
#             email='supprime@example.com',  # false email
#             password_hash=hashed_password,  # hashed password
#         )
#         db.session.add(deleted_user)
#         db.session.commit()


# def login_process(
#     email,
#     password
# ):
#     user = User.query.filter_by(email=email).first()
    
#     if not user:
#         return False
    
#     if user.id == 0:   # deleted user id
#         return False

#     if user and user.check_password(password):
#         login_user(user)
#         return True
#     return False
