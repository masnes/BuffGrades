.. BuffGrades documentation master file, created by
   sphinx-quickstart on Thu Apr 23 12:19:42 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to BuffGrades's documentation!
======================================

.. toctree::
   :maxdepth: 2

   BuffGrades
   TestBuffGrades
   TableData

.. module:: BuffGrades


The Functions
+++++++++++++

.. function:: __init__(self)
	This function initializes the database, setting up all the basic tables with no info.


.. function:: connect(self)
	This function attempts to connect to the database.


.. function:: connect_to_and_or_create_database(self, cnx, cursor)
	Creates cursor and cnx connection object, runs create_database to create database if one does not exist


.. function:: create_database(self, cursor)
	Has the cursor actually create the MySQL database


.. function:: create_tables(self, cursor)
	Creates all the tables with proper MySQL syntax and BuffGrades formatting


.. function:: add_name(self, cnx, cursor)
	Has user enter desired Username, and First and Last names, adds info into personal_info table


.. function:: finish(self, cnx, cursor)
	Deconstructor, closes cnx and cursor objects




Indices and tables
==================

* :ref:`modindex`
* :ref:`search`

