# from flask_jwt_extended import jwt_required, get_jwt_identity
# from flask_restful import Resource
# from app.api.v2.models.parcel_models import ParcelModels

# parcel_models = ParcelModels()


# class ParcelViews(Resource):
#     """ 
#     This method holds methods that control methods that manipulate parcels data
#     """

#     @jwt_required
#     def get(self):
#         """ retrieves all parcels in the """
#         current_user = get_jwt_identity()
#         if current_user[2] == 'admin':
#             pass