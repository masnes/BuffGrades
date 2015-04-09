
from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
from TableData import TABLES, TABLEORDER

DB_NAME = 'BuffGrades'

class DatabaseSetup(object):
    def __init__(self):
       cnx, cursor = self.connect()
       self.connect_to_and_or_create_database(cnx, cursor)
       self.create_tables(cursor)
       print("Created Tables Successfully")
       self.add_name(cnx, cursor)
       self.finish(cnx, cursor)
    
    def connect(self):
       try:
          print("Attempting Connection")
          cnx = mysql.connector.connect(user='root',password= 'pass', database="BuffGrades")
          print("Creating Cursor")
          cursor = cnx.cursor()
          
          return cnx, cursor
       except mysql.connector.Error as err:
          print("Connection Failed: {} , Attempting to create database".format(err))
          cnx = mysql.connector.connect(user='root', password='pass')
          return cnx, cnx.cursor()
    
    def connect_to_and_or_create_database(self, cnx, cursor):
       try:
          cnx.database = DB_NAME    
       except mysql.connector.Error as err:
          if err.errno == errorcode.ER_BAD_DB_ERROR:
             self.create_database(cursor)
             cnx.database = DB_NAME
          else:
             print(err)
             exit(1)
    
    def create_database(self, cursor):
       try:
          cursor.execute(
             "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
       except mysql.connector.Error as err:
          print("Database Creation FAILURE: {}".format(err))
          exit(1)

    def create_tables(self, cursor):
        for name in TABLEORDER:
          ddl = TABLES[name]
        try:
            print("Creating table {}: ".format(name), end='')
            cursor.execute(ddl)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("All set")
             
    def add_name(self, cnx, cursor):
        try:
            user = raw_input("Please enter your desired username")
            first = raw_input("Please enter your first name")
            last = raw_input("please enter your last name")
            
            addName_Data = (user, first, last)
            
            addName = ("INSERT INTO personal_info"
                    "(userName, firstName, lastName) "
                    "VALUES (%ss, %s, %s)")
                    
            cursor.execute(addName, addName_Data)
            cnx.commit()
            exit(1)
        except mysql.connector.Error as err:
            print(err.msg)

    def finish(self, cnx, cursor):
       cursor.close()
       cnx.close()
       print("Database setup complete.")

if __name__ == '__main__':
    DatabaseSetup()
