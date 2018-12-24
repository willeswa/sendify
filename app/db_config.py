""" This module configures database connections """
from .config import app_config
import os
import psycopg2
from psycopg2 import Error

env = os.getenv('FLASK_ENV')
if env:
    uri = app_config[env].DATABASE_URI
else:
    uri = "host='localhost' dbname='testdb_sendify' user='postgres' password='star2030'"


class Database:
    """ Handles database connection """

    def __enter__(self):
        self.conn = psycopg2.connect(uri)
        return self.conn

    def __exit__(self, exc_type, exc_val, traceback):
        self.conn.close()

    def connection(self, uri):
        with Database() as conn:
            return conn

    def init_db(self):
        """ provides an entry point for the uri """
        conn = self.connection(uri)
        return conn

    def create_table(self):
        """ creates tables in the database """
        queries = ("""
            CREATE TABLE IF NOT EXISTS users(
                user_id SERIAL UNIQUE,
                email VARCHAR UNIQUE NOT NULL,
                name VARCHAR NOT NULL,
                password VARCHAR NOT NULL,
                admin BOOLEAN DEFAULT False);""",
                   """CREATE TABLE IF NOT EXISTS parcels(
                parcel_id SERIAL,
                title VARCHAR NOT NULL,
                sender_name VARCHAR NOT NULL,
                sender_email VARCHAR NOT NULL,
                rec_name VARCHAR NOT NULL,
                rec_email VARCHAR NOT NULL,
                address VARCHAR NOT NULL,
                postal_code VARCHAR NOT NULL,
                pick_up VARCHAR NOT NULL,
                current_location VARCHAR NOT NULL,
                weight NUMERIC NOT NULL,
                bill NUMERIC NOT NULL,
                user_id integer REFERENCES users (user_id) ON DELETE CASCADE,
                status VARCHAR DEFAULT 'Pending Approval',
                created_on DATE NOT NULL DEFAULT CURRENT_DATE
            );""",)
        with Database() as conn:
            curr = conn.cursor()
            for query in queries:
                curr.execute(query)
            conn.commit()

    def destroy_tables(self):
        """ deletes tables from the database """
        with Database() as conn:
            queries = ("""DROP TABLE IF EXISTS parcels;""",
                       """ DROP TABLE IF EXISTS users CASCADE;""",)
            curr = conn.cursor()
            for query in queries:
                curr.execute(query)
                conn.commit()
