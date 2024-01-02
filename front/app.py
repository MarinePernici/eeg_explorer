import os

import dash_bootstrap_components as dbc
from dash import Dash
from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager

load_dotenv()  # Charge les variables d'environnement depuis '.env'

server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

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

from models import db, User

db.init_app(server)

# Configuration de Flask-Login
login_manager = LoginManager()
login_manager.init_app(server)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


from api import *
from routes import *

with server.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run_server(debug=True)
