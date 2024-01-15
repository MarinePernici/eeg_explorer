import os
import requests

from dotenv import load_dotenv
from back.models import User, db, Queries, QueryResults, Contacts
from passlib.hash import argon2
from flask_login import logout_user

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()  # Charge les variables d'environnement depuis '.env'


def update_user_id(rows, new_id):
    for row in rows:
        row.user_id = new_id
    try:
        db.session.commit()
    except Exception as e:
        print("Erreur lors de la mise à jour :", e)
        db.session.rollback()


def delete_user(user):
    try:
        db.session.delete(user)
        db.session.commit()
        logout_user()
    except Exception as e:
        print("Erreur lors de la suppression de l'utilisateur :", e)
        db.session.rollback()


def verify_password(user, password):
    return user.check_password(password)


def get_query_result_from_id(query_id):
    return QueryResults.query.filter_by(query_id=query_id).first()


def get_queries_from_user_id(user_id):
    return Queries.query.filter_by(user_id=user_id).all()    


def get_contacts_from_user_id(user_id):
    return Contacts.query.filter_by(user_id=user_id).all()


def edit_password(user, new_password):
    user.set_password(new_password)
    try:
        db.session.commit()
        return True
    except Exception as e:
        print("Erreur lors de la modification du mot de passe:", e)
        db.session.rollback()
        return False


def edit_username(user, new_username):
    user.username = new_username
    try:
        db.session.commit()
        return True
    except Exception as e:
        print("Erreur lors de la modification du nom d'utilisateur:", e)
        db.session.rollback()
        return False


def edit_email(user, new_email):
    user.email = new_email
    try:
        db.session.commit()
        return True
    except Exception as e:
        print("Erreur lors de la modification de l'adresse email:", e)
        db.session.rollback()
        return False


def get_user_from_id(user_id):
    return User.query.filter_by(id=user_id).first()


def get_user_from_email(email):
    return User.query.filter_by(email=email).first()


def get_user_from_username(username):
    return User.query.filter_by(username=username).first()


def is_username_registered(name):
    existing_username = User.query.filter_by(username=name).first()
    return existing_username is not None


def is_email_registered(email):
    existing_user = User.query.filter_by(email=email).first()
    return existing_user is not None


def create_user(name, email, password):

    if is_email_registered(email):
        return False

    # create a user instance
    user = User(username=name, email=email)
    user.set_password(password)

    # add user in the database
    try:
        db.session.add(user)
        db.session.commit()
        return True
    except Exception as e:
        print("Erreur lors de la création de l'utilisateur:", e)
        db.session.rollback()
        return False


def create_deleted_user():
    deleted_user = User.query.filter_by(username='deletedUser').first()
    if not deleted_user:
        # generate a strong random password
        random_password = os.urandom(24).hex()
        hashed_password = argon2.hash(random_password)

        deleted_user = User(
            id=0,
            username='deletedUser',
            email='supprime@example.com',  # false email
            password_hash=hashed_password,  # hashed password
        )
        db.session.add(deleted_user)
        db.session.commit()


def get_query_id(response):
    query_id = response.json().get('query_id')
    return query_id


def post_data_in_db(
    data,
    route,
):
    url = f'http://127.0.0.1:8050/api/{route}'
    response = requests.post(
        url,
        json=data,
        timeout=60
    )
    print(response.json(), flush=True)
    return response


def send_contact_email(name, email, subject, message):

    msg = MIMEMultipart()
    msg['Subject'] = 'Contact EEG Explorer'

    body = f"""
Message reçu via le formulaire de contact EEG Explorer
\nNom : {name}
Email : {email}
Sujet : {subject}
Message :\n{message}
"""
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


def get_user_history(user_id):
    response = requests.get(
        'http://127.0.0.1:8050/api/get_user_history',
        params={'user_id': user_id},
        timeout=180
    )
    print("Request status :", response.status_code, flush=False)
    return response
