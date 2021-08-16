from base_test import BaseTest


class TestCleaner(BaseTest):
    def test_hello(self):
        response = self.client.get('/')
        assert response.status_code == 200
