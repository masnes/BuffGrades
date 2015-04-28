#!/usr/bin/env python3
import sys

import src.gui as gui
import src.db as db

def usage():
    print('''
Usage:  python BuffGrades.py [options]

Options:
    -h            print this help
    -g            Show the gui
    -d            test the database scaffold prior to starting the gui
                    MySQL Username and Password Required
                    Defaults to 'root' and 'pass'

                  (warning, GUI is not currently linked to the database)

    -u:username   MySQL username
    -p:password   MySQL password

Ex:

python3 BuffGrades.py -g -d -u:test -p:testpass

''')

def main():
    run_db = False
    show_gui = False
    show_usage = False
    mysql_user = 'root'
    mysql_pass = 'pass'

    for arg in sys.argv[1:]: # first item in argv is the program name
        if '-u:' == arg[:3]:
            mysql_user = arg[3:]
        elif '-p:' == arg[:3]:
            mysql_pass = arg[3:]
        else:
            if 'h' in arg and arg[0] == '-':
                show_usage = True
            if 'd' in arg and arg[0] == '-':
                run_db = True
            if 'g' in arg and arg[0] == '-':
                show_gui = True


    if show_usage == True:
        usage()
    elif run_db != True and show_gui != True:
        usage()

    if run_db == True:
        db.DatabaseSetup(mysql_user, mysql_pass)
    if show_gui == True:
        gui.run_gui()



if __name__ == '__main__':
    main()
