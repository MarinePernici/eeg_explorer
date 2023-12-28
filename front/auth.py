import os
import re

from dotenv import load_dotenv
from models import User, db
from passlib.hash import argon2

load_dotenv()  # Charge les variables d'environnement depuis '.env'


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
    return True, "Le mot de passe respecte les standards de sécurité."


def create_user(name, email, password):

    if is_email_registered(email):
        return False

    # Créez une instance de l'utilisateur
    user = User(username=name, email=email)
    user.set_password(password)  # Utilisez la méthode définie dans votre modèle User pour hacher le mot de passe

    # Ajoutez l'utilisateur à la base de données
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
        # Générer un mot de passe fort et aléatoire
        random_password = os.urandom(24).hex()
        hashed_password = argon2.hash(random_password)

        deleted_user = User(
            id=0,  # ou un autre ID spécifique
            username='deletedUser',
            email='supprime@example.com',  # Email factice
            password_hash=hashed_password,  # Mot de passe hashé
            # Assurez-vous de définir d'autres champs requis avec des valeurs par défaut ou factices
        )
        db.session.add(deleted_user)
        db.session.commit()
