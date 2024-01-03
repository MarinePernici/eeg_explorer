import os

from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager


load_dotenv()  # Charge les variables d'environnement depuis '.env'

server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

from back.models import db, User

db.init_app(server)

# Configuration de Flask-Login
login_manager = LoginManager()
login_manager.init_app(server)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from front.callbacks import *

with server.app_context():
    db.create_all()

if __name__ == '__main__':
    server.run(debug=True)