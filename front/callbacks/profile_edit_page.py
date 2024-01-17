""" Callbacks for the profile edit page"""

from collections import Counter
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

import dash
from dash.dependencies import Input, Output, State

from back.api.auth_routes import get_username, is_user_authenticated, get_id
from front.app import app
from back.api.auth import (
    get_user_from_id, edit_username, get_user_history
)
from front.functions.validity_functions import is_username_valid

# Callback to display the current username on the profile edit page
@app.callback(
    Output('profile-username', 'children'),
    [
        Input('url', 'pathname'),
        Input('username-change-status', 'children'),
    ],
)
def update_edit_content(pathname, change_status):
    """
    Display the current username and email on the profile edit page

    Args:
        pathname (str): current url path
        username_status (str): username change status
        email_status (str): email change status

    Returns:
        str: username and email to display
    """
    if pathname == '/profile/edit' or change_status:
        if is_user_authenticated():
            return f"Nom d'utilisateur actuel : {get_username()}"

    return dash.no_update


# callback pour modifier le nom d'utilisateur
@app.callback(
    Output('username-change-status', 'children'),
    Output('username-change-margin', 'className'),
    [Input('edit-username-button', 'n_clicks')],
    [State('new-username', 'value')]
)
def change_username(n_clicks, new_username):
    if new_username and n_clicks > 0 and is_user_authenticated():
        
        validity, reason = is_username_valid(new_username)
        if not validity:
            return reason, "mb-3"
        
        user = get_user_from_id(get_id())

        if edit_username(user, new_username):
            return "Le nom d'utilisateur a été changé avec succès.", "mb-3"
        return "Une erreur est survenue lors du changement de nom d'utilisateur.", "mb-3"

    return "", dash.no_update


# vérifier la validité du nouveau nom
@app.callback(
    [Output("new-username", "valid"),
     Output("new-username", "invalid"),
     Output("new-username-feedback-valid", "children"),
     Output("new-username-feedback-invalid", "children")],
    [Input("new-username", "value")],
)
def check_username_validity(name):
    if not name:
        return False, False, '', ''
    
    validity, reason = is_username_valid(name)
    if not validity:
        return False, True, '', reason

    return True, False, reason, ''


# callback pour activer/désactiver le bouton de changement de nom
@app.callback(
    Output("edit-username-button", "disabled"),
    [Input("new-username", "valid")],
)
def update_edit_username_button_state(username_valid):
    if username_valid:
        return False
    return True


# afficher le plot des utilisations
@app.callback(
    Output('profile-graph', 'figure'),
    [Input('url', 'pathname')]
)
def update_profile_graph(pathname):
    if pathname == '/profile/edit' and is_user_authenticated():
        try:
            response = get_user_history(get_id())
            if response.status_code == 200:
                print("Statistics are accessibles", flush=True)
                try:
                    history_data = response.json()
                    dates = []
                    for entry in history_data:
                        date = datetime.strptime(
                            entry['date'].split(' ')[0],
                            '%d/%m/%Y'
                        ).date()
                        dates.append(date)
                    if not dates:
                        return dash.no_update
                    data = Counter(dates)

                    # Générer toutes les dates pour les 30 derniers jours
                    end_date = datetime.now().date()
                    start_date = end_date - timedelta(days=30)
                    all_dates = pd.date_range(
                        start=start_date,
                        end=end_date,
                        freq='D'
                    ).date

                    # Créer un DataFrame avec toutes les dates et les comptes
                    df = pd.DataFrame(
                        {'Date': all_dates, 'Nombre de Requêtes': 0}
                    )
                    for date, count in data.items():
                        df.loc[df['Date'] == date, 'Nombre de Requêtes'] = count
                    
                    fig = px.line(
                        df,
                        x='Date',
                        y='Nombre de Requêtes',
                        title='Votre activité sur EEG Explorer ces 30 derniers jours'
                    )
                    fig.update_layout(
                        xaxis_tickangle=-45,
                        paper_bgcolor='#1a1950',
                        title_font_color='white',
                        xaxis_title_font_color='white',
                        yaxis_title_font_color='white',
                        xaxis_tickfont_color='white',
                        yaxis_tickfont_color='white',
                    )
                    return fig
                except ValueError:
                    print("La réponse n'est pas au format JSON")
                    return {}
            else:
                print(f"Erreur API: {response.status_code}")
                return {}
        except Exception as e:
            print(f"Erreur requête: {e}", flush=True)
            return {}
    return dash.no_update






    return dash.no_update