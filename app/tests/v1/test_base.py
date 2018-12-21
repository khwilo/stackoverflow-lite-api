'''This module represents the base test class'''
import unittest

from datetime import datetime

from app import create_app
from app.api.utils.serializer import serialize
from app.api.v1.models.user_model import USERS, UserModel
from app.api.v1.models.question_model import QUESTIONS

class BaseTestCase(unittest.TestCase):
    '''Base class for other test classes'''
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.app_context = self.app.app_context()
        self.app_context.push()

        self.user_registration = dict(username="john", email="john@example.com", password="12345")
        self.user_login = dict(username="john", password="12345")

        self.empty_username = dict(username="", email="john@example.com", password="12")
        self.digit_username = dict(username="1234", email="john@example.com", password="12")

        self.empty_password = dict(username="test", email="test@example.com", password=" ")

        self.incorrect_username = dict(username="jane", password="12345")
        self.incorrect_password = dict(username="john", password="abcd")

        self.question = dict(title="Test title", description="Test description", created_by="Test")

        self.answer = dict(description="Test answer description")

    @staticmethod
    def get_accept_content_type_headers():
        '''Return the content type headers for the body'''
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def test_serialize_function(self):
        '''Test the function serialize() converts an object to a dictionary'''
        user = UserModel(username="Test", email="test@example.com", password="12345")
        serialized_user_obj = serialize(user)
        user_dict = dict(username="Test", email="test@example.com", password="12345")
        self.assertTrue(serialized_user_obj, user_dict)
        now_date = datetime.utcnow()
        serialized_date = serialize(now_date)
        self.assertTrue(serialized_date, now_date.isoformat())

    def tearDown(self):
        del USERS[:]
        del QUESTIONS[:]
        self.app_context.pop()

if __name__ == "__main__":
    unittest.main()
