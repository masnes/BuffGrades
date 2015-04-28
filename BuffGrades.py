#!/usr/bin/env python3
import sys

import src.gui as gui
import src.db as db

def usage():
    print('''
Usage:  python BuffGrades.py [options]

Options:
    -h  print this help
    -g  Show the gui
    -d  test the database scaffold prior to starting the gui
''')

def main():
    run_db = False
    show_gui = False
    show_usage = False

    for arg in sys.argv[1:]: # first item in argv is the program name
        if 'h' in arg:
            show_usage = True
        if 'd' in arg:
            run_db = True
        if 'g' in arg:
            show_gui = True

    if show_usage == True:
        usage()
    elif run_db != True and show_gui != True:
        usage()

    if run_db == True:
        db.DatabaseSetup()
    if show_gui == True:
        gui.run_gui()



if __name__ == '__main__':
    main()
