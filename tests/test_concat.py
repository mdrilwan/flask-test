from flaskr import app
import unittest

class TestConcat(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_concat(self):
        response = self.app.get('/concat?a=4&b=2')
        assert response.data == b'42'
        response = self.app.get('/concat?a=100&b=200')
        assert response.data == b'100200'
