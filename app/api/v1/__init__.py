""" This module defines blueprints for version 1 """
from flask_restful import Api
from flask import Blueprint

from app.api.v1.views.parcel_views import ParcelViews

v1 = Blueprint('version1', __name__, url_prefix='/api/v1')
api = Api(v1, catch_all_404s=True)

api.add_resource(ParcelViews, '/parcels')
