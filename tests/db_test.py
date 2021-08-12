from flask_testing import TestCase
from flask import url_for
import requests

from app import create_app, db
from routes import hello


class MyTest(TestCase):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:dev@localhost/cleaner'
    TESTING = True

    def create_app(self):
        return create_app()

    def setUp(self):
        db.create_all(self.create_app())

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_hello(self):
        url = url_for(hello)
        response = requests.get(url)
        assert response.status == 200
