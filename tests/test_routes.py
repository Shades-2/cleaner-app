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
