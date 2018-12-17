'''This module represents the base test class'''
import unittest

from app import create_app
from app.api.v1.user_model import USERS

class BaseTestCase(unittest.TestCase):
    '''Base class for other test classes'''
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

        self.user_registration = dict(username="john", email="john@example.com", password="12345")
        self.user_login = dict(username="john", password="12345")

        self.empty_username = dict(username="", email="john@example.com", password="12")
        self.digit_username = dict(username="1234", email="john@example.com", password="12")

        self.empty_password = dict(username="test", email="test@example.com", password=" ")

        self.incorrect_username = dict(username="jane", password="12345")
        self.incorrect_password = dict(username="john", password="abcd")

    @staticmethod
    def get_accept_content_type_headers():
        '''Return the content type headers for the body'''
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def tearDown(self):
        del USERS[:]

if __name__ == "__main__":
    unittest.main()
