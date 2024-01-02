""" app routes"""
import re
import time
import os
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from itsdangerous import URLSafeTimedSerializer as Serializer

import dash
import dash_bootstrap_components as dbc
from dash import callback_context, dcc, html
from dash.dependencies import Input, Output, State
from flask import session
from flask_login import current_user, login_required, login_user, logout_user
import pandas as pd

from app import app
from auth import (
    create_user, is_email_allowed, is_email_registered,
    is_username_registered, is_password_safe, is_email_valid,
    create_deleted_user
)
import chat_agent as agent
from models import db, User, Queries, QueryResults, Contacts
from pages.header import header
from pages.navbar import navbar
from pages.footer import footer
from pages.home import home_layout
from pages.login import login_layout, user_layout
from pages.explorer import explorer_layout
from pages.profile import profile_layout
from pages.profile_history import profile_history_layout
from pages.profile_delete import profile_delete_account_layout
from pages.profile_edit import (
    profile_edit_layout, profile_edit_password_layout
)
from pages.unauthorized import unauthorized_layout
from pages.error_404 import error_404_layout
from pages.contact import contact_form_layout
from pages.forgot_password import forgot_password_layout
from pages.reset_password import reset_password_layout
from dotenv import load_dotenv

load_dotenv()

pages = ['/home', '/explorer', '/profile', '/login', '/profile/history', '/profile/edit', '/profile/edit/password']
open_pages = ['/home', '/login', '/', '/contact', '/forgot-password']

# Contenu principal
content = html.Div(id="page-content")

app.layout = html.Div(className='content-wrapper', children=[
    header,
    navbar,
    dcc.Store(id='redirect-url'),
    dcc.Location(id='url', refresh=False),
    content,
    footer
])



# call back pour afficher le layout en fonction de l'url
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def page_router(pathname):
    # Redirection pour les utilisateurs non authentifiés tentant d'accéder à des pages protégées
    if pathname.startswith('/reset_password/'):
        return reset_password_layout
    
    if pathname not in open_pages:
        if not current_user.is_authenticated:
            return unauthorized_layout

    # Gestion de l'affichage des pages
    if pathname in ('/home', '/'):
        return home_layout
    if pathname in ('/login', ):
        if current_user.is_authenticated:
            return user_layout
        return login_layout
    if pathname == '/explorer':
        return explorer_layout
    if pathname.startswith('/profile'):
        if pathname == '/profile/history':
            return profile_history_layout
        if pathname.startswith('/profile/edit'):
            if pathname.endswith('/password'):
                return profile_edit_password_layout
            return profile_edit_layout
        if pathname == '/profile/delete':
            return profile_delete_account_layout
        return profile_layout
    if pathname == '/contact':
        return contact_form_layout
    if pathname == '/forgot-password':
        return forgot_password_layout
    return error_404_layout


# callback pour mettre à jour le lien de connexion
@app.callback(
    Output('start-exploration-button', 'href'),
    [Input('url', 'pathname')],
)
def update_explorer_link(pathname):
    if pathname == '/home' and current_user.is_authenticated:
        return '/explorer'
    return '/login'

# Callback pour mettre à jour le contenu dynamique
@app.callback(
    Output('dynamic-username', 'children'),
    [Input('url', 'pathname')]
)
def update_dynamic_content(pathname):
    """
    """
    if pathname in pages:
        if current_user.is_authenticated:
            return dcc.Markdown(
                    f"Bienvenue **{current_user.username}**"
                )
    return dash.no_update


# Callback pour afficher les coordonnées de l'utilisateur
@app.callback(
    Output('profile-username', 'children'),
    Output('profile-email', 'children'),
    [Input('url', 'pathname'), Input('username-change-status', 'children'), Input('email-change-status', 'children')],
)
def update_edit_content(pathname, username_status, email_status):
    if pathname == '/profile/edit':
        if current_user.is_authenticated:
            return f"Nom d'utilisateur actuel : {current_user.username}", f"Email actuel : {current_user.email}"
    if username_status == "Le nom d'utilisateur a été changé avec succès.":
        return f"Nom d'utilisateur actuel : {current_user.username}", f"Email actuel : {current_user.email}"
    if email_status == "L'email a été changé avec succès.":
        return f"Nom d'utilisateur actuel : {current_user.username}", f"Email actuel : {current_user.email}"
    return dash.no_update

# callback pour activer/désactiver le bouton d'inscription
@app.callback(
    [Output('signup-button', 'disabled'), Output('signup-button', 'color')],
    [Input('signup-email', 'valid'), Input('signup-password', 'valid', ), Input('signup-name', 'valid')]
)
def update_signup_button_state(valid_email, valid_password, valid_name):
    if valid_email and valid_password and valid_name:
        return False, 'primary'  # Active le bouton
    return True, 'info'  # Désactive le bouton


# callback pour activer/désactiver le bouton de connexion
@app.callback(
    Output('login-button', 'disabled'), Output('login-button', 'color'),
    [Input('login-email', 'valid'), Input('login-password', 'value')]
)
def update_login_button_state(valid_email, password):
    if valid_email and password :  # Vérifie si les champs ne sont pas vides
        return False, 'primary'  # Active le bouton
    return True, 'info'  # Désactive le bouton


# callback pour créer un compte
@app.callback(
    Output('signup-status', 'children'),
    [Input('signup-button', 'n_clicks')],
    [State('signup-name', 'value'),
     State('signup-email', 'value'),
     State('signup-password', 'value')]
)
def create_account(n_clicks, name, email, password):
    if n_clicks is None or not email or not password:
        return dash.no_update

    if is_email_registered(email):
        return 'Un compte existe déjà avec cette adresse e-mail.'

    if is_username_registered(name):
        return 'Ce nom d\'utilisateur est déjà utilisé. Veuillez en choisir un autre'

    # Vérifier si l'email est autorisé
    if not is_email_allowed(email):
        return 'Adresse email non autorisée. Vous ne pouvez pas créer de compte.'

    # Créer l'utilisateur
    if create_user(name, email, password):
        return 'Compte créé avec succès. Vous pouvez maintenant vous connecter.'

    return 'Erreur lors de la création du compte.'


# callback pour se connecter
@app.callback(
    Output('login-status', 'children'), Output('redirect-url', 'data'),
    [Input('login-button', 'n_clicks'), Input('login-password', 'value'),],
    [State('login-email', 'value'), State('login-password', 'value'),]
)
def login(n_clicks, password_edit, email, password):
    ctx = callback_context
    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate
    
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if trigger_id == 'login-button':
        if n_clicks > 0:
            user = User.query.filter_by(email=email).first()

            if user.id == 0:   # Compte supprimé
                return "Identifiants invalides", dash.no_update

            if user and user.check_password(password):
                login_user(user)
                return "Vous êtes connecté.", "/login"

            return html.Div([
                html.P("Mot de passe invalide.", className='text-danger'),
            ]), dash.no_update        
        return "", dash.no_update
    if trigger_id == 'login-password':
        return "", dash.no_update


# callback pour se déconnecter
@app.callback(
    Output('logout-content', 'children'),
    [Input('logout-button', 'n_clicks')],
    prevent_initial_call=True,
)
def logout(n_clicks):
    if n_clicks > 0:
        logout_user()

        return html.Div([
                html.P("Vous n'êtes plus connecté."),
            ])
    return dash.no_update


@app.callback(
    Output('url', 'pathname'),
    [Input('redirect-url', 'data')]
)
def redirect(pathname):
    return pathname if pathname else dash.no_update


# # callback pour modifier le layout quand l'utilisateur est connecté/déconnecté
# @app.callback(
#     Output('login-card-container', 'style'),
#     Output('login-card-container-logged', 'style'),
#     [Input('login-button', 'n_clicks'), Input('logout-button', 'n_clicks')],
#     # prevent_initial_call=True
# )
# def update_forms_and_message(login_n_clicks, logout_n_clicks):

#     if current_user.is_authenticated:
#         return {'display': 'none'}, {'display': 'flex'}
#     return {'display': 'flex'}, {'display': 'none'}


# vérifier la validité du nom d'inscription
@app.callback(
    [Output("signup-name", "valid"), Output("signup-name", "invalid")],
    [Input("signup-name", "value")],
)
def check_username_validity(name):
    if not name:
        return False, False
    if is_username_registered(name):
        return False, True
    return True, False

# vérifier la validité de l'email d'inscription
@app.callback(
    [Output("signup-email", "valid"),
     Output("signup-email", "invalid"),
     Output("email-feedback-valid", "children"),
     Output("email-feedback-invalid", "children")],
    [Input("signup-email", "value")],
)
def check_email_validity(email):
    if not email:
        return False, False, '', ''
    if not is_email_valid(email):
        return False, True, '', 'Adresse email invalide.'
    if is_email_registered(email):
        return False, True, '', 'Un compte existe déjà avec cette adresse e-mail.'
    if not is_email_allowed(email):
        return False, True, '', 'Adresse email non autorisée. Vous ne pouvez pas créer de compte.'
    return True, False, 'Adresse email valide.', ''

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

# vérifier la validité de l'email de connexion
@app.callback(
    [Output("login-email", "valid"),
     Output("login-email", "invalid"),
     Output("login-email-valid", "children"),
     Output("login-email-invalid", "children")],
    [Input("login-email", "value")],
)
def check_login_email_validity(email):
    if not email:
        return False, False, '', ''
    if not is_email_valid(email):
        return False, True, '', 'Adresse email invalide.'
    if not is_email_registered(email):
        return False, True, '', 'Adresse email non reconnue.'
    return True, False, 'Adresse email valide.', ''

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
        return False, True, '', 'Adresse email invalide.'
    # if not is_email_registered(email):
    #     return False, True, '', 'Adresse email non reconnue.'
    return True, False, 'Adresse email valide.', ''

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


# changer le mot de passe
@app.callback(
    Output('password-change-status', 'children'),
    [Input('edit-password-button', 'n_clicks')],
    [State('old-password', 'value'),
     State('new-password', 'value'),
     State('confirm-new-password', 'value')]
)
def change_password(n_clicks, old_password, new_password, confirm_new_password):
    if n_clicks > 0 and current_user.is_authenticated:
        user = User.query.filter_by(id=current_user.id).first()
        if not user.check_password(old_password):
            return "L'ancien mot de passe est incorrect."
        
        if new_password != confirm_new_password:
            return "Les nouveaux mots de passe ne correspondent pas."

        safety, reason = is_password_safe(new_password)
        if not safety:
            return reason
        try :
            user.set_password(new_password)
            db.session.commit()
            return "Le mot de passe a été changé avec succès."
        except Exception as e:
            print(e)
            return "Erreur lors de la mise à jour du mot de passe. Veuillez réessayer."
    return ""


# callback pour modifier le nom d'utilisateur
@app.callback(
    Output('username-change-status', 'children'),
    [Input('edit-username-button', 'n_clicks')],
    [State('new-username', 'value')]
)
def change_username(n_clicks, new_username):
    if new_username and n_clicks > 0 and current_user.is_authenticated:
        user = User.query.filter_by(id=current_user.id).first()
        if is_username_registered(new_username):
            return "Ce nom d'utilisateur est déjà utilisé. Veuillez en choisir un autre"

        user.username = new_username
        db.session.commit()
        return "Le nom d'utilisateur a été changé avec succès."

    return ""

# callback pour modifier l'email
@app.callback(
    Output('email-change-status', 'children'),
    [Input('edit-email-button', 'n_clicks')],
    [State('new-email', 'value')]
)
def change_email(n_clicks, new_email):
    if new_email and n_clicks > 0 and current_user.is_authenticated:
        user = User.query.filter_by(id=current_user.id).first()
        if not is_email_valid(new_email):
            return "Adresse email invalide."

        if is_email_registered(new_email):
            return "Un compte existe déjà avec cette adresse e-mail."

        if not is_email_allowed(new_email):
            return "Adresse email non autorisée. Vous ne pouvez pas créer de compte."

        user.email = new_email
        db.session.commit()
        return "L'email a été changé avec succès."

    return ""

# Callback pour la recherche dans la base de données spectre
@app.callback(
    [Output("search-result", "children"),
     Output("search-button", "n_clicks"),
    Output("query-card-container", "style")
     ],
    [Input("query", "value"), Input("search-button", "n_clicks")],
    prevent_initial_call=True
)
def ask_spectre_database(query, n_clicks):
    if n_clicks > 0:
        query_result, total_tokens, prompt_tokens, completion_tokens, total_cost, execution_time = agent.query_database(query)
        
        # Enregistrer la requête en base de données
        query_data = {
            'query_text': query,
            'user_id': current_user.id,  # Assurez-vous d'avoir accès à l'ID de l'utilisateur actuel
            'prompt_tokens': prompt_tokens,
            'completion_tokens': completion_tokens,
            'total_tokens': total_tokens,
            'cost': total_cost
        }
        try:
            response = requests.post('http://127.0.0.1:8050/api/record_query', json=query_data, timeout=60)  # Mettez à jour l'URL selon votre configuration
            print(response.json(), flush=True)
        except requests.RequestException as e:
            print(e, flush=True)
            return e, 0
                
        if response.ok:
            try:
                query_id = response.json().get('query_id')
            except requests.RequestException as e:
                print(e, flush=True)
                return e, 0
        # Enregistrer les résultats en base de données
            result_data = {
                'query_id': query_id,  # Vous devez récupérer l'ID de la requête que vous venez d'enregistrer
                'result': query_result,
                'execution_time': execution_time,  # Calculez le temps d'exécution si nécessaire
            }
            try:
                response = requests.post('http://127.0.0.1:8050/api/record_query_result', json=result_data, timeout=60)
                print(response.json(), flush=True)
            except requests.RequestException as e:
                print(e, flush=True)
                return e, 0
        # time.sleep(5)
        # query_result = query
        return [dcc.Markdown(query_result)], 0, {'display': 'flex'}

    return "", 0, {'display': 'none'}


@app.callback(
    Output('history-table', 'children'),
    [Input('url', 'pathname')]
)
def update_history_table(pathname):
    if pathname == '/profile/history':
        try:
            # Utilisez les cookies de session pour maintenir le contexte utilisateur
            # with requests.Session() as s:
            #     s.cookies.update(session)
            #     response = s.get(
            #         'http://127.0.0.1:8050/api/get_user_history',
            #         timeout=180
            #     )
            response = requests.get(
                'http://127.0.0.1:8050/api/get_user_history',
                params={'user_id': current_user.id},
                timeout=180
            )
            print(response.status_code, flush=False)
            # print(response.json(), flush=False)
            # print(response.text, flush=False)
            if response.status_code == 200:
                print("Request status :", response.status_code, "\nQuery history is accessible", flush=True)
                try:
                    history_data = response.json()
                    rows = []
                    for entry in history_data:
                        row = html.Tr([
                            html.Td(entry['date']),
                            html.Td(entry['query']),
                            html.Td(entry['response'])
                        ])
                        rows.append(row)
                    if rows == []:
                        return html.Tr([
                            html.Td("Aucune requête enregistrée."),
                            html.Td(""),
                            html.Td("")
                        ])
                    return rows
                except ValueError:
                    print("La réponse n'est pas au format JSON")
                    return []
            else:
                print(f"Erreur API: {response.status_code}")
                return []
        except requests.RequestException as e:
            print(f"Erreur requête: {e}", flush=True)
            return []
    return []


@app.callback(
    Output('delete-confirm', 'children'),
    Output('delete-account-button', 'n_clicks'),
    [Input('delete-account-button', 'n_clicks')],
    [State('delete-account-text', 'value'),
     State('delete-account-password', 'value'),
     State('delete-account-text-display', 'children')],
    prevent_initial_call=True
)
def delete_account(n_clicks, text, password, text_display):
    if n_clicks > 0 and current_user.is_authenticated:
        if not password:
            return 'Veuillez entrer votre mot de passe.', 0
        if not text:
            return 'Veuillez entrer le texte de confirmation.', 0
        if text != text_display:
            return 'Veuillez corriger le texte de confirmation.', 0
        if not current_user.check_password(password):
            return 'Mot de passe invalide.', 0
        if n_clicks == 1:
            return 'Etes-vous sûr de vouloir supprimer votre compte ? Cette action est irréversible. Cliquez à nouveau sur le bouton pour confirmer.', 1
        if n_clicks > 1:
            user_id = current_user.id

            # Identify the user to delete
            user_to_delete = User.query.get(user_id)
            
            if user_to_delete:
                        
                # if not exist create a deleted user
                create_deleted_user()

                # update queries and contacts tables with deleted user id
                deleted_user_id = User.query.filter_by(
                    username='deletedUser'
                ).first().id
                queries_to_update = Queries.query.filter_by(
                    user_id=user_id
                ).all()
                for query_row in queries_to_update:
                    query_row.user_id = deleted_user_id
                db.session.commit()

                contacts_to_update = Contacts.query.filter_by(
                    user_id=user_id
                ).all()
                for contact_row in contacts_to_update:
                    contact_row.user_id = deleted_user_id
                db.session.commit()

                # Supprimer l'utilisateur
                db.session.delete(user_to_delete)
                db.session.commit()
                logout_user()
                return 'Compte utilisateur supprimé avec succès.', 0
            
            return 'Erreur: Utilisateur non trouvé.', 0
        
    return 'Vous devez être connecté pour supprimer votre compte.', 0


# Callback pour télécharger l'historique de l'utilisateur
import pandas as pd
from dash.dependencies import Input, Output

@app.callback(
    Output('download-data', 'data'),
    [Input('download-button', 'n_clicks')],
    [State('format-select', 'value')],
    prevent_initial_call=True
)
def generate_file(n_clicks, file_format):
    if n_clicks > 0:
        if current_user.is_authenticated:
            # Récupérer les données de l'utilisateur
            user_id = current_user.id
            user_queries = Queries.query.filter_by(user_id=user_id).all()
            history = {'Date': [], 'Requête': [], 'Réponse': []}
            for query_info in user_queries:
                query_result = QueryResults.query.filter_by(query_id=query_info.id).first()
                history['Date'].append(query_info.time_created.strftime("%d/%m/%Y - %H:%M:%S"))
                history['Requête'].append(query_info.query_text)
                history['Réponse'].append(query_result.result if query_result else 'No response')

            print(history, flush=True)
            # Convertir les données en DataFrame Pandas
            df = pd.DataFrame.from_dict( history)

            # Générer le fichier en fonction du format sélectionné
            if file_format == 'csv':
                return dcc.send_data_frame(df.to_csv, filename="historique_requetes.csv")
            elif file_format == 'xlsx':
                return dcc.send_data_frame(df.to_excel, filename="historique_requetes.xlsx", index=False)
    return dash.no_update


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
        if current_user.is_authenticated:
            user_id = current_user.id
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
    [State('new-password-reset', 'value'), State('confirm-new-password-reset', 'value'), State('url', 'pathname')],
    prevent_initial_call=True,
)
def reset_password(n_clicks, new_password, confirm_new_password, pathname):
    if n_clicks > 0:
        try:
            token = pathname.split('/')[-1]  # Extraire le token de l'URL
            # Ajoutez ici la logique pour vérifier le token et réinitialiser le mot de passe
            s = Serializer(app.server.secret_key)
            email = s.loads(token, salt='password-reset-salt', max_age=3600)
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
        try:
            user = User.query.filter_by(email=email).first()
            user.set_password(new_password)
            db.session.commit()
        except Exception as e:
            print(e)
            return "Erreur lors de la mise à jour du mot de passe. Veuillez réessayer."
        return "Votre mot de passe a été réinitialisé."
    return ""

