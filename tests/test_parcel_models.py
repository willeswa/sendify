""" This module holds the classes to test parcels models and views """

from app.api.v1.models.parcel_models import ParcelModels
from tests import BaseTestClass

parcel_models = ParcelModels()


class TestParcels(BaseTestClass):
    """ This class holds methods to tests the parcel models methods """

    def test_create_parcel(self):
        """ tests the create parcel method """
        result = parcel_models.create_parcel(1, 'Dornish Wine', 32, 'Wanjala',
                                             'gwiliez@gmail.com', '30197811', 'Kagwe@gmail.com',
                                             'Kibera', 'Kangemi')
        self.assertEqual(result, {'message': 'Successfully created parcel'})
