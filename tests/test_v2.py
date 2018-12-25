""" This module holds methods that test v2 """
import json
from tests import BaseTestClass
import os
from app.db_config import Database
from app.api.v2.models.user_models import UserModels
from psycopg2 import Error


db = Database()
user_models = UserModels()


class TestVersion2(BaseTestClass):
    """ This class holds test methods for version 2 """

    def test_dbconnection(self):
        """ tests db conncetion """
        with db as conn:
            self.assertEqual(conn.get_dsn_parameters()[
                             'dbname'], 'testdb_sendify')

    def test_create_user(self):
        """ tests the methods for creating user """
        response = user_models.create_user(
            "Juma Nature", "jnature@gmail.com", "somepass")
        self.assertEqual(response, "Successfully created created account")

    def test_non_user(self):
        """ test the method that signs in users """
        response = user_models.sign_in("jnature@gmail.com", "somepass")
        self.assertEqual(response, 'Email not registered')

    def test_wrong_entries(self):
        """ tests user reponse for wrong inforation """
        response = user_models.sign_in('janet@gmail.com', "pas")
        self.assertEqual(response, "Wrong Password!")

    def test_create_user_view(self):
        """ tests the view for creating user """
        response = self.client.post('/api/v2/auth/signup',
                                    data=json.dumps(self.user_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_login_views(self):
        """ tests the response for the user login views """
        response = self.client.post('/api/v2/auth/login',
                                    data=json.dumps(self.login_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_wrong_login_pass(self):
        """ tests response for a wrong password """
        response = self.client.post('/api/v2/auth/login',
                                    data=json.dumps(self.wrong_pass),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
