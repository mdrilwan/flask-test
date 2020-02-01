from flaskr import app
import unittest

class TestIndex(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        assert response.data == b'Rest interface to perform operations like sum, concat, subtract'
