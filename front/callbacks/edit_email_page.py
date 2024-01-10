""" Callbacks for the edit_email page"""

import dash
from dash.dependencies import Input, Output, State

from back.api.auth_routes import (get_id, is_user_authenticated)
from front.app import app
from front.auth import (
    get_user_from_id,
    is_email_valid,
    edit_email,
    is_email_allowed,
    is_email_registered,
)


# vérifier la validité du nouvel email
@app.callback(
    [Output('new-email', 'valid'),
     Output('new-email', 'invalid'),
     Output('new-email-feedback-valid', 'children'),
     Output('new-email-feedback-invalid', 'children'),],
    [Input("new-email", "value")],
)
def check_new_email_validity(email):
    if not email:
        return False, False, '', ''
    if not is_email_valid(email):
        return False, True, '', 'Ceci n\'est pas une adresse email valide.'
    return True, False, '', ''


# vérifier la validité de la confirmation du nouvel email
@app.callback(
    [Output('confirm-new-email', 'valid'),
     Output('confirm-new-email', 'invalid'),
     Output('confirm-new-email-feedback-valid', 'children'),
     Output('confirm-new-email-feedback-invalid', 'children'),],
    [Input("confirm-new-email", "value"),
     Input("new-email", "value")],
)
def check_confirm_new_email_validity(confirm_email, new_email):
    if not confirm_email:
        return False, False, '', ''
    if confirm_email != new_email:
        return False, True, '', 'Les adresses email ne correspondent pas.'
    return True, False, '', ''


# callback pour activer/désactiver le bouton de modification du mot de passe
@app.callback(
    Output("edit-email-button", "disabled"),
    [Input("new-email", "valid"),
     Input("confirm-new-email", "valid"),
     Input("password", "value")],
)
def update_edit_email_button_state(
    valid_new_email,
    valid_confirm_email,
    password
):
    if valid_new_email and valid_confirm_email and password:
        return False
    return True


# callback pour modifier l'email
@app.callback(
    Output('email-change-status', 'children'),
    [Input('edit-email-button', 'n_clicks')],
    [State('new-email', 'value'),
     State('password', 'value')]
)
def change_email(n_clicks, new_email, password):
    if new_email and n_clicks > 0 and is_user_authenticated():
        user = get_user_from_id(get_id())

        if not user.check_password(password):
            return "Identifiants invalides."
        
        if not is_email_valid(new_email):
            return "Adresse email invalide."

        if is_email_registered(new_email):
            return "Un compte existe déjà avec cette adresse e-mail."

        if not is_email_allowed(new_email):
            return "Adresse email non autorisée. Vous ne pouvez pas créer de compte."

        if edit_email(user, new_email):
            return "L'email a été changé avec succès."
        return "Une erreur est survenue lors du changement d'email."

    return ""

# callback pour reinitialiser le formulaire
@app.callback(
    Output('password', 'value'),
    Output('new-email', 'value'),
    Output('confirm-new-email', 'value'),
    [Input('email-change-status', 'children')],
    prevent_initial_call=True
)
def reset_form(status):
    if status == "L'email a été changé avec succès.":
        return '', '', ''
    return dash.no_update, dash.no_update, dash.no_update