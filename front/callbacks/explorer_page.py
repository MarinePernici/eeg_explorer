
import requests
import json

import dash
from dash import dcc
from dash.dependencies import Input, Output, State

from back.api.auth_routes import get_id
from front.app import app
import back.chat_agent as agent
from front.functions.explorer_functions import is_query_safe
from back.api.auth import (
    post_query_in_db, get_query_id, post_query_result_in_db
)


# Callback pour activer/désactiver le bouton de recherche
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
     Output('query-reminder', 'children'),
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
            total_tokens = None
            prompt_tokens = None
            completion_tokens = None
            total_cost = None
            execution_time = 0
            query_registered = message
        else:
            (
                query_result, total_tokens,
                prompt_tokens, completion_tokens,
                total_cost, execution_time
            ) = agent.query_database(query)
            query_registered = query

        reminder = f"Votre question était : {query}"

        error = (
            "Une erreur s'est produite",
            reminder,
            "",
            {'display': 'flex'}
        )
        # Enregistrer la requête en base de données
        query_data = {
            'query_text': query_registered,
            'user_id': get_id(),
            'prompt_tokens': prompt_tokens,
            'completion_tokens': completion_tokens,
            'total_tokens': total_tokens,
            'cost': total_cost
        }

        try:
            response = post_query_in_db(
                query_data,
            )
        except Exception as e:
            print(e, flush=True)
            return error

        if response.ok:
            try:
                query_id = get_query_id(response)
            except requests.RequestException as e:
                print(e, flush=True)
                return error
        # Enregistrer les résultats en base de données
        result_data = {
            'query_id': query_id,
            'result': query_result,
            'execution_time': execution_time,
        }
        try:
            response = post_query_result_in_db(result_data)

        except requests.RequestException as e:
            print(e, flush=True)
            return error
        if response.ok:
            return (
                [dcc.Markdown(query_result)],
                reminder,
                "",
                {'display': 'flex'}
            )
        return error

    return "", "", "", {'display': 'none'}
