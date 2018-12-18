""" This module acts as the base test module """

import unittest
from app import create_app


class BaseTestClass(unittest.TestCase):
    """ This class sets methods that are common to all test class """

    def setUp(self):
        """ Creates the app and passes the client for testing """
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.db = [ {
            "bill": 12915,
            "current_loc": "Kibera",
            "destination": "gas",
            "parcel_id": 1,
            "pick_up": "Kibera",
            "r_email": "pwanjala@gmail.com",
            "r_id_no": "30197811",
            "s_email": "gwiliez@gmail.com",
            "s_name": " ",
            "status": "in transit",
            "title": "Dornish Wine",
            "user_id": 2,
            "weight": 105
        }, {
            "bill": 12915,
            "current_loc": "Kibera",
            "destination": "gas",
            "parcel_id": 3,
            "pick_up": "Kibera",
            "r_email": "pwanjala@gmail.com",
            "r_id_no": "30197811",
            "s_email": "gwiliez@gmail.com",
            "s_name": " ",
            "status": "in transit",
            "title": "Dornish Wine",
            "user_id": 2,
            "weight": 105
        },{
            "bill": 12915,
            "current_loc": "Kibera",
            "destination": "gas",
            "parcel_id": 2,
            "pick_up": "Kibera",
            "r_email": "pwanjala@gmail.com",
            "r_id_no": "30197811",
            "s_email": "gwiliez@gmail.com",
            "s_name": " ",
            "status": "in transit",
            "title": "Dornish Wine",
            "user_id": 2,
            "weight": 105
        }]

    parcel = {
        'user_id': 1,
        'title': 'Dornish Wine',
        'weight': 32,
        's_name': 'Wanjala',
        's_email': 'gwiliez@gmail.com',
        'r_id_no': '30197811',
        'r_email': 'Kagwe@gmail.com',
        'pick_up': 'Kibera',
        'destination': 'Kangemi'
    }

    empty_parcel = {
        'user_id': 1,
        'title': '',
        'weight': 32,
        's_name': 'Wanjala',
        's_email': 'gwiliez@gmail.com',
        'r_id_no': '30197811',
        'r_email': 'Kagwe@gmail.com',
        'pick_up': 'Kibera',
        'destination': 'Kangemi'
    }
