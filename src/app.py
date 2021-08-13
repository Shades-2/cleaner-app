from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test=False):
    app = Flask(__name__)
    if test:
        app.config['SECRET_KEY'] = 'test'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:dev@localhost/unittest-cleaner'
    else:
        app.config['SECRET_KEY'] = 'dev'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:dev@localhost/cleaner'
    db.init_app(app)
    with app.app_context():
        import routes
        import models
        db.create_all()
        return app
