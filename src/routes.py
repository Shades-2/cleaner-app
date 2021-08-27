from flask import request, current_app as app, jsonify
from werkzeug.exceptions import BadRequest
from models import Cleaner
from app import db


@app.route("/cleaner", methods=['POST'])
def add_cleaner():
    data = request.json
    # validate data obj - has all required values?
    cleaner = Cleaner(
        username=data.get('username'),
        email=data.get('email'),
        services=data.get('services'))
    db.session.add(cleaner)
    db.session.commit()
    return jsonify({}), 201


@app.route("/cleaner", methods=['GET'])
def get_cleaner():
    username = request.args.get('username')
    if not username:
        raise BadRequest('No username provided')

    cleaner = db.session.query(
        Cleaner
    ).filter_by(
        username=username
    ).first_or_404()

    return jsonify({
        'username': cleaner.username,
        'email': cleaner.email,
        'services': cleaner.services
    })
