""" This module holds methods that test v2 """
from tests import BaseTestClass
import os
from app.db_config import init_db, destroy_tables, connection
from psycopg2 import Error

class TestVersion2(BaseTestClass):
    
    def test_dbconnection(self):
        """ tests db conncetion """
        conn = init_db()
        self.assertEqual(conn.get_dsn_parameters()['dbname'], 'testdb_sendify')

    
