import sys

import src.gui as gui
import src.db as db

def usage():
    print('''
Usage:  python BuffGrades.py [options]

Options:
    -h  print this help
    -d  test the database scaffold prior to starting the gui
''')

def main():
    run_db = False
    for arg in sys.argv[1:]: # first item in argv is the program name
        if 'h' in arg:
            usage()
            return
        if 'd' in arg:
            run_db = True

    if run_db != False:
        db.DatabaseSetup()
    gui.run_gui()

if __name__ == '__main__':
    main()
