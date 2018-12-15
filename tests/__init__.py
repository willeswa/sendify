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

    
