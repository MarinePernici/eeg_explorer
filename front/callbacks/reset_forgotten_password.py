
import dash
from dash.dependencies import Input, Output, State

from front.app import app
from back.api.auth import (
    get_user_from_email,
    is_email_registered, edit_password
)
from front.functions.validity_functions import is_email_valid, is_password_safe


import os
import smtplib
from email.mime.text import MIMEText
from itsdangerous import URLSafeTimedSerializer as Serializer

from dotenv import load_dotenv

load_dotenv()


# vérifier la validité de l'email de réinitialisation du mot de passe
@app.callback(
    [Output("user-email", "valid"),
     Output("user-email", "invalid"),
     Output("user-email-valid", "children"),
     Output("user-email-invalid", "children")],
    [Input("user-email", "value")],
)
def check_user_email_validity(email):
    if not email:
        return False, False, '', ''
    if not is_email_valid(email):
        return False, True, '', 'Ceci n\'est pas une adresse mail.'
    return True, False, '', ''


# callback pour activer/désactiver le bouton de réinitialisation du mot de passe
@app.callback(
    Output("forgot-password-button", "disabled"),
    [Input("user-email", "valid")],
)
def update_forgot_password_button_state(valid_email):
    if valid_email:
        return False
    return True


# Callback pour envoyer un email de réinitialisation de mot de passe
@app.callback(
    Output('forgot-password-message', 'children'),
    [Input('forgot-password-button', 'n_clicks')],
    [State('user-email', 'value')]
)
def send_reset_password_email(n_clicks, email):
    if n_clicks > 0:
        if is_email_registered(email):
            s = Serializer(app.server.secret_key)
            token = s.dumps(email, salt='password-reset-salt')

            try:
                # Préparer le message email
                lien = f"http://127.0.0.1:8050/reset_password/{token}"
                msg_body = f"""
                Bonjour,
                
                Vous recevez cet email car nous avons reçu une demande de réinitialisation du mot de passe pour votre compte EEG Explorer.
                
                Pour réinitialiser votre mot de passe, veuillez cliquer sur le lien ci-dessous :
                {lien}

                Si vous rencontrez des problèmes pour cliquer sur le lien, copiez et collez l'URL dans votre navigateur
                
                Ce lien de réinitialisation est valide pendant 15 minutes. Passé ce délai, il sera nécessaire de soumettre une nouvelle demande de réinitialisation de mot de passe.
                
                Si vous n'avez pas demandé cette réinitialisation, veuillez ignorer cet email. Aucune modification ne sera apportée à votre compte.
                
                L'équipe EEG Explorer
                """
                msg = MIMEText(msg_body)
                msg['Subject'] = 'Réinitialisation de votre mot de passe EEG Explorer'
                msg['From'] = os.environ.get('email_contact')
                msg['To'] = email

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(os.environ.get('email_contact'), os.environ.get('email_password'))
                server.sendmail(os.environ.get('email_contact'), email, msg.as_string())
                server.quit()

                return "Si votre compte existe, un email de réinitialisation a été envoyé."
            except Exception as e:
                return f"Erreur lors de l'envoi de l'email : {e}"

        return "Si votre compte existe, un email de réinitialisation a été envoyé."
    return ""
    
# Callback pour réinitialiser le mot de passe
@app.callback(
    Output('reset-password-message', 'children'),
    [Input('reset-password-button', 'n_clicks')],
    [State('new-password-reset', 'value'),
     State('confirm-new-password-reset', 'value'),
     State('url', 'pathname')],
    prevent_initial_call=True,
)
def reset_password(n_clicks, new_password, confirm_new_password, pathname):
    if n_clicks > 0:
        try:
            token = pathname.split('/')[-1]  # Extraire le token de l'URL
            # Ajoutez ici la logique pour vérifier le token et réinitialiser le mot de passe
            s = Serializer(app.server.secret_key)
            email = s.loads(token, salt='password-reset-salt', max_age=900)
        except Exception as e:
            print(e)
            return "Ce lien de réinitialisation est invalide ou a expiré."
        if not is_email_registered(email):
            return "Email non reconnu."
        if new_password != confirm_new_password:
            return "Les nouveaux mots de passe ne correspondent pas."
        safety, reason = is_password_safe(new_password)
        if not safety:
            return reason

        user = get_user_from_email(email)
        if edit_password(user, new_password):
            return "Votre mot de passe a été réinitialisé."
        return "Erreur lors de la mise à jour du mot de passe. Veuillez réessayer."
    return ""

# Callback pour vérifier la validité du nouveau mot de passe
@app.callback(
    [Output("new-password-reset", "valid"),
     Output("new-password-reset", "invalid"),
     Output("new-password-reset-feedback-valid", "children"),
     Output("new-password-reset-feedback-invalid", "children")],
    [Input("new-password-reset", "value")],
)
def check_new_password_validity(password):
    if not password:
        return False, False, '', ''
    safety, reason = is_password_safe(password)
    if not safety:
        return False, True, '', reason
    return True, False, '', ''


# Callback pour vérifier la validité de la confirmation du nouveau mot de passe
@app.callback(
    [Output("confirm-new-password-reset", "valid"),
     Output("confirm-new-password-reset", "invalid"),
     Output("confirm-new-password-reset-feedback-valid", "children"),
     Output("confirm-new-password-reset-feedback-invalid", "children")],
    [Input("confirm-new-password-reset", "value"),
     Input("new-password-reset", "value")],
)
def check_confirm_new_password_validity(confirm_password, password):
    if not confirm_password:
        return False, False, '', ''
    if confirm_password == password:
        return True, False, '', ''
    return False, True, '', 'Les mots de passe ne correspondent pas.'


# Callback pour activer/désactiver le bouton de réinitialisation du mot de passe
@app.callback(
    Output("reset-password-button", "disabled"),
    [Input("new-password-reset", "valid"),
     Input("confirm-new-password-reset", "valid")],
)
def update_reset_password_button_state(valid_password, valid_confirm_password):
    if valid_password and valid_confirm_password:
        return False
    return True


# Callback pour reinitialiser les valeurs des champs de mot de passe
@app.callback(
    Output("new-password-reset", "value"),
    Output("confirm-new-password-reset", "value"),
    [Input("reset-password-button", "n_clicks")],
)
def reset_password_inputs(n_clicks):
    if n_clicks > 0:
        return "", ""
    return dash.no_update, dash.no_update