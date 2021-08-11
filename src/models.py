from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:dev@localhost:5432/cleaner'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(
        db.String(120), nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.email}', '{self.image_file} )"


class CleanerDetails():
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(
        db.String(120), nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)
    services = db.Column(db.String(120))
