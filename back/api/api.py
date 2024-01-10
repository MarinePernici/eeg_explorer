""" API routes. """

from flask import request, jsonify
from front.app import app
from back.api.models import db, Queries, QueryResults, Contacts
from sqlalchemy.exc import SQLAlchemyError


@app.server.route('/api/record_query', methods=['POST'])
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


@app.server.route('/api/record_query_result', methods=['POST'])
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


@app.server.route('/api/record_contact', methods=['POST'])
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


@app.server.route('/api/get_user_history', methods=['GET'])
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


# @app.server.route('/test')
# @login_required
# def test_route():
#     print(current_user)
#     print(current_user.id)
#     return 'Test'
