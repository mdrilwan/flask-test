from flaskr import app
import unittest

class TestSum(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_sum(self):
        response = self.app.get('/sum?a=4&b=2')
        assert response.data == b'6'
        response = self.app.get('/sum?a=100&b=200')
        assert response.data == b'300'
