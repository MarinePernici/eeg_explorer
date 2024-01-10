""" callback for the contact form"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests
from dash.dependencies import Input, Output, State
from dotenv import load_dotenv

from back.api.auth_routes import get_id, is_user_authenticated
from front.app import app

load_dotenv()


# Callback pour enregistrer un message de contact
@app.callback(
    Output('form-output', 'children'),  # Vous pouvez ajouter un élément pour afficher un message de confirmation
    [Input('contact-submit', 'n_clicks')],
    [State('contact-name', 'value'),
     State('contact-email', 'value'),
     State('contact-subject', 'value'),
     State('contact-message', 'value')]
)
def handle_form_submission(n_clicks, name, email, subject, message):
    if n_clicks is None:
        return None  # Pas d'action si le bouton n'a pas été cliqué

    # Ici, vous pouvez ajouter la logique pour enregistrer les données dans une base de données
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
            response = requests.post('http://127.0.0.1:8050/api/record_contact', json=contact_data, timeout=60)
            print(response.json(), flush=True)
        except requests.RequestException as e:
            print(e, flush=True)
            return f"Erreur lors de l'enregistrement du message : {e}"

    # Exemple de logique pour envoyer un email (à adapter selon votre configuration SMTP)
        try:
            msg = MIMEMultipart()
            msg['Subject'] = 'Contact EEG Explorer'  # Définir l'objet de l'email

            # Ajouter le nom, l'email et le message de l'expéditeur dans le corps de l'email
            body = f"Message reçu via le formulaire de contact EEG Explorer\n\nNom : {name}\nEmail : {email}\nSujet : {subject}\nMessage :\n{message}"
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(
                os.environ.get('email_contact'),
                os.environ.get('email_password')
            )
            server.sendmail(
                from_addr=os.environ.get('email_contact'),
                to_addrs=os.environ.get('email_contact'),
                msg=msg.as_string()
            )
            server.quit()
            return 'Bien reçu! Nous vous répondrons dès que possible.'
        except Exception as e:
            return f'Erreur lors de l\'envoi du message : {e}'
    except Exception as e:
        return f"Erreur lors du traitement de votre demande : {e}"
