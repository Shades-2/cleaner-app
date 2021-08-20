from flask import current_app
from flask_sqlalchemy import SQLAlchemy

from app import db


class Cleaner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    services = db.Column(db.String(120))
