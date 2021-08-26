from unittest import TestCase

from app import create_app, db


class BaseTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app(test=True)
        cls.app.app_context().push()
        cls.client = cls.app.test_client()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
