from flask_testing import TestCase
from flask import current_app, url_for

from urllib.parse import urlparse,urlunparse
import os

from main import app

class MainTest(TestCase):

    def create_app(self):
        app.config['TESTING']= True
        app.config['WTF_CSFR_ENABLED'] = False
        app.config['URL_ROOT'] = ''

        return app
    
    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    #def test_index_redirects(self):
    #    # Create a client object.
    #    client = self.client
    #    
    #    # Make a GET request to the `index()` function.
    #    response = client.get(url_for('index'))

    #    # Assert that the response redirects the user to the `hello()` function.
    #    self.assertRedirects(response, url_for('hello'))
    
    def test_hello_get(self):
        repsonse = self.client.get(url_for('hello'))

        self.assert200(repsonse)

    #def test_hello_post(self):
    #    fake_form = {
    #        'username': 'fake',
    #        'password': 'fake-password'
    #    }
    #    response = self.client.post(url_for('hello'), data=fake_form)
#
    #    self.assertRedirects(response, url_for('index'))

    def test_auth_blueprint_exists(self):
        self.assertIn('auth', self.app.blueprints)

    def test_auth_login_get(self):
        self.client.get(url_for('auth.login'))

        self.assertTemplateUsed('login.html')

    #not suport WTF
    #def test_auth_login_post(self):    
        #fake_form = {
        #    'username': 'Alfred the Great',
        #    'password': 'The Grand Britain'
        #}
        #response = self.client.post(url_for('auth.login',data = fake_form))
        #self.assertRedirects(response, url_for('index'))
        
    #variables export FLASK_APP=main.py  