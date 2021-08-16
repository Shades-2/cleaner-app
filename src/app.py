from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ
from dotenv import dotenv_values

config = dotenv_values('.env')

user_name = environ['USER']
password = environ['PASSWORD']
secret_key = environ['SECRET_KEY']


def create_app(test=False):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = f'{secret_key}'
    if test:
        app.config['SQLALCHEMY_DATABASE_URI'] = (
            f'postgresql+psycopg2://{user_name}:{password}@localhost/unittest-cleaner'
        )
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = (
            f'postgresql+psycopg2://{user_name}:{password}@localhost/cleaner'
        )
    return app


app = create_app()
db = SQLAlchemy(app)
