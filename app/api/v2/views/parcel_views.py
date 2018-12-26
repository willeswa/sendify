from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from app.api.v2.models.parcel_models import ParcelModels

parcel_models = ParcelModels()


class ParcelViews(Resource):
    """ 
    This method holds methods that control methods that manipulate parcels data
    """

    @jwt_required
    def post(self):
        """ retrieves all parcels in the """
        response = parcel_models.create_parcel("come", "name", "email", "add", "po", "pi", 25)
        return {"message": response}
