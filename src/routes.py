from flask import request, current_app as app, jsonify
from models import Cleaner
from app import db


@app.route("/cleaner", methods=['POST'])
def add_cleaner():
    data = request.json
    cleaner = Cleaner(username=data.get('username'),
                      email=data.get('email'),
                      password=data.get('password'),
                      services=data.get('services'))
    db.session.add(cleaner)
    db.session.commit()
    return jsonify({}), 201


@app.route("/cleaner", methods=['GET'])
def get_cleaner():
    username = request.args.get('username')
    cleaner = db.session.query(Cleaner).filter_by(username=username).first()
    return jsonify({
        'username': cleaner.username,
        'email': cleaner.email,
        'password': cleaner.password,
        'services': cleaner.services
    })
