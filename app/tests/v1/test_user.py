'''This module represents tests for the user entity'''
import json

from app.tests.v1.test_base import BaseTestCase

class UserTestCase(BaseTestCase):
    '''Test definitions for a user'''
    def test_user_registration(self):
        '''Test the API can register a user'''
        res = self.client().post(
            '/auth/signup',
            headers=BaseTestCase.get_accept_content_type_headers(),
            data=json.dumps(self.user_registration)
        )
        self.assertEqual(res.status_code, 201)
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(201, response_msg["status"])
        self.assertEqual("Create user record", response_msg["data"][0]["message"])

    def test_user_login(self):
        '''Test the API can log in a user'''
        res = self.client().post(
            '/auth/signup',
            headers=BaseTestCase.get_accept_content_type_headers(),
            data=json.dumps(self.user_registration)
        )
        self.assertEqual(res.status_code, 201)
        res = self.client().post(
            '/auth/login',
            headers=BaseTestCase.get_accept_content_type_headers(),
            data=json.dumps(self.user_login)
        )
        self.assertEqual(res.status_code, 200)
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(200, response_msg["status"])
        self.assertEqual("Logged in as john", response_msg["data"][0]["message"])

    def test_empty_username(self):
        '''Test the API cannot register a user with an empty username'''
        res = self.client().post(
            '/auth/signup',
            headers=BaseTestCase.get_accept_content_type_headers(),
            data=json.dumps(self.empty_username)
        )
        self.assertEqual(res.status_code, 400)
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual("USERNAME CANNOT BE EMPTY", response_msg["message"])

    def test_digit_username(self):
        '''
        Test the API cannot register a user with username consisting of digits only
        '''
        res = self.client().post(
            '/auth/signup',
            headers=BaseTestCase.get_accept_content_type_headers(),
            data=json.dumps(self.digit_username)
        )
        self.assertEqual(res.status_code, 400)
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual("USERNAME CANNOT CONSIST OF DIGITS ONLY", response_msg["message"])

    def test_empty_password(self):
        '''
        Test the API cannot register a user with an empty password
        '''
        res = self.client().post(
            '/auth/signup',
            headers=BaseTestCase.get_accept_content_type_headers(),
            data=json.dumps(self.empty_password)
        )
        self.assertEqual(res.status_code, 400)
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual("PASSWORD CANNOT BE EMPTY", response_msg["message"])

    def test_incorrect_username(self):
        '''Test the API cannot log in a user who is not yet registered'''
        res = self.client().post(
            '/auth/login',
            headers=BaseTestCase.get_accept_content_type_headers(),
            data=json.dumps(self.incorrect_username)
        )
        self.assertEqual(res.status_code, 400)
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual("User with username 'jane' doesn't exist!", response_msg["message"])
