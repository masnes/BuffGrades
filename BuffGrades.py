
from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode


DB_NAME = 'BuffGrades'

TABLES = {}
TABLES['users_students'] = (
    "CREATE TABLE `users_students` ("
	"studentId int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,"
	"userNameId varchar(16) NOT NULL,"
	"courseId varchar(8) NOT NULL);"
    "  PRIMARY KEY (`studentID`)"
    ") ENGINE=InnoDB")


TABLES['personal_info'] = (
    "CREATE TABLE `personal_info` ("
	"personalInfoId int(11) AUTO_INCREMENT NOT NULL,"
	"userName varchar(16) NOT NULL,"
	"firstName varchar(16) NOT NULL,"
	"lastName varchar(16) NOT NULL,"
	"  PRIMARY KEY (`personalInfoId`)"
    ") ENGINE=InnoDB")
    
TABLES['courses'] = (
	"CREATE TABLE courses ("
	"id int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,"
	"assignmentId int(8) NOT NULL,"
	"courseId varchar(8) NOT NULL,"
	"courseName varchar(30) NOT NULL,"
	"assignmentTypeId varchar(12) NOT NULL);"
    "  PRIMARY KEY ('id')"
    ")ENGINE=InnoDB")

TABLES['assignmentTypeId']=(
	"CREATE TABLE assignmentTypeId ("
	"id int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,"
	"assignmentTypeID varchar(8) NOT NULL,"
	"assignmentId varchar(30) NOT NULL,"
	"typeName varchar(12) NOT NULL,"
	"typeWeight int(3) NOT NULL,"
	"numOfAssigns int(3) NOT NULL);"
	"PRIMARY KEY ('id')"
	") ENGINE=InnoDB")

TABLES['assignment'] = (
    "CREATE TABLE `personal_info` ("
	"id int(11) AUTO_INCREMENT NOT NULL,"
	"assignmentID int(8) NOT NULL,"
	"assigmentTypeID varchar(16) NOT NULL,"
	"pointsPossible int(4) NOT NULL,"
	"studentScore int(4) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")
try:
	cnx = mysql.connector.connect(user='root',password= 'pass', database='test')
	cursor = cnx.cursor()
	print("Connection attempted")
except mysql.connector.Error as err:
	print("Game Over man, Game Over: {}".format(err))

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Database Creation FAILURE: {}".format(err))
        exit(1)
try:
    cnx.database = DB_NAME    
    print("aaaaaaaaaargh")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)
for name, ddl in TABLES.iteritems():
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

cursor.close()
cnx.close()
