'''Application module'''
import json

from flask import Flask, request, jsonify, abort, make_response

from instance.config import APP_CONFIG
from app.api.v1.user_model import UserModel

from app.api.v1.user_view import AUTH

def create_app(config_name):
    '''Instantiate the Flask application'''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(APP_CONFIG[config_name])
    app.config.from_pyfile('config.py')
    app.register_blueprint(AUTH)
    return app
