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
        self.email = email
        self.password = password

        query = """ SELECT email, password FROM users """
        curr = self.db.cursor()
        curr.execute(query)
        records = curr.fetchall()
        if records[0] == self.email:
            if records[1] == self.password:
                return 'Login Successful'
            else:
                return 'Wrong Password!'
        else:
            return 'Email not registered'