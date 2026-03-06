import unittest
import json
from app import app


class FlaskAppTestCase(unittest.TestCase):

    # setup test client
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test Home Route
    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Welcome to My Flask Web App")

    # Test About Route
    def test_about_route(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "This is the About Page")

    # Test Dynamic Route
    def test_user_route(self):
        response = self.app.get('/user/vamsi')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello, vamsi!")

    # Test POST Route
    def test_post_data(self):
        test_data = {"name": "Vamsi", "age": 21}

        response = self.app.post(
            '/data',
            data=json.dumps(test_data),
            content_type='application/json'
        )

        response_json = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_json["message"], "Data received successfully")
        self.assertEqual(response_json["data"], test_data)


if __name__ == '__main__':
    unittest.main()