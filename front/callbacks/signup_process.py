""" Callbacks for the signup process"""

import dash
from dash.dependencies import Input, Output, State

from front.app import app
from back.api.auth import (
    is_email_registered, create_user
)
from front.functions.validity_functions import (
    is_email_allowed, is_email_valid,
    is_password_safe, is_username_valid
)


# callback pour activer/désactiver le bouton d'inscription
@app.callback(
    Output('signup-button', 'disabled'),
    [Input('signup-email', 'valid'),
     Input('signup-password', 'valid', ),
     Input('signup-name', 'valid')
    ]
)
def update_signup_button_state(
    valid_email: bool,
    valid_password: bool,
    valid_name: bool,
) -> bool:
    """ Update the signup button state

    Args:
        valid_email (bool): is email valid
        valid_password (bool): is password valid
        valid_name (bool): is name valid

    Returns:
        bool: is button disabled
    """
    if valid_email and valid_password and valid_name:
        return False  # button enabled
    return True  # button disabled


# callback pour créer un compte
@app.callback(
    [
        Output('signup-status', 'children'),
        Output('signup-name', 'value'),
        Output('signup-email', 'value'),
        Output('signup-password', 'value')
    ],
    [
        Input('signup-button', 'n_clicks')
    ],
    [
        State('signup-name', 'value'),
        State('signup-email', 'value'),
        State('signup-password', 'value')
    ]
)
def create_account(n_clicks, name, email, password):
    if n_clicks is None or not email or not password:
        return dash.no_update

    if is_email_registered(email):
        return 'Un compte existe déjà avec cette adresse e-mail. Veuillez utiliser le formulaire de connexion', '', '', ''

    # Vérifier si l'email est autorisé
    if not is_email_allowed(email):
        return 'Adresse email non autorisée. Vous ne pouvez pas créer de compte.', '', '', ''

    # Créer l'utilisateur
    is_user_created, message = create_user(name, email, password)

    return message, '', '', ''


# vérifier la validité du nom d'inscription
@app.callback(
    [Output("signup-name", "valid"),
     Output("signup-name", "invalid"),
     Output("username-feedback-valid", "children"),
     Output("username-feedback-invalid", "children")],
    [Input("signup-name", "value")],
)
def check_username_validity(name):
    if not name:
        return False, False, '', ''
    
    validity, reason = is_username_valid(name)
    if not validity:
        return False, True, '', reason

    return True, False, reason, ''


@app.callback(
    [Output("signup-email", "valid"),
     Output("signup-email", "invalid"),
     Output("email-feedback-valid", "children"),
     Output("email-feedback-invalid", "children")],
    [Input("signup-email", "value")],
)
def check_email_validity(
    email: str
) -> tuple[bool, bool, str, str]:
    """ Check if the email is valid and allowed

    Args:
        email (str): email to check
    
    Returns:
        bool: is email valid
        bool: is email invalid
        bool: valid feedback
        bool: invalid feedback
    """
    if not email:
        return False, False, '', ''
    if not is_email_valid(email):
        return False, True, '', 'Ceci n\'est pas une adresse email valide.'
    if not is_email_allowed(email):
        return False, True, '', 'Adresse email non autorisée.'
    return True, False, '', ''

# vérifier la validité du mot de passe d'inscription
@app.callback(
    [Output("signup-password", "valid"),
     Output("signup-password", "invalid"),
     Output("password-feedback-valid", "children"),
     Output("password-feedback-invalid", "children")
    ],
    [Input("signup-password", "value")],
)
def check_password_validity(password):
    if not password:
        return False, False, '', ''
    safety, reason = is_password_safe(password)
    if not safety:
        return False, True, '', reason
    return True, False, reason, ''