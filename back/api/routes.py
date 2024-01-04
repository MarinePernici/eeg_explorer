""" API routes. """

import jwt
import datetime

from flask import jsonify, request, make_response
from sqlalchemy.exc import SQLAlchemyError
from flask import Flask, jsonify, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy


from back.models import Contacts, Queries, QueryResults, db, User

from ..server import server


@server.route('/api/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        login_user(user)
        if current_user.is_authenticated:
            # Création du token
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),  # Expiration après 1 jour
                'iat': datetime.datetime.utcnow(),  # Date de création du token
                'sub': user.id  # Sujet du token (identifiant de l'utilisateur)
            }
            token = jwt.encode(payload, server.config['SECRET_KEY'], algorithm='HS256')

            # Retourner le token dans un cookie
            # resp = make_response(jsonify({'login': True}))
            # resp.set_cookie('auth_token', token)
            # return resp
            return jsonify({'token': token})
    return jsonify({'login': False}), 401


@server.route('/api/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'logout': True})


@server.route('/api/is_authenticated')
def is_authenticated():
    if current_user.is_authenticated:
        return jsonify(
            {'authenticated': True,
             'user_id': current_user.get_id(),
             'email': current_user.email,
             'username': current_user.username}
        )
    return jsonify({'authenticated': False})


@server.route('/api/record_query', methods=['POST'])
def record_query():
    data = request.json
    try:
        new_query = Queries(
            query_text=data['query_text'],
            user_id=data['user_id'],
            prompt_tokens=data.get('prompt_tokens'),
            completion_tokens=data.get('completion_tokens'),
            total_tokens=data.get('total_tokens'),
            cost=data.get('cost')
        )
        db.session.add(new_query)
        db.session.commit()
        return jsonify({
            "success": True,
            "message": "Requête enregistrée.",
            "query_id": new_query.id
        })
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"success": False, "message": str(e)})


@server.route('/api/record_query_result', methods=['POST'])
def record_query_result():
    data = request.json
    try:
        new_query_result = QueryResults(
            query_id=data['query_id'],
            result=data['result'],
            execution_time=data['execution_time']
        )
        db.session.add(new_query_result)
        db.session.commit()
        return jsonify(
            {"success": True, "message": "Résultat de requête enregistré."}
        )
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"success": False, "message": str(e)})


@server.route('/api/record_contact', methods=['POST'])
def record_contact():
    data = request.json
    try:
        new_contact = Contacts(
            name=data['name'],
            email=data['email'],
            subject=data['subject'],
            message=data['message'],
            user_id=data['user_id']
        )
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({"success": True, "message": "Message envoyé."})
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"success": False, "message": str(e)})


@server.route('/api/get_user_history', methods=['GET'])
def get_user_history():
    user_id = request.args.get('user_id')
    user_queries = Queries.query.filter_by(user_id=user_id).all()
    history = []
    for query_info in user_queries:
        query_result = QueryResults.query.filter_by(
            query_id=query_info.id
        ).first()
        history.append({
            'date': query_info.time_created.strftime("%d/%m/%Y - %H:%M:%S"),
            'query': query_info.query_text,
            'response': query_result.result if query_result else 'No response'
        })
    return jsonify(history)


# @server.route('/test')
# @login_required
# def test_route():
#     print(current_user)
#     print(current_user.id)
#     return 'Test'
