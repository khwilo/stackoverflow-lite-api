'''This module represents the question view'''
from flask import Blueprint, request, jsonify, make_response

from app.api.v1.question_model import QuestionModel

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

    QuestionModel.add_questions(question.question_as_dict())

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