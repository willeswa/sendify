""" This module holds classes that handle users methods """
from app.db_config import Database
from flask_jwt_extended import create_access_token


db = Database()


class UserModels:
    """ This class holds methods that manipulate the users table """

    def create_user(self, name, email, password):
        """ creates user and saves to db """
        if self.check_if_user_exist(email):
            return 'Email already registered'
        else:
            with db as conn:
                curr = conn.cursor()
                query = """ INSERT INTO users (email, name, password) VALUES (%s, %s, %s)"""
                curr.execute(query, (email, name, password))
                conn.commit()
            return "Successfully created created account"

    def sign_in(self, email, password):
        """ Checks if user credentials are correct """
        if self.check_if_user_exist(email):
            with db as conn:
                curr = conn.cursor()
                query = """ SELECT * FROM users WHERE email = %s """
                curr.execute(query, (email,))
                record = curr.fetchone()
                if record[3] == password:
                    access_token = create_access_token(
                        {'name': record[2], 'user_id': record[0], 'email': email, 'admin': record[4]})
                    return access_token
                else:
                    return 'Incorrect Password!'
        else:
            return 'Email is not registered'

    def check_if_user_exist(self, email):
        with db as conn:
            query = """ SELECT EXISTS (SELECT * FROM users where email = %s) """
            curr = conn.cursor()
            curr.execute(query, (email,))
            exists = curr.fetchone()
            return exists[0]
