import os
import re

from dotenv import load_dotenv
from back.api.models import User, db, Queries, QueryResults, Contacts
from passlib.hash import argon2
from flask_login import logout_user

load_dotenv()  # Charge les variables d'environnement depuis '.env'


def update_user_id(rows, new_id):
    for row in rows:
        row.user_id = new_id
    try:
        db.session.commit()
    except Exception as e:
        print("Erreur lors de la mise à jour :", e)
        db.session.rollback()


def delete_user(user):
    try:
        db.session.delete(user)
        db.session.commit()
        logout_user()
    except Exception as e:
        print("Erreur lors de la suppression de l'utilisateur :", e)
        db.session.rollback()


def verify_password(user, password):
    return user.check_password(password)


def get_query_result_from_id(query_id):
    return QueryResults.query.filter_by(query_id=query_id).first()


def get_queries_from_user_id(user_id):
    return Queries.query.filter_by(user_id=user_id).all()    


def get_contacts_from_user_id(user_id):
    return Contacts.query.filter_by(user_id=user_id).all()

def edit_password(user, new_password):
    user.set_password(new_password)
    try:
        db.session.commit()
        return True
    except Exception as e:
        print("Erreur lors de la modification du mot de passe:", e)
        db.session.rollback()
        return False


def edit_username(user, new_username):
    user.username = new_username
    try:
        db.session.commit()
        return True
    except Exception as e:
        print("Erreur lors de la modification du nom d'utilisateur:", e)
        db.session.rollback()
        return False


def edit_email(user, new_email):
    user.email = new_email
    try:
        db.session.commit()
        return True
    except Exception as e:
        print("Erreur lors de la modification de l'adresse email:", e)
        db.session.rollback()
        return False


def get_user_from_id(user_id):
    return User.query.filter_by(id=user_id).first()


def get_user_from_email(email):
    return User.query.filter_by(email=email).first()


def get_user_from_username(username):
    return User.query.filter_by(username=username).first()


def is_email_allowed(email):
    allowed_domain = os.environ.get('ALLOWED_DOMAIN')
    domain = email.split('@')[-1]
    return domain.lower() == allowed_domain.lower()


def is_username_registered(name):
    existing_username = User.query.filter_by(username=name).first()
    return existing_username is not None


def is_email_registered(email):
    existing_user = User.query.filter_by(email=email).first()
    return existing_user is not None


def is_email_valid(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None


def is_username_valid(username):
    if username.lower() == 'deleteduser':
        return False, 'Ce nom d\'utilisateur n\'est pas autorisé.'

    if len(username) < 3 or len(username) > 15:
        return False, 'Le nom d\'utilisateur doit avoir entre 3 et 15 caractères.'

    username_regex = r'^[a-zA-Z0-9._-]{3,15}$'
    if not re.match(username_regex, username):
        return False, 'Le nom d\'utilisateur ne doit contenir que des chiffres, lettres, tirets ou underscores.'

    return re.match(username_regex, username) is not None, ''


def is_password_safe(password):
    if len(password) < 12:
        return False, 'Le mot de passe doit contenir au moins 12 caractères.'
    if not re.search(r"[A-Z]", password):
        return False, 'Le mot de passe doit contenir au moins une lettre majuscule.'
    if not re.search(r"[a-z]", password):
        return False, 'Le mot de passe doit contenir au moins une lettre minuscule.'
    if not re.search(r"\d", password):
        return False, 'Le mot de passe doit contenir au moins un chiffre.'
    if not re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', password):
        return False, 'Le mot de passe doit contenir au moins un caractère spécial.'
    return True, ""


def create_user(name, email, password):

    if is_email_registered(email):
        return False

    # create a user instance
    user = User(username=name, email=email)
    user.set_password(password)

    # add user in the database
    try:
        db.session.add(user)
        db.session.commit()
        return True
    except Exception as e:
        print("Erreur lors de la création de l'utilisateur:", e)
        db.session.rollback()
        return False


def create_deleted_user():
    deleted_user = User.query.filter_by(username='deletedUser').first()
    if not deleted_user:
        # generate a strong random password
        random_password = os.urandom(24).hex()
        hashed_password = argon2.hash(random_password)

        deleted_user = User(
            id=0,
            username='deletedUser',
            email='supprime@example.com',  # false email
            password_hash=hashed_password,  # hashed password
        )
        db.session.add(deleted_user)
        db.session.commit()
