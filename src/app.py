from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(test=False):
    app = Flask(__name__)
    if not test:
        app.config['SECRET_KEY'] = 'dev'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:dev@localhost/cleaner'
    else:
        app.config['SECRET_KEY'] = 'test'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:dev@localhost/unittest-cleaner'

    return app


app = create_app()
db = SQLAlchemy(app)
