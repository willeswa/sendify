from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse
from app.api.v2.models.parcel_models import ParcelModels
from app.validators import Validator
from app.db_config import Database

parcel_models = ParcelModels()
db = Database()


class ParcelViews(Resource):
    """ 
    This method holds methods that control methods that manipulate parcels data
    """

    def __init__(self):
        self.validators = Validator()
        self.parser = reqparse.RequestParser()

    @jwt_required
    def post(self):
        """ retrieves all parcels in the """
        self.parser.add_argument(
            'title', required=True, type=self.validators.validate_string_fields, help='Must provide a value', location='json')
        self.parser.add_argument(
            'weight', required=True, type=self.validators.validate_int_fields, help='Weight must be an integer or a float', location='json')
        self.parser.add_argument(
            'rec_name', required=True, type=self.validators.validate_string_fields, help='Must provide a value', location='json')
        self.parser.add_argument(
            'rec_email', required=True, type=self.validators.validate_string_fields, help='Must provide a value', location='json')
        self.parser.add_argument(
            'address', required=True, type=self.validators.validate_string_fields, help='Must provide a value', location='json')
        self.parser.add_argument(
            'postal_code', required=True, type=self.validators.validate_string_fields, help='Must provide a value', location='json')
        self.parser.add_argument(
            'pick_up', required=True, type=self.validators.validate_string_fields, help='Must provide a value', location='json')
        parcel = self.parser.parse_args()
        response = parcel_models.create_parcel(parcel['title'],
                                               parcel['rec_name'],
                                               parcel['rec_email'],
                                               parcel['address'],
                                               parcel['postal_code'],
                                               parcel['pick_up'],
                                               parcel['weight'])
        return {"message": response}

    @jwt_required
    def get(self):
        """ Controls method to retrieve all parcels """
        response = parcel_models.get_all_parcels()
        return {"message": response}


class ParcelView(Resource):
    """ Handles routes to manipute specific orders """

    def __init__(self):
        self.validators = Validator()
        self.parser = reqparse.RequestParser()

    @jwt_required
    def put(self, parcel_id):
        """ updates the status of a parcel appropriately """
        self.parser.add_argument(
            'status', required=True, type=self.validators.validate_string_fields, help='Must provide status', location='json')
        parcel = self.parser.parse_args()

        response = parcel_models.cancel_parcel(parcel_id, parcel['status'])
        return {"message": response}
