""" This module holds the classes to test parcels models and views """
import json
from flask_restful import abort
from app.api.v1.models.parcel_models import ParcelModels
from tests import BaseTestClass

parcel_models = ParcelModels()


class TestVersion1(BaseTestClass):
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

    def test_retrieve_parcels(self):
        """ tests the route that retrieves all parcels """
        response = self.client.get('/api/v1/parcels')
        self.assertEqual(response.status_code, 200)

    def test_order_details(self):
        """ tests the order details model """
        response = parcel_models.view_order_details(1)
        self.assertEquals(response['parcel_id'], 1)

    def test_views_for_parcel_details(self):
        """ Tests the response when one visits the url to view a parcel """
        response = self.client.get('/api/v1/parcels/1')
        self.assertEqual(response.status_code, 200)

    def test_user_specific_method(self):
        """ tests the user specific method """
        response = parcel_models.user_specific_parcels(1)
        self.assertEqual(response[0]['user_id'], 1)

    def test_user_specific_view(self):
        """ tests the response for the specific user view route """
        response = self.client.get('/api/v1/users/2/parcels')
        self.assertEqual(response.status_code, 200)

    def test_no_parcel_for_specific_user(self):
        """ tests the response when there are no parcels for a specific user """
        response = parcel_models.user_specific_parcels(5)
        self.assertEqual(response, 'No Parcels by user 5')

    def test_cancel_parcel(self):
        """ tests the method that cancels a parcel """
        response = parcel_models.cancel_parcel(1)
        canceled = parcel_models.cancel_parcel(2)
        delivered = parcel_models.cancel_parcel(3)
        self.assertEqual(delivered, 'This parcel is already delivered, it cannot be canceled')
        self.assertEqual(response, 'successfully canceled parcel 1'.capitalize())
        self.assertEqual(canceled, 'The parcel is already canceled')

    def test_cancel_parcel_view(self):
        """ Test for the response from the cancel parcel view """
        response = self.client.put('/api/v1/parcels/1/cancel')
        self.assertEqual(response.status_code, 200)
