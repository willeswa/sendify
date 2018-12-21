""" This module configures database connections """
from .config import app_config
import os
import psycopg2
from psycopg2 import Error

env = os.getenv('FLASK_ENV')

if 'testing':
    uri = "host='localhost' dbname='db_sendify' user='postgres' password='star2030'"
else:
    uri = app_config[env].DATABASE_URI


def connection(url):
    """ Initiates connection with the database """
    try:
        conn = psycopg2.connect(uri)
        return conn
    except (Exception, Error) as error:
        print(error)


def create_table():
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
            status VARCHAR DEFAULT 'In Transit',
            created_on TIMESTAMP DEFAULT NOW()
        );""",)

    conn = init_db()
    curr = conn.cursor()
    for query in queries:
        curr.execute(query)
    conn.commit()


def init_db():
    """ provides an entry point for the uri """
    conn = connection(uri)
    return conn


def destroy_tables():
    """ deletes tables from the database """
    conn = init_db()
    curr = conn.cursor()
    queries = ("""DROP TABLE IF EXISTS parcels;""",
               """ DROP TABLE IF EXISTS users CASCADE;""",)
    try:
        for query in queries:
            curr.execute(query)
            conn.commit()
    except (Exception, Error) as error:
        print(error)
