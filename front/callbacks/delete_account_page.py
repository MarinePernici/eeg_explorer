""" callback for the delete account page"""

import dash
from dash.dependencies import Input, Output, State

from back.api.auth_routes import (get_id,
                                  is_user_authenticated)
from front.app import app
from front.auth import (
    get_user_from_id,
    get_user_from_username,
    get_queries_from_user_id,
    get_contacts_from_user_id,
    create_deleted_user,
    verify_password,
    update_user_id,
    delete_user

)


@app.callback(
    Output('delete-confirm', 'children'),
    Output('delete-account-button', 'n_clicks'),
    Output('delete-account-text', 'value'),
    Output('delete-account-password', 'value'),
    [Input('delete-account-button', 'n_clicks')],
    [State('delete-account-text', 'value'),
     State('delete-account-password', 'value'),
     State('delete-account-text-display', 'children')],
    prevent_initial_call=True
)
def delete_account(n_clicks, text, password, text_display):
    if n_clicks > 0 and is_user_authenticated():
        if not password:
            return 'Veuillez entrer votre mot de passe.', 0, '', ''
        if not text:
            return 'Veuillez entrer le texte de confirmation.', 0, '', ''
        if text != text_display:
            return 'Veuillez corriger le texte de confirmation.', 0, '', ''
        if not verify_password(get_user_from_id(get_id()), password):
            return 'Mot de passe invalide.', 0, '', ''
        if n_clicks == 1:
            return """Etes-vous sûr de vouloir supprimer votre compte ? Cette
action est irréversible. Cliquez à nouveau sur le bouton pour confirmer.
""", 1, dash.no_update, dash.no_update
        if n_clicks > 1:
            user_id = get_id()

            # Identify the user to delete
            user_to_delete = get_user_from_id(user_id)

            if user_to_delete:

                # if not exist create a deleted user
                create_deleted_user()

                # update queries and contacts tables with deleted user id
                deleted_user_id = get_user_from_username('deletedUser').id

                queries_to_update = get_queries_from_user_id(user_id)
                update_user_id(queries_to_update, deleted_user_id)

                contacts_to_update = get_contacts_from_user_id(user_id)
                update_user_id(contacts_to_update, deleted_user_id)

                # Supprimer l'utilisateur
                delete_user(user_to_delete)
                return 'Compte utilisateur supprimé avec succès.', 0, '', ''

            return 'Erreur: Utilisateur non trouvé.', 0, '', ''

    return 'Vous devez être connecté pour supprimer votre compte.', 0, '', ''