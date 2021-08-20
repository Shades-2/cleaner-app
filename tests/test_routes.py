from base_test import BaseTest
from models import Cleaner
from app import db


class TestAPI(BaseTest):
    def test_add_cleaner(self):
        data = {'username': 'foo',
                'email': 'bar',
                'password': 'baz',
                'services': 'x'}
        response = self.client.post('/cleaner', json=data)
        cleaner = db.session.query(Cleaner).filter_by(username='foo').first()
        assert cleaner.username == data['username']
        assert cleaner.email == data['email']
        assert cleaner.password == data['password']
        assert cleaner.services == data['services']
        assert response.status_code == 201

