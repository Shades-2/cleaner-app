from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from os import environ
from dotenv import load_dotenv

load_dotenv()

user_name = environ['DB_USER']
password = environ['PASSWORD']
secret_key = environ['SECRET_KEY']

db = SQLAlchemy()
ma = Marshmallow()


def create_app(test=False):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = f'{secret_key}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if test:
        app.config['SQLALCHEMY_DATABASE_URI'] = (
            f'postgresql+psycopg2://{user_name}:{password}@localhost/unittest-cleaner'
        )
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = (
            f'postgresql+psycopg2://{user_name}:{password}@localhost/cleaner'
        )
    db.init_app(app)
    with app.app_context():
        import routes
        import models
        db.create_all()
        return app
