'''This module represents tests for the question entity'''
import json

from app.tests.v1.test_base import BaseTestCase

class QuestionTestCase(BaseTestCase):
    '''Test definitions for a question'''
    def test_user_post_question(self):
        '''Test the API can post questions'''
        res = self.client().post(
            '/api/v1/questions',
            headers=BaseTestCase.get_accept_content_type_headers(),
            data=json.dumps(self.question)
        )
        self.assertEqual(res.status_code, 201)
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(201, response_msg["status"])
        self.assertTrue(response_msg["data"])
