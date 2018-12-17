'''Application module'''
import json

from flask import Flask, request, jsonify, abort

from instance.config import APP_CONFIG
from app.api.v1.models import UserModel

def create_app(config_name):
    '''Instantiate the Flask application'''

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(APP_CONFIG[config_name])
    app.config.from_pyfile('config.py')

    @app.route('/auth/signup', methods=['POST'])
    def user_registration():
        '''API endpoint for user registration'''
        username = str(request.args.get('username'))
        email = str(request.args.get('email'))
        password = UserModel.generate_password_hash(str(request.args.get('password')))

        # Create an instance of the user
        user = UserModel(username=username, email=email, password=password)

        UserModel.add_user(user.user_as_dict())

        response = jsonify({
            'status': 201,
            'data': [
                {
                    'id': user.get_user_id(),
                    'message': "Create user record"
                }
            ]
        })
        response.status_code = 201
        return response

    @app.route('/auth/login', methods=['POST'])
    def user_login():
        '''API endpoint for the user login'''
        data = request.get_json()
        username = data['username']
        password = UserModel.generate_password_hash(data['password'])

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

    return app
