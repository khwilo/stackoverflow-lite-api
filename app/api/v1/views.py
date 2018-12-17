'''This module represents the user view'''
from flask import Blueprint, request, jsonify, make_response

from app.api.v1.models import UserModel

AUTH = Blueprint("auth_sign_in", __name__, url_prefix='/auth')

@AUTH.route('/signup', methods=['POST'])
def user_registration():
    '''API endpoint for user registration'''
    # data = request.get_json()
    username = request.get_json()['username']
    email = request.get_json()['email']
    password = request.get_json()['password']

    if not username or not username.split():
        return make_response(jsonify({
            'message': 'USERNAME CANNOT BE EMPTY'
        }), 400)

    if username.isdigit():
        return make_response(jsonify({
            'message': 'USERNAME CANNOT CONSIST OF DIGITS ONLY'
        }), 400)

    if not password or not password.split():
        return make_response(jsonify({
            'message': 'PASSWORD CANNOT BE EMPTY'
        }), 400)

    # Create an instance of the user
    user = UserModel(
        username=username,
        email=email,
        password=UserModel.generate_password_hash(password)
    )

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

@AUTH.route('/login', methods=['POST'])
def user_login():
    '''API endpoint for the user login'''
    username = request.get_json()['username']
    password = request.get_json()['password']


    current_user = UserModel.get_user_by_username(username)

    if not current_user:
        return make_response(jsonify({
            'message': "User with username '{}' doesn't exist!".format(username)
        }), 400)


    response = jsonify({
        'status': 200,
        'data': [
            {
                'message': 'Logged in as {}'.format(username)
            }
        ]
    })
    response.status_code = 200
    return response
