from base_test import BaseTest
from models import Cleaner
from app import db


class TestAPI(BaseTest):
    def test_add_cleaner(self):
        data = {'username': 'foo',
                'email': 'bar',
                'services': 'x'}
        response = self.client.post('/cleaner', json=data)
        cleaner = db.session.query(Cleaner).filter_by(username='foo').first()
        assert cleaner.username == data['username']
        assert cleaner.email == data['email']
        assert cleaner.services == data['services']
        assert response.status_code == 201

    def test_get_cleaner(self):
        cleaner_details = {'username': 'x', 'email': 'y', 'services': 'a'}
        cleaner = Cleaner(**cleaner_details)
        db.session.add(cleaner)
        db.session.commit()
        response = self.client.get('/cleaner', query_string={'username': 'x'})
        assert response.status_code == 200
        return_details = response.json
        assert cleaner_details == return_details

    # TODO test get cleaner no username provided

    def test_add_cleaner_with_non_unique_username(self):
        username = 'khjfgk'
        cleaner_details = {'username': username, 'email': 'a', 'services': 'b'}
        cleaner = Cleaner(**cleaner_details)
        db.session.add(cleaner)
        db.session.commit()
        response = self.client.post(
            '/cleaner',
            json={'username': username, 'email': 'c', 'services': 'd'})
        assert response.status_code == 400
        assert response.json['error'] == 'non unique username'

    # def test_add_cleaner_with_non_unique_email(self):
    #     cleaner_details = {'username': 'y', 'email': 'c', 'services': 'd'}
    #     cleaner = Cleaner(**cleaner_details)
    #     db.session.add(cleaner)
    #     db.session.commit()
    #     response = self.client.post('/cleaner', json=cleaner_details)
    #     assert response.status_code == 400