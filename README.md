# BuffGrades
Record your grades, estimate your final grade, see what you need to achieve your goals

Repo Organization:
Currently, our repo was mixed up a bit as we, due to still figuring out quirks of github, merged all of our branches to our master branch.
However, looking at our repo you will find that we still have our original branches under the branches tab and you may
go here to see our original organization. For the most part our master contained many of our class required project tasks, 
and our separate branches, such as connector/python, held our side work in the connector/python. We also had a dedicated 
branch to our gui, which holds much of Michael's and Nish's work on our phenomenal gui. We also have an e_r diagram and
project requirements branch which is open, yet we have merged these to our master. 
The gem of our repo is found within our four beautiful folder's in our organize branch which are Assignment_Submissions,
doc, src, and test. Each folder is, as you would believe, what it says. Our doc has all our generated sphinx documentation,
our src has all of our source code, and our test has our test code. The cherry on top of our gem is the Assignment_Submissions,
which contains all previous assignments we have completed as required by the class.

Finding and Building Doc's:
In order to find go to master branch, enter doc folder, enter BuffGradesDocbuild folder, and execute ./html

Describe how to build/run/test/etc code:

/\ Required Software /\
  Current Versions of:
    - PySide (for python 3) pip install PySide
    - Connector Python: https://dev.mysql.com/downloads/connector/python/
    - MySQL: http://www.mysql.com/downloads/
    - Python: (python 3 required for GUI) https://www.python.org/downloads/

run mysql -u root -p (then enter your password or create the password 'pass' preferably) to start SQL server
run ./BuffGrades.py

*note* There will be a problem running ./BuffGrades.py with the argument to run the database (d) as you need an SQL server running. The SQL 'root' and 'pass' information is currently hardcoded as such within the db.py file, so in order for the Connector Python scripts to run, the 'root' and 'pass' fields must be manually replaced with whatever the login information for you personal SQL server is. This can be found on Line: 21 of the db.py file inside the src folder in the master branch. After manipulating those fields with the proper information, the Connector Python should be able to access and appropriately create and manage a new database for BuffGrades.

CI System:
We are not using a CI System with our project and in fact find it far more gratifying to write and execute our tests
each time by our own free will. Rather than allowing the machines to take control of our baby. CI System, or as some
call it "Skynet."

