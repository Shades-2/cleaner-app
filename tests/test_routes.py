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
        self.cleaner = Cleaner(**self.test_user)
        db.session.add(self.cleaner)
        db.session.commit()

    def test_add_cleaner(self):
        response = self.client.post('/cleaner', json={
            'username': 'harry',
            'email': 'harry@gmail.com',
            'services': 'everything'
        })

        # Check response is correct

        self.assertEqual(response.status_code, 201)

        # Retrieve newly created cleaner object from database and check it's correct
        cleaner = db.session.query(Cleaner).filter_by(username='harry').first()
        self.assertEqual(cleaner.username, 'harry')
        self.assertEqual(cleaner.email, 'harry@gmail.com')
        self.assertEqual(cleaner.services, 'everything')

    def test_get_cleaner(self):
        response = self.client.get('/cleaner', query_string={'username': self.test_user['username']})
        self.assertEqual(response.status_code, 200)
        return_details = response.json
        self.assertEqual(self.test_user, return_details)

    # TODO test get cleaner no username provided

    def test_add_cleaner_with_non_unique_username(self):
        response = self.client.post(
            '/cleaner',
            json=self.test_user)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'non unique username')

    def test_add_cleaner_with_non_unique_email(self):
        cleaner_details_with_non_unique_email = {'username': 'johnny', 'email': 'bar@gmail.com', 'services': 'klj'}
        response = self.client.post('/cleaner', json=cleaner_details_with_non_unique_email)
        self.assertEqual(response.status_code, 400)

    def test_add_cleaner_with_invalid_email(self):
        cleaner_deatils_with_invalid_email = {'username': 'johnny', 'email': 'as', 'services': 'klj'}
        response = self.client.post('/cleaner', json=cleaner_deatils_with_invalid_email)
        self.assertEqual(response.status_code, 400)
