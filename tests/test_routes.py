from base_test import BaseTest
from models import Cleaner
from app import db


class TestAPI(BaseTest):
    def setUp(self):
        super().setUp()
        self.test_user = {
            'username': 'foo',
            'email': 'bar@gmail.com',
            'services': 'x'
        }

    def test_add_cleaner(self):
        response = self.client.post('/cleaner', json=self.test_user)

        # Check response is correct
        self.assertEqual(response.status_code, 201)

        # Retrieve newly created cleaner object from database and check it's correct
        cleaner = db.session.query(Cleaner).filter_by(username='foo').first()
        self.assertEqual(cleaner.username, self.test_user['username'])
        self.assertEqual(cleaner.email, self.test_user['email'])
        self.assertEqual(cleaner.services, self.test_user['services'])

    def test_get_cleaner(self):
        cleaner = Cleaner(**self.test_user)
        db.session.add(cleaner)
        db.session.commit()
        response = self.client.get('/cleaner', query_string={'username': self.test_user['username']})
        self.assertEqual(response.status_code, 200)
        return_details = response.json
        self.assertEqual(self.test_user, return_details)

    # TODO test get cleaner no username provided

    def test_add_cleaner_with_non_unique_username(self):
        db.session.add(self.test_user)
        db.session.commit()
        response = self.client.post(
            '/cleaner',
            json=self.test_user)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'non unique username')

    def test_add_cleaner_with_non_unique_email(self):
        cleaner_details_with_non_unique_email = {'username': 'johnny', 'bar@gmail.com': 'c', 'services': 'klj'}
        db.session.add(self.test_user)
        db.session.commit()
        response = self.client.post('/cleaner', json=cleaner_details_with_non_unique_email)
        self.assertEqual(response.status_code, 400)

    def test_add_cleaner_with_invalid_email(self):
        pass
