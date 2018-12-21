""" This module controls user related views """
from flask_restful import Resource, reqparse
from app.validators import Validator
from app.db_config import init_db
from app.api.v2.models.user_models import UserModels


class SignupViews(Resource):
    """ controls methods related to user signup """

    def __init__(self):
        self.db = init_db
        self.parser = reqparse.RequestParser()
        self.validator = Validator()
        self.user_models = UserModels()

    def post(self):
        """ passes user data to the signup method """
        self.parser.add_argument(
            'name', required=True, type=self.validator.validate_string_fields, help='Enter a valid name')
        self.parser.add_argument(
            'email', required=True, type=self.validator.validate_string_fields, help='Must be a valid email')
        self.parser.add_argument(
            'password', required=True, type=self.validator.validate_string_fields, help='Must enter a valid password')

        user = self.parser.parse_args()
        response = self.user_models.create_user(user['name'],
                                                  user['email'],
                                                  user['password'])
        return {"message": response}, 201