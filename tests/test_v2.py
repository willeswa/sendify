""" This module holds methods that test v2 """
from tests import BaseTestClass
from app.db_config import init_db, destroy_tables, connection
from psycopg2 import Error

class TestVersion2(BaseTestClass):
    
    def test_dbconnection(self):
        """ tests db conncetion """
        con = connection("host='localhost' dbname='_sendify' user='postgres' password='star2030'")
        conn = init_db()
        self.assertEqual(conn.get_dsn_parameters()['dbname'], 'db_sendify')
        self.assertEqual(con, None)

    
