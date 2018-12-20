'''This module represents the question view'''
from flask import Blueprint, request, jsonify, make_response

from app.api.utils.serializer import serialize
from app.api.v1.models.question_model import QuestionModel, QUESTIONS
from app.api.v1.models.answer_model import AnswerModel

API = Blueprint("api", __name__, url_prefix='/api/v1')

@API.route('/questions', methods=['POST'])
def user_post_question():
    '''API endpoint for posting questions'''
    title = request.get_json()['title']
    description = request.get_json()['description']
    created_by = request.get_json()['created_by']

    question = QuestionModel(
        title=title,
        description=description,
        created_by=created_by
    )

    QuestionModel.add_questions(serialize(question))

    return make_response(jsonify({
        'status': 201,
        'data': [
            {
                'id': question.get_question_id(),
                'title': title,
                'description': description,
                'created_by': created_by,
                'created_on': question.created_on
            }
        ]
    }), 201)

@API.route('/questions', methods=['GET'])
def user_fetch_all_questions():
    '''API endpoint for fetching all questions'''
    questions = QuestionModel.get_all_questions()
    if questions == []:
        return make_response(jsonify({
            'message': 'NO QUESTION HAS BEEN ADDED YET!'
        }), 404)
    return make_response(jsonify({
        'status': 200,
        'data': questions
    }), 200)

@API.route('/questions/<question_id>', methods=['GET'])
def fetch_one_question(question_id):
    '''API endpoint for fetching one question'''
    if question_id.isdigit():
        question = QuestionModel.get_question_by_id(int(question_id))
        if question == {}:
            return make_response(jsonify({
                'message': "QUESTION WITH ID '{}' DOESN'T EXIST!".format(question_id)
            }), 404)
        return make_response(jsonify({
            'status': 200,
            'data': [question]
        }))
    return make_response(jsonify({
        'message': "QUESTION ID MUST BE AN INTEGER VALUE"
    }), 400)

@API.route('/questions/<question_id>', methods=['DELETE'])
def delete_one_question(question_id):
    '''API endpoint for deleting one question'''
    if question_id.isdigit():
        question = QuestionModel.get_question_by_id(int(question_id))
        if question == {}:
            return make_response(jsonify({
                'message': "QUESTION WITH ID '{}' DOESN'T EXIST!".format(question_id)
            }), 404)
        QUESTIONS.remove(question)
        return make_response(jsonify({
            'status': 200,
            'message': "QUESTION WITH ID '{}' HAS BEEN SUCCESSFULLY DELETED".format(question_id)
        }), 200)
    return make_response(jsonify({
        'message': "QUESTION ID MUST BE AN INTEGER VALUE"
    }), 400)

@API.route('/questions/<question_id>/answers', methods=['POST'])
def post_answer(question_id):
    '''API endpoint for posting an answer'''
    description = request.get_json()['description']

    answer = AnswerModel(
        description=description
    )

    question = QuestionModel.get_question_by_id(int(question_id))
    AnswerModel.add_answer(answer, question_id)

    return make_response(jsonify({
        'status': 201,
        'data': [question]
    }))
