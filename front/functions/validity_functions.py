import os
import re
from dotenv import load_dotenv

load_dotenv()


def is_email_allowed(email):
    allowed_domain = os.environ.get('ALLOWED_DOMAIN')
    domain = email.split('@')[-1]
    return domain.lower() == allowed_domain.lower()


def is_email_valid(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None


def is_username_valid(username):
    if username.lower() == 'deleteduser':
        return False, 'Ce nom d\'utilisateur n\'est pas autorisé.'

    username_regex = r'^[a-zA-Z0-9]{1,30}$'
    if not re.match(username_regex, username):
        return False, 'Seuls les lettres et les chiffres sont autorisés (max. 30 caractères).'

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
