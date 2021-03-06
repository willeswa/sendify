""" This module acts as the base test module """

import unittest
from app import create_app
from app.db_config import Database
from app.api.v2.models.user_models import UserModels
from app.api.v2.views.user_views import LoginViews

db = Database()
users = UserModels()
user_views = LoginViews()


class BaseTestClass(unittest.TestCase):
    """ This class sets methods and define data common to all test class """

    def setUp(self):
        """ Creates the app and passes the client for testing """
        db.destroy_tables()
        db.create_table()
        self.app = create_app('testing')
        self.client = self.app.test_client()
        users.create_user("Janet Mugogo", "janet@gmail.com", "pass")
        self.db = [{
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
        }, {
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
    empty_parcel2 = {
        "title": "",
        "weight": 35,
        "rec_name": "Sharon Adhiambo",
        "rec_email": "shazz@gmail.com",
        "address": "Lumumba Dr.",
        "postal_code": "00517",
        "pick_up": ""
    }
    user_data = {
        "name": "Wanjala Godfrey",
        "email": "gwiliez@gmail.com",
        "password": "pass"
    }
    empty_user_data = {
        "name": "",
        "email": "gwiliez@gmail.com",
        "password": "pass"
    }

    login_data = {
        "email": "janet@gmail.com",
        "password": "pass"
    }

    wrong_pass = {
        "email": "janet@gmail.com",
        "password": "passw"
    }
