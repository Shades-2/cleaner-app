from flask import request, current_app as app, jsonify
from sqlalchemy.exc import IntegrityError
from models import Cleaner
from app import db
import constants
from email_validator import validate_email, EmailSyntaxError


@app.route("/cleaner", methods=['POST'])
def add_cleaner():
    data = request.json
    cleaner = Cleaner(
        username=data.get('username'),
        email=data.get('email'),
        services=data.get('services'))

    try:
        validate_email(data.get('email'))
    except EmailSyntaxError as e:
        return jsonify({'error': str(e)})

    db.session.add(cleaner)
    try:
        db.session.commit()
    except IntegrityError as e:
        if 'psycopg2.errors.UniqueViolation' in str(e):
            if 'username' in str(e):
                return jsonify({'error': constants.NON_UNIQUE_USERNAME}), 400
            if 'email' in str(e):
                return jsonify({'error': constants.NON_UNIQUE_EMAIL}), 400
        raise

    return jsonify({}), 201


@app.route("/cleaner", methods=['GET'])
def get_cleaner():
    username = request.args.get('username')
    if not username:
        return jsonify({'error': constants.USERNAME_NOT_PROVIDED_ERROR}), 400

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
