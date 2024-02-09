import os
import re
from dotenv import load_dotenv
from dash import html


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


# def is_password_safe(password):
#     if len(password) < 12:
#         return False, 'Le mot de passe doit contenir au moins 12 caractères.'
#     if not re.search(r"[A-Z]", password):
#         return False, 'Le mot de passe doit contenir au moins une lettre majuscule.'
#     if not re.search(r"[a-z]", password):
#         return False, 'Le mot de passe doit contenir au moins une lettre minuscule.'
#     if not re.search(r"\d", password):
#         return False, 'Le mot de passe doit contenir au moins un chiffre.'
#     if not re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', password):
#         return False, 'Le mot de passe doit contenir au moins un caractère spécial.'
#     return True, ""
def is_safe_input(input_string: str) -> bool:
    """
    Checks if the input string is safe to be processed or
    inserted into the database.
    This function searches for patterns that might indicate
    an SQL injection attempt.

    Args:
        input_string (str): The input string to be checked.

    Returns:
        bool: True if the input string is safe, False otherwise.
    """
    # List of patterns 
    patterns = [
        r';',        # Semicolon
        r'--',       # SQL comment
        r'\/\*',     # SQL comment (start)
        r'\*\/',     # SQL comment (end)
        r'@@',       # SQL system variable
        r'char\(',   # CHAR function (used for obfuscation)
    ]

    # Check each pattern against the input
    for pattern in patterns:
        if re.search(pattern, input_string):
            return False

    return True


def format_password_feedback(feedback: str) -> html.P:
    """ Format the password feedback

    Args:
        feedback (str): feedback to format

    Returns:
        html.P: formatted feedback
    """
    return html.P(
        f'Le mot de passe doit contenir au moins {feedback}.',
        className='my-0'
    )

def is_password_safe(password: str) -> tuple[bool, list[str]]:
    """ Check if the password is safe

    Args:
        password (str): password to check

    Returns:
        tuple[bool, list[str]]: is password safe, list of errors
    """
    errors = []

    if not is_safe_input(password):
        errors.append('Le mot de passe n\'est pas valide.')
        return False, errors

    if len(password) < 12:
        errors.append(format_password_feedback('12 caractères'))

    if not re.search(r"[A-Z]", password):
        errors.append(format_password_feedback('une lettre majuscule'))

    if not re.search(r"[a-z]", password):
        errors.append(format_password_feedback('une lettre minuscule'))

    if not re.search(r"\d", password):
        errors.append(format_password_feedback('un chiffre'))

    if not re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', password):
        errors.append(format_password_feedback('un caractère spécial'))

    if not errors:
        return True, errors
    return False, errors
