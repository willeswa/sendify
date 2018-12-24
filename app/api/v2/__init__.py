""" This module defines blueprints for version 1 """
from flask_restful import Api
from flask import Blueprint

from app.api.v2.views.user_views import SignupViews, LoginViews

v2 = Blueprint('version2', __name__, url_prefix='/api/v2')
api = Api(v2, catch_all_404s=True)

api.add_resource(SignupViews, '/auth/signup')
api.add_resource(LoginViews, '/auth/login')
