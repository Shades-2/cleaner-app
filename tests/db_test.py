from flask_sqlalchemy import SQLAlchemy
from flask import url_for
import requests
from unittest import TestCase
from app import create_app


test_app = create_app(test=True)
db = SQLAlchemy(test_app)


class BaseTest(TestCase):

    def setUp(self):
        test_app.app_context().push()
        with test_app.app_context():
            db.session.remove()
            db.drop_all()
            db.create_all()

    def tearDown(self):
        with test_app.app_context():
            db.session.remove()
            db.drop_all()


class TestCleaner(BaseTest):
    def test_hello(self):
        url = url_for('hello')
        response = requests.get(url)
        assert response.status_code == 200
