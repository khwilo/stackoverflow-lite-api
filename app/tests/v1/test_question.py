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

    def test_fetch_all_questions(self):
        '''Test the API can fetch all questions'''
        res = self.client().post(
            '/api/v1/questions',
            headers=BaseTestCase.get_accept_content_type_headers(),
            data=json.dumps(self.question)
        )
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/api/v1/questions')
        self.assertEqual(res.status_code, 200)
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(200, response_msg["status"])
        self.assertTrue(response_msg["data"])

    def test_fetch_empty_questions_record(self):
        '''
        Test the API returns formatted message when trying to
        fetch questions from an empty record
        '''
        res = self.client().get('/api/v1/questions')
        self.assertEqual(res.status_code, 404)
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual("NO QUESTION HAS BEEN ADDED YET!", response_msg["message"])

    def test_fetch_one_question(self):
        '''Test the API can fetch one question'''
        res = self.client().post(
            '/api/v1/questions',
            headers=BaseTestCase.get_accept_content_type_headers(),
            data=json.dumps(self.question)
        )
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/api/v1/questions/1')
        self.assertEqual(res.status_code, 200)
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(200, response_msg["status"])
        self.assertTrue(response_msg["data"])

    def test_incorrect_question_id(self):
        '''Test the API cannot fetch a question with an incorrect id'''
        res = self.client().get('/api/v1/questions/i')
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(res.status_code, 400)
        self.assertEqual("QUESTION ID MUST BE AN INTEGER VALUE", response_msg["message"])

    def test_non_existent_question(self):
        '''Test the API cannot a non-existent question'''
        res = self.client().get('/api/v1/questions/2')
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(res.status_code, 404)
        self.assertEqual("QUESTION WITH ID '2' DOESN'T EXIST!", response_msg["message"])

    def test_delete_one_question(self):
        '''Test the API can delete one question'''
        res = self.client().post(
            '/api/v1/questions',
            headers=BaseTestCase.get_accept_content_type_headers(),
            data=json.dumps(self.question)
        )
        self.assertEqual(res.status_code, 201)
        res = self.client().delete('/api/v1/questions/1')
        self.assertEqual(res.status_code, 200)
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(response_msg["status"], 200)
        self.assertEqual(
            response_msg["message"],
            "QUESTION WITH ID '1' HAS BEEN SUCCESSFULLY DELETED"
        )

    def test_post_answer(self):
        '''Test the API can post an answer'''
        res = self.client().post(
            '/api/v1/questions',
            headers=BaseTestCase.get_accept_content_type_headers(),
            data=json.dumps(self.question)
        )
        self.assertEqual(res.status_code, 201)
        res = self.client().post(
            '/api/v1/questions/1/answers',
            headers=BaseTestCase.get_accept_content_type_headers(),
            data=json.dumps(self.answer)
        )
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(res.status_code, 201)
        self.assertTrue(response_msg["data"][0]["answers"])

    def test_answer_non_existent_question(self):
        '''Test the API cannot post an answer to a non-existing question'''
        res = self.client().post(
            '/api/v1/questions/1/answers',
            headers=BaseTestCase.get_accept_content_type_headers(),
            data=json.dumps(self.answer)
        )
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(res.status_code, 404)
        self.assertEqual(
            response_msg["message"],
            "QUESTION WITH ID '1' DOESN'T EXIST!"
        )
