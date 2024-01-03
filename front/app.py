# Importations nécessaires
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

from front.components import header, navbar, footer


# Importation de l'application serveur Flask depuis server.py
from back.server import server

# Initialisation de l'application Dash
external_stylesheets = [
    dbc.themes.YETI,
    'https://fonts.googleapis.com/css2?family=Lobster&display=swap'
]
app = Dash(
    __name__,
    server=server,
    url_base_pathname='/',
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
    meta_tags=[
        {
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1.0'
        }
    ]
)
app.title = 'EEG Explorer'

# Définition du layout de l'application
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


from front.callbacks import *


# Point d'entrée principal pour l'exécution de l'application
if __name__ == '__main__':
    app.run_server(debug=True)  # Activer le mode debug pour le développement
