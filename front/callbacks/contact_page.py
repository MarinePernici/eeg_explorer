""" callback for the contact form"""

import os

import dash
import requests
from dash.dependencies import Input, Output, State
from dotenv import load_dotenv

from back.api.auth import post_data_in_db, send_contact_email
from back.api.auth_routes import get_id, is_user_authenticated
from front.app import app
from front.functions.validity_functions import is_email_valid

load_dotenv()


# callback pour vérifier la validité de l'email
@app.callback(
    Output("contact-email", "valid"),
    Output("contact-email", "invalid"),
    Output("contact-email-feedback-valid", "children"),
    Output("contact-email-feedback-invalid", "children"),
    [Input("contact-email", "value")],
)
def update_contact_email_validity(email):
    if email is None:
        return False, False, "", ""
    if not email:
        return False, False, "", ""
    if is_email_valid(email):
        return True, False, "Adresse email valide", ""
    return False, True, "", "Adresse email invalide"


# callback pour activé/désactivé le bouton d'envoi du message
@app.callback(
    Output("contact-submit", "disabled"),
    [Input("contact-name", "value"),
     Input("contact-email", "valid"),
     Input("contact-subject", "value"),
     Input("contact-message", "value")],
)
def update_contact_submit_button_state(name, valid_email, subject, message):
    if name and valid_email and subject and message:
        return False
    return True


# Callback pour enregistrer un message de contact
@app.callback(
    Output('form-output', 'children'),
    [Input('contact-submit', 'n_clicks')],
    [State('contact-name', 'value'),
     State('contact-email', 'value'),
     State('contact-subject', 'value'),
     State('contact-message', 'value')]
)
def handle_form_submission(n_clicks, name, email, subject, message):
    if n_clicks == 0:
        return None  # Pas d'action si le bouton n'a pas été cliqué

    if not name or not email or not subject or not message:
        return 'Veuillez remplir tous les champs du formulaire.'

    if not is_email_valid(email):
        return 'Veuillez entrer une adresse email valide.'

    try:
        if is_user_authenticated():
            user_id = get_id()
        else:
            user_id = None

        contact_data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
            'user_id': user_id
        }
        try:
            post_data_in_db(data=contact_data, route='record_contact')
        except requests.RequestException as e:
            print(
                f"Erreur lors de l'enregistrement du message : {e}",
                flush=True
            )
            return f"""
            Erreur lors de l'enregistrement du message, veuillez réessayer.
            Si le problème persiste, veuillez nous contacter à l'adresse
            suivante : {os.environ.get('email_contact')}
            """

        try:
            send_contact_email(name, email, subject, message)
            return 'Bien reçu! Nous vous répondrons dès que possible.'
        except Exception as e:
            print(
                f'Erreur lors de l\'envoi du message : {e}',
                flush=True
            )
            return f"""
            Erreur lors de l\'envoi du message, veuillez réessayer.
            Si le problème persiste, veuillez nous contacter à l'adresse
            suivante : {os.environ.get('email_contact')}
            """
    except Exception as e:
        print(
            f'Erreur lors du traitement de la demande : {e}',
            flush=True
        )
        return f"""
        Erreur lors du traitement de votre demande, veuillez réessayer.
        Si le problème persiste, veuillez nous contacter à l'adresse 
        suivante : {os.environ.get('email_contact')}
        """


# callback pour supprimer les valeurs du formulaire après envoi
@app.callback(
    Output('contact-name', 'value'),
    Output('contact-email', 'value'),
    Output('contact-subject', 'value'),
    Output('contact-message', 'value'),
    [Input('form-output', 'children')],
    prevent_initial_call=True
)
def clear_form_output(form_output):
    if form_output == 'Bien reçu! Nous vous répondrons dès que possible.':
        return "", "", "", ""
    return dash.no_update, dash.no_update, dash.no_update, dash.no_update
