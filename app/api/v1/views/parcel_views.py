""" This module holds classes that handles the parcels views """
from flask_restful import Resource, reqparse
from app.api.v1.models.parcel_models import ParcelModels

parcels = []


class ParcelViews(Resource):
    """ This class defines the post and get all parcels methods """

    def __init__(self):
        self.db = parcels
        self.parcel_models = ParcelModels()

    def validate_int_fields(self, field_value):
        """ validate fields that accept integers """
        if isinstance(field_value, int):
            return float(field_value)
        else:
            raise ValueError

    def validate_string_fields(self, field_value):
        """ validates fields that accept strings """
        if field_value:
            return field_value
        else:
            raise ValueError

    def post(self):
        """ Validates the parcel data and posts """
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            'user_id', required=True, type=int, help='Must provide a value', location='json')
        self.parser.add_argument(
            'title', required=True, type=self.validate_string_fields, help='Must provide a value', location='json')
        self.parser.add_argument(
            'weight', required=True, type=self.validate_int_fields, help='Weight must be an integer or a float', location='json')
        self.parser.add_argument(
            's_name', required=True, type=self.validate_string_fields, help='Must provide a value', location='json')
        self.parser.add_argument(
            's_email', required=True, type=self.validate_string_fields, help='Must provide a value', location='json')
        self.parser.add_argument(
            'r_id_no', required=True, type=self.validate_string_fields, help='Must provide a value', location='json')
        self.parser.add_argument(
            'r_email', required=True, type=self.validate_string_fields, help='Must provide a value', location='json')
        self.parser.add_argument(
            'pick_up', required=True, type=self.validate_string_fields, help='Must provide a value', location='json')
        self.parser.add_argument(
            'destination', required=True, type=self.validate_string_fields, help='Must provide a value', location='json')

        parcel = self.parser.parse_args()
        response = self.parcel_models.create_parcel(parcel['user_id'],
                                                    parcel['title'],
                                                    parcel['weight'],
                                                    parcel['s_name'],
                                                    parcel['s_email'],
                                                    parcel['r_id_no'],
                                                    parcel['r_email'],
                                                    parcel['pick_up'],
                                                    parcel['destination'])
        return response['message'], 201

    def get(self):
        """ allows users to retrieve all data """
        response = self.parcel_models.get_all_parcels()
        return {'message': response}, 200


class ParcelView(Resource):
    """ This class contains methods to controll specific parcels """
    
    def __init__(self):
        self.db = parcels
        self.parcel_models = ParcelModels()

    def get(self, parcel_id):
        """ Control method to get a specific parcel """
        response = self.parcel_models.view_order_details(parcel_id)
        return {'message': response}, 200
