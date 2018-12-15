""" This module holds the classes to test parcels models and views """
import json
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
        self.assertEqual(result['message'], 'Successfully created parcel')

    def test_create_parcel_view(self):
        """ tests the view for creating parcel """
        response = self.client.post('/api/v1/parcels',
                                    data=json.dumps(self.parcel),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_parcel_data_validation(self):
        """ tests if the data is correctly validated """
        response = self.client.post('/api/v1/parcels',
                                    data=json.dumps(self.empty_parcel),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)