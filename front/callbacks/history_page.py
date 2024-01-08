
import requests
import json

import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
from flask_login import current_user

from back.api.auth_routes import (get_id, get_username, get_email,
                                  is_user_authenticated)
from front.app import app
from front.auth import get_user_from_id, is_password_safe, edit_password,  get_queries_from_user_id, get_query_result_from_id
from front.models import User, db
import front.chat_agent as agent
import pandas as pd


@app.callback(
    Output('history-table', 'children'),
    [Input('url', 'pathname')]
)
def update_history_table(pathname):
    if pathname == '/profile/history':
        try:
            response = requests.get(
                'http://127.0.0.1:8050/api/get_user_history',
                params={'user_id': get_id()},
                timeout=180
            )
            print(response.status_code, flush=False)
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
                    if not rows:
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
    Output('download-data', 'data'),
    [Input('download-button', 'n_clicks')],
    [State('format-select', 'value')],
    prevent_initial_call=True
)
def generate_file(n_clicks, file_format):
    if n_clicks > 0:
        if is_user_authenticated():
            # Récupérer les données de l'utilisateur
            user_id = get_id()
            user_queries = get_queries_from_user_id(user_id)
            history = {'Date': [], 'Requête': [], 'Réponse': []}
            for query_info in user_queries:
                query_result = get_query_result_from_id(query_info.id)
                history['Date'].append(query_info.time_created.strftime("%d/%m/%Y - %H:%M:%S"))
                history['Requête'].append(query_info.query_text)
                history['Réponse'].append(query_result.result if query_result else 'No response')

            print(history, flush=True)
            # Convertir les données en DataFrame Pandas
            df = pd.DataFrame.from_dict(history)

            # Générer le fichier en fonction du format sélectionné
            if file_format == 'csv':
                return dcc.send_data_frame(df.to_csv, filename="historique_requetes.csv", index=False)
            if file_format == 'xlsx':
                return dcc.send_data_frame(df.to_excel, filename="historique_requetes.xlsx", index=False)
            
    return dash.no_update
