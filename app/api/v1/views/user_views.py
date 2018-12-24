""" This module holds classes that control user views """
from flask_restful import Resource
from app.api.v1.models.parcel_models import ParcelModels

parcel_models = ParcelModels()


class UserView(Resource):
    """ This class holds methods that point to specific user related methods """

    def get(self, user_id):
        """ Retrieves user specific parcels """
        response = parcel_models.user_specific_parcels(user_id)
        return {"message": response}, 200
