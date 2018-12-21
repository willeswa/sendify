""" This module defines blueprints for version 1 """
from flask_restful import Api
from flask import Blueprint

from app.api.v1.views.parcel_views import ParcelViews, ParcelView
from app.api.v1.views.user_views import UserView

v2 = Blueprint('version2', __name__, url_prefix='/api/v2')
api = Api(v2, catch_all_404s=True)

api.add_resource(ParcelViews, '/parcels')
api.add_resource(ParcelView, '/parcels/<int:parcel_id>', '/parcels/<int:parcel_id>/cancel')
api.add_resource(UserView, '/users/<int:user_id>/parcels')

