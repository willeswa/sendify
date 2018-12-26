""" This module holds classes that handle users methods """
from app.db_config import Database
from flask_jwt_extended import create_access_token


db = Database()


class UserModels:
    """ This class holds methods that manipulate the users table """

    def create_user(self, name, email, password):
        """ creates user and saves to db """
        self.name = name
        self.email = email
        self.password = password

        with db as conn:
            curr = conn.cursor()
            query = """ INSERT INTO users (email, name, password) VALUES (%s, %s, %s)"""
            curr.execute(query, (self.email, self.name, self.password))
            conn.commit()
            return "Successfully created created account"

    def sign_in(self, email, password):
        """ Checks if user credentials are correct """
        self.email = email
        self.password = password

        with db as conn:
            curr = conn.cursor()
            query = """ SELECT email, password, name, admin, user_id FROM users WHERE email = %s """
            curr.execute(query, (self.email,))
            record = curr.fetchone()
            if record and record[0] == self.email:
                if record[1] == self.password:
                    access_token = create_access_token(
                        {'name': record[2], 'user_id':record[4], 'email': self.email, 'admin': record[3]})
                    return access_token
                else:
                    return 'Wrong Password!'
            else:
                return 'Email not registered'
            
    