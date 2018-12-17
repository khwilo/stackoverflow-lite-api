'''Application module'''
import json

from flask import Flask, request, jsonify, abort, make_response

from instance.config import APP_CONFIG
from app.api.v1.models import UserModel

from app.api.v1.views import AUTH

def create_app(config_name):
    '''Instantiate the Flask application'''

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(APP_CONFIG[config_name])
    app.config.from_pyfile('config.py')

    app.register_blueprint(AUTH)

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
