""" This module controls user related views """
from flask_restful import Resource, reqparse
from app.validators import Validator
from flask_jwt_extended import jwt_required
from app.db_config import Database
from app.api.v2.models.user_models import UserModels
from app.api.v2.models.parcel_models import ParcelModels

db = Database()
parcel_models = ParcelModels()


class SignupViews(Resource):
    """ controls methods related to user signup """

    def __init__(self):
        self.db = db.init_db()
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


class LoginViews(Resource):
    """ Controls methods related to user login """

    def __init__(self):
        """ Initiate class variables """
        self.db = db.init_db()
        self.parser = reqparse.RequestParser()
        self.validator = Validator()
        self.user_models = UserModels()

    def post(self):
        """ passes user data to the login method """
        self.parser.add_argument(
            'email', required=True, type=self.validator.validate_string_fields, help='Enter a valid email')
        self.parser.add_argument(
            'password', required=True, type=self.validator.validate_string_fields, help='Password cannot be empty')

        user = self.parser.parse_args()
        response = self.user_models.sign_in(user['email'],
                                            user['password'])
        return {"message": response}


class UserView(Resource):
    """ Controls user specific requests """

    def __init__(self):
        """ Initiate class variables """
        self.db = db.init_db

    @jwt_required
    def get(self, user_id):
        """ calls the method to retrieve user specific parcels """
        response = parcel_models.get_user_specific_parcels(user_id)
        return {"message": response}

    def put(self, parcel_id):
        """ update parcel status """