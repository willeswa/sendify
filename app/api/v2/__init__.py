""" This module defines blueprints for version 1 """
from flask_restful import Api
from flask import Blueprint

from app.api.v2.views.user_views import SignupViews, LoginViews
from app.api.v2.views.parcel_views import ParcelViews, ParcelView, ChangeeAddress, ChangeCurrentLocation
from app.api.v2.views.user_views import UserView

v2 = Blueprint('version2', __name__, url_prefix='/api/v2')
api = Api(v2, catch_all_404s=True)

api.add_resource(SignupViews, '/auth/signup')
api.add_resource(LoginViews, '/auth/login')
api.add_resource(ParcelViews, '/parcels')
api.add_resource(UserView, '/users/<int:user_id>/parcels')
api.add_resource(ParcelView, '/parcels/<int:parcel_id>/changestatus', '/parcels/<int:parcel_id>')
api.add_resource(ChangeeAddress, '/parcels/<int:parcel_id>/address')
api.add_resource(ChangeCurrentLocation, '/parcels/<int:parcel_id>/currentlocation')

