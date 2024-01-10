""" Callbacks for the edit_password page"""

from dash.dependencies import Input, Output, State

from back.api.auth_routes import (get_id, is_user_authenticated)
from front.app import app
from front.auth import get_user_from_id, is_password_safe, edit_password


# vérifier la validité du nouveau mot de passe
@app.callback(
    [Output('new-password', 'valid'),
     Output('new-password', 'invalid'),
     Output('new-password-feedback-valid', 'children'),
     Output('new-password-feedback-invalid', 'children'),],
    [Input("new-password", "value")],
)
def check_new_password_validity(password):
    if not password:
        return False, False, '', ''
    safety, reason = is_password_safe(password)
    if not safety:
        return False, True, '', reason
    return True, False, reason, ''

# vérifier la validité de la confirmation du nouveau mot de passe
@app.callback(
    [Output('confirm-new-password', 'valid'),
     Output('confirm-new-password', 'invalid'),
     Output('confirm-new-password-feedback-valid', 'children'),
     Output('confirm-new-password-feedback-invalid', 'children'),],
    [Input("confirm-new-password", "value"),
     Input("new-password", "value")],
)
def check_confirm_new_password_validity(confirm_password, new_password):
    if not confirm_password:
        return False, False, '', ''
    if confirm_password != new_password:
        return False, True, '', 'Les mots de passe ne correspondent pas.'
    return True, False, '', ''


# callback pour activer/désactiver le bouton de modification du mot de passe
@app.callback(
    Output("edit-password-button", "disabled"),
    [Input("new-password", "valid"),
     Input("confirm-new-password", "valid"),
     Input("old-password", "value")],
)
def update_edit_password_button_state(valid_new_password, valid_confirm_password, old_password):
    if valid_new_password and valid_confirm_password and old_password:
        return False
    return True


# changer le mot de passe
@app.callback(
    Output('password-change-status', 'children'),
    [Input('edit-password-button', 'n_clicks')],
    [State('old-password', 'value'),
     State('new-password', 'value'),
     State('confirm-new-password', 'value')]
)
def change_password(n_clicks, old_password, new_password, confirm_new_password):
    if n_clicks > 0 and is_user_authenticated():
        user = get_user_from_id(get_id())
        print(user)
        if not user.check_password(old_password):
            return "Identifiants invalides."
        
        if new_password != confirm_new_password:
            return "Les nouveaux mots de passe ne correspondent pas."

        safety, reason = is_password_safe(new_password)
        if not safety:
            return reason
        if edit_password(user, new_password):
            return "Le mot de passe a été changé avec succès."
        return "Erreur lors de la mise à jour du mot de passe. Veuillez réessayer."
    return ""
