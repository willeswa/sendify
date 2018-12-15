""" This module acts as the base test module """

import unittest
from app import create_app


class BaseTestClass(unittest.TestCase):
    """ This class sets methods that are common to all test class """

    def setUp(self):
        """ Creates the app and passes the client for testing """
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.db = []

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
