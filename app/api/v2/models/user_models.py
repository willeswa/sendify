""" This module holds classes that handle users methods """
from app.db_config import init_db


class UserModels:
    """ This class holds methods that manipulate the users table """

    def __init__(self):
        """ initializes the connection """
        self.db = init_db()

    def create_user(self, name, email, password):
        """ creates user and saves to db """
        self.name = name
        self.email = email
        self.password = password

        query = """ INSERT INTO users (email, name, password) VALUES (%s, %s, %s)"""
        curr = self.db.cursor()
        curr.execute(query, (self.email, self.name, self.password))
        self.db.commit()
        return "Successfully created created account"

    def sign_in(self, email, password):
        """ Checks if user credentials are correct """
        self.email = email
        self.password = password

        query = """ SELECT email, password FROM users WHERE email = %s """
        curr = self.db.cursor()
        curr.execute(query, (self.email,))
        record = curr.fetchone()
        if record and record[0] == self.email:
            if record[1] == self.password:
                return 200
            else:
                return 'Wrong Password!'
        else:
            return 'Email not registered'
