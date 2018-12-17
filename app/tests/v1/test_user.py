'''This module represents tests for the user entity'''
import json
import unittest

from app.tests.v1.test_base import BaseTestCase

class UserTestCase(BaseTestCase):
    '''Test definitions for a user'''
    def test_user_registration(self):
        '''Test the API can register a user'''
        res = self.client().post(
            '/auth/signup',
            headers=BaseTestCase.get_accept_content_type_headers(),
            data=json.dumps(self.user_regisration)
        )
        self.assertEqual(res.status_code, 201)
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(201, response_msg["status"])
        self.assertEqual("Create a user record", response_msg["data"][0]["message"])
