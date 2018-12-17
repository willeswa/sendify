""" This module defines blueprints for version 1 """
from flask_restful import Api
from flask import Blueprint

from app.api.v1.views.parcel_views import ParcelViews, ParcelView
from app.api.v1.views.user_views import UserView

v1 = Blueprint('version1', __name__, url_prefix='/api/v1')
api = Api(v1, catch_all_404s=True)

api.add_resource(ParcelViews, '/parcels')
api.add_resource(ParcelView, '/parcels/<int:parcel_id>')
api.add_resource(UserView, '/users/<int:user_id>/parcels')
