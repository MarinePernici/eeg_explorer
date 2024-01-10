
import requests
import json

import dash
from dash import dcc
from dash.dependencies import Input, Output, State

from back.api.auth_routes import get_id
from front.app import app
import back.api.chat_agent as agent
from front.functions.explorer_functions import is_query_safe


#Callback pour activer/désactiver le bouton de recherche
@app.callback(
    Output("search-button", "disabled"),
    [Input("query", "value")],
)
def update_search_button_state(query):
    if query:
        return False
    return True


# Callback pour la recherche dans la base de données spectre
@app.callback(
    [Output("search-result", "children"),
     Output("query", "value"),
     Output("query-card-container", "style")
     ],
    [Input("search-button", "n_clicks")],
    [State("query", "value")],
    prevent_initial_call=True
)
def ask_spectre_database(n_clicks, query):
    if n_clicks > 0:
        is_safe, message = is_query_safe(query)
        if not is_safe:
            query_result = message
            total_tokens = 0
            prompt_tokens = 0
            completion_tokens = 0
            total_cost = 0
            execution_time = 0
        else:
        
            query_result, total_tokens, prompt_tokens, completion_tokens, total_cost, execution_time = agent.query_database(query)
        
        # Enregistrer la requête en base de données
        query_data = {
            'query_text': query,
            'user_id': get_id(),  # Assurez-vous d'avoir accès à l'ID de l'utilisateur actuel
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
            return "Une erreur s'est produite", "", {'display': 'flex'}
                
        if response.ok:
            try:
                query_id = response.json().get('query_id')
            except requests.RequestException as e:
                print(e, flush=True)
                return "Une erreur s'est produite", "", {'display': 'flex'}
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
                return "Une erreur s'est produite", "", {'display': 'flex'}
        # time.sleep(5)
        # query_result = query
        return [dcc.Markdown(query_result)], "", {'display': 'flex'}

    return "", "", {'display': 'none'}
