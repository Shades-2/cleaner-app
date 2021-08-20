from flask import request, current_app, jsonify
from models import Cleaner
from app import db


@current_app.route("/cleaner", methods=['POST'])
def add_cleaner():
    data = request.json
    cleaner = Cleaner(username=data.get('username'),
                      email=data.get('email'),
                      password=data.get('password'),
                      services=data.get('services'))
    db.session.add(cleaner)
    db.session.commit()
    return jsonify({}), 201
