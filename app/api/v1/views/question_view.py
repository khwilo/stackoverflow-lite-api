'''This module represents the question view'''
from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api.utils.serializer import serialize
from app.api.v1.models.question_model import QuestionModel, QUESTIONS
from app.api.v1.models.answer_model import AnswerModel

API = Blueprint("api", __name__, url_prefix='/api/v1')

@API.route('/questions', methods=['POST'])
@jwt_required
def user_post_question():
    '''API endpoint for posting questions'''
    title = request.get_json()['title']
    description = request.get_json()['description']
    created_by = get_jwt_identity()

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
@jwt_required
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
@jwt_required
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
@jwt_required
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
@jwt_required
def post_answer(question_id):
    '''API endpoint for posting an answer'''
    description = request.get_json()['description']
    answered_by = get_jwt_identity()

    answer = AnswerModel(
        description=description,
        answered_by=answered_by
    )

    if question_id.isdigit():
        question = QuestionModel.get_question_by_id(int(question_id))
        if question == {}:
            return make_response(jsonify({
                'message': "QUESTION WITH ID '{}' DOESN'T EXIST!".format(question_id)
            }), 404)
        asked_by = question['created_by']

        if asked_by == answered_by:
            return make_response(jsonify({
                'message': "YOU CAN'T ANSWER YOUR OWN QUESTION"
            }), 401)

        AnswerModel.add_answer(answer, question_id)
        return make_response(jsonify({
            'status': 201,
            'data': [question]
        }), 201)
    return make_response(jsonify({
        'message': "QUESTION ID MUST BE AN INTEGER VALUE"
    }), 400)

@API.route('/questions/<question_id>/answers/<answer_id>', methods=['PUT'])
@jwt_required
def update_answer(question_id, answer_id):
    '''API endpoint for updating an answer'''
    description = request.get_json()['description']
    accepted = request.get_json()['accepted']
    rejected = request.get_json()['rejected']

    if question_id.isdigit():
        question = QuestionModel.get_question_by_id(int(question_id))
        if question == {}:
            return make_response(jsonify({
                'message': "QUESTION WITH ID '{}' DOESN'T EXIST!".format(question_id)
            }), 404)
        if answer_id.isdigit():
            answer = QuestionModel.get_answer_by_id(question, int(answer_id))
            if answer == {}:
                return make_response(jsonify({
                    'message': "ANSWER WITH ID '{}' DOESN'T EXIST!".format(answer_id)
                }), 404)
            answer["description"] = description
            answer["accepted"] = accepted
            answer["rejected"] = rejected
            return make_response(jsonify({
                'data': answer,
                'message': "ANSWER HAS BEEN UPDATED SUCCESSFULLY!"
            }))
        return make_response(jsonify({
            'message': "ANSWER ID MUST BE AN INTEGER VALUE!"
        }), 400)
    return make_response(jsonify({
        'message': "QUESTION ID MUST BE AN INTEGER VALUE!"
    }), 400)
