from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

import unittest

from src.db import DatabaseSetup, DB_NAME
from src.TableData import TABLES, TABLEORDER

class DatabaseSetupTestMockup(DatabaseSetup):
    def __init__(self):
        """Don't automatically connect, like in the main version"""
        pass

    def dry_connect(self):
        """Connect to mysql without database assigned"""
        cnx = mysql.connector.connect(user='root', password='pass')
        return cnx, cnx.cursor()

    def drop_db(self, db_name):
        """Use this to clear the database for tests"""
        #TODO
        pass



class DatabaseSetupTests(unittest.TestCase):
    def setup(self):
        self.user = 'root'
        self.password = 'pass'
        self.cnx = None
        self.cursor = None
        self.databaseSetupTestMockup = DatabaseSetupTestMockup()

    def test_connect_with_no_database_created(self):
        """Just makes sure cnx is working"""
        cnx, cursor = DatabaseSetupTestMockup().dry_connect()
        assert cnx is not None
        assert cursor is not None

    def tearDown(self):
        pass
