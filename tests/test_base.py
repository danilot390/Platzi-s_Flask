from flask_testing import TestCase
from flask import current_app, url_for

from main import app

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING']= True
        app.config['WTF_CSFR_ENABLED'] = False

        return app
    
    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_index_redirects(self):
        response = self.client.get(url_for('index'))
        print(response)
        self.assertRedirects(response, url_for('hello'))

    def test_hello_get(self):
        repsonse = self.client.get(url_for('hello'))

        self.assert200(repsonse)

    def test_hello_post(self):
        user={
            'user': 'fake',
            'password' : 123,
        }
        response = self.client.post(url_for('hello', data={user}))

        self.assertRedirects(response, url_for('index'))