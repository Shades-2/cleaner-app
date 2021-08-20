from unittest import TestCase

from app import create_app, db


class BaseTest(TestCase):

    def setUp(self):
        self.app = create_app(test=True)
        self.app.app_context().push()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
