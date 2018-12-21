""" This module holds classes that handle users methods """
from app.db_config import init_db


class UserModels:
    """ This class holds methods that manipulate the users table """

    def __init__(self):
        self.db = init_db()