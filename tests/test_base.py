""" This modelu holds common class to other modules """
from app import create_app
import unittest


class BaseClass(unittest.TestCase):
    """ Holds methods that are common to all test classes """

    def setUp(self):
        """ creates test client"""
        self.app = create_app('testing')
        self.client = self.app.test_client()