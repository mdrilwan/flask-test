from flaskr import app
import unittest

class TestSubtract(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_subtract(self):
        response = self.app.get('/subtract?a=4&b=2')
        assert response.data == b'2'
        response = self.app.get('/subtract?a=100&b=200')
        assert response.data == b'-100'
