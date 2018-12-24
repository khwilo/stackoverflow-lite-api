'''This module represents tests for the question entity'''
import json

from app.tests.v1.test_base import BaseTestCase

class QuestionTestCase(BaseTestCase):
    '''Test definitions for a question'''
    def test_user_post_question(self):
        '''Test the API can post questions'''
        res = self.get_response_from_user()
        response_msg = json.loads(res.data.decode("UTF-8"))
        access_token = response_msg["data"][0]["access_token"]
        res = self.client().post(
            '/api/v1/questions',
            headers=self.get_authentication_headers(access_token),
            data=json.dumps(self.question)
        )
        self.assertEqual(res.status_code, 201)
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(201, response_msg["status"])
        self.assertTrue(response_msg["data"])

    def test_fetch_all_questions(self):
        '''Test the API can fetch all questions'''
        res = self.get_response_from_user()
        response_msg = json.loads(res.data.decode("UTF-8"))
        access_token = response_msg["data"][0]["access_token"]
        res = self.client().post(
            '/api/v1/questions',
            headers=self.get_authentication_headers(access_token),
            data=json.dumps(self.question)
        )
        self.assertEqual(res.status_code, 201)
        res = self.client().get(
            '/api/v1/questions',
            headers=self.get_authentication_headers(access_token)
        )
        self.assertEqual(res.status_code, 200)
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(200, response_msg["status"])
        self.assertTrue(response_msg["data"])

    def test_fetch_empty_questions_record(self):
        '''
        Test the API returns formatted message when trying to
        fetch questions from an empty record
        '''
        res = self.get_response_from_user()
        response_msg = json.loads(res.data.decode("UTF-8"))
        access_token = response_msg["data"][0]["access_token"]
        res = self.client().get(
            '/api/v1/questions',
            headers=self.get_authentication_headers(access_token)
        )
        self.assertEqual(res.status_code, 404)
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual("NO QUESTION HAS BEEN ADDED YET!", response_msg["message"])

    def test_fetch_one_question(self):
        '''Test the API can fetch one question'''
        res = self.get_response_from_user()
        response_msg = json.loads(res.data.decode("UTF-8"))
        access_token = response_msg["data"][0]["access_token"]
        res = self.client().post(
            '/api/v1/questions',
            headers=self.get_authentication_headers(access_token),
            data=json.dumps(self.question)
        )
        self.assertEqual(res.status_code, 201)
        res = self.client().get(
            '/api/v1/questions/1',
            headers=self.get_authentication_headers(access_token)
        )
        self.assertEqual(res.status_code, 200)
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(200, response_msg["status"])
        self.assertTrue(response_msg["data"])

    def test_incorrect_question_id(self):
        '''Test the API cannot fetch a question with an incorrect id'''
        res = self.get_response_from_user()
        response_msg = json.loads(res.data.decode("UTF-8"))
        access_token = response_msg["data"][0]["access_token"]
        res = self.client().get(
            '/api/v1/questions/i',
            headers=self.get_authentication_headers(access_token)
        )
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(res.status_code, 400)
        self.assertEqual("QUESTION ID MUST BE AN INTEGER VALUE", response_msg["message"])

    def test_non_existent_question(self):
        '''Test the API cannot a non-existent question'''
        res = self.get_response_from_user()
        response_msg = json.loads(res.data.decode("UTF-8"))
        access_token = response_msg["data"][0]["access_token"]
        res = self.client().get(
            '/api/v1/questions/2',
            headers=self.get_authentication_headers(access_token)
        )
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(res.status_code, 404)
        self.assertEqual("QUESTION WITH ID '2' DOESN'T EXIST!", response_msg["message"])

    def test_delete_one_question(self):
        '''Test the API can delete one question'''
        res = self.get_response_from_user()
        response_msg = json.loads(res.data.decode("UTF-8"))
        access_token = response_msg["data"][0]["access_token"]
        res = self.client().post(
            '/api/v1/questions',
            headers=self.get_authentication_headers(access_token),
            data=json.dumps(self.question)
        )
        self.assertEqual(res.status_code, 201)
        res = self.client().delete(
            '/api/v1/questions/1',
            headers=self.get_authentication_headers(access_token)
        )
        self.assertEqual(res.status_code, 200)
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(response_msg["status"], 200)
        self.assertEqual(
            response_msg["message"],
            "QUESTION WITH ID '1' HAS BEEN SUCCESSFULLY DELETED"
        )

    def test_post_answer(self):
        '''Test the API can post an answer'''
        res = self.get_response_from_user()
        response_msg = json.loads(res.data.decode("UTF-8"))
        access_token = response_msg["data"][0]["access_token"]
        res = self.client().post(
            '/api/v1/questions',
            headers=self.get_authentication_headers(access_token),
            data=json.dumps(self.question)
        )
        self.assertEqual(res.status_code, 201)
        res = self.client().post(
            '/api/v1/questions/1/answers',
            headers=self.get_authentication_headers(access_token),
            data=json.dumps(self.answer)
        )
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(res.status_code, 201)
        self.assertTrue(response_msg["data"][0]["answers"])

    def test_answer_non_existent_question(self):
        '''Test the API cannot post an answer to a non-existing question'''
        res = self.get_response_from_user()
        response_msg = json.loads(res.data.decode("UTF-8"))
        access_token = response_msg["data"][0]["access_token"]
        res = self.client().post(
            '/api/v1/questions/1/answers',
            headers=self.get_authentication_headers(access_token),
            data=json.dumps(self.answer)
        )
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(res.status_code, 404)
        self.assertEqual(
            response_msg["message"],
            "QUESTION WITH ID '1' DOESN'T EXIST!"
        )

    def test_edit_answer(self):
        '''Test the API can edit an answer'''
        res = self.get_response_from_user()
        response_msg = json.loads(res.data.decode("UTF-8"))
        access_token = response_msg["data"][0]["access_token"]
        res = self.client().post(
            '/api/v1/questions',
            headers=self.get_authentication_headers(access_token),
            data=json.dumps(self.question)
        )
        self.assertEqual(res.status_code, 201)
        res = self.client().post(
            '/api/v1/questions/1/answers',
            headers=self.get_authentication_headers(access_token),
            data=json.dumps(self.answer)
        )
        self.assertEqual(res.status_code, 201)
        res = self.client().put(
            '/api/v1/questions/1/answers/1',
            headers=self.get_authentication_headers(access_token),
            data=json.dumps({
                'description': "Updated test answer description",
                'accepted': True,
                "rejected": False
            })
        )
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_msg["message"], "ANSWER HAS BEEN UPDATED SUCCESSFULLY!")

    def test_edit_non_existent_answer(self):
        '''Test the API cannot edit a non-existent answer'''
        res = self.get_response_from_user()
        response_msg = json.loads(res.data.decode("UTF-8"))
        access_token = response_msg["data"][0]["access_token"]
        res = self.client().post(
            '/api/v1/questions',
            headers=self.get_authentication_headers(access_token),
            data=json.dumps(self.question)
        )
        self.assertEqual(res.status_code, 201)
        res = self.client().put(
            '/api/v1/questions/1/answers/1',
            headers=self.get_authentication_headers(access_token),
            data=json.dumps({
                'description': 'Non-existent answer',
                'accepted': False,
                'rejected': True
            })
        )
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(res.status_code, 404)
        self.assertEqual(response_msg["message"], "ANSWER WITH ID '1' DOESN'T EXIST!")

    def test_incorrect_edit_answer(self):
        '''Test the API cannot edit an answer with an incorrect ID'''
        res = self.get_response_from_user()
        response_msg = json.loads(res.data.decode("UTF-8"))
        access_token = response_msg["data"][0]["access_token"]
        res = self.client().post(
            '/api/v1/questions',
            headers=self.get_authentication_headers(access_token),
            data=json.dumps(self.question)
        )
        self.assertEqual(res.status_code, 201)
        res = self.client().put(
            '/api/v1/questions/1/answers/i',
            headers=self.get_authentication_headers(access_token),
            data=json.dumps({
                'description': 'Incorrect answer ID',
                'accepted': False,
                'rejected': True
            })
        )
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(res.status_code, 400)
        self.assertEqual(response_msg["message"], "ANSWER ID MUST BE AN INTEGER VALUE!")
