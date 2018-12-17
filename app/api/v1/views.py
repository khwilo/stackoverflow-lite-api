'''This module represents the user view'''
from flask import Blueprint, request, jsonify, make_response

from app.api.v1.models import UserModel

AUTH = Blueprint("auth", __name__, url_prefix='/auth')

@AUTH.route('/signup', methods=['POST'])
def user_registration():
    '''API endpoint for user registration'''
    # data = request.get_json()
    username = request.get_json()['username']
    email = request.get_json()['email']
    password = UserModel.generate_password_hash(request.get_json()['password'])

    if not username or not username.split():
        return make_response(jsonify({
            'message': 'USERNAME CANNOT BE EMPTY'
        }), 400)

    # Create an instance of the user
    user = UserModel(username=username, email=email, password=password)

    UserModel.add_user(user.user_as_dict())

    response = make_response(jsonify({
        'status': 201,
        'data': [
            {
                'id': user.get_user_id(),
                'message': "Create user record"
            }
        ]
    }), 201)
    return response
