'''Application module'''
import json

from flask import Flask, request, jsonify, abort, make_response
from flask_jwt_extended import JWTManager

from instance.config import APP_CONFIG
from app.api.v1.models.user_model import UserModel

from app.api.v1.views.user_view import AUTH
from app.api.v1.views.question_view import API

def create_app(config_name):
    '''Instantiate the Flask application'''
    app = Flask(__name__, instance_relative_config=True)
    jwt = JWTManager(app)
    app.config.from_object(APP_CONFIG[config_name])
    app.config.from_pyfile('config.py')
    app.register_blueprint(AUTH)
    app.register_blueprint(API)
    return app
