from PySide.QtGui import *
from PySide.QtCore import *

import sys

import dummy_class_data as data

class Grades(QDialog):

    def __init__(self, parent=None):
        super(Grades, self).__init__(parent)
        self.course_data = data.course_data

        self.course_name_label = QLabel(self.course_data["course_name"])

        self.create_layout()

    def create_layout(self):
        layout = QGridLayout()
        layout.addWidget(self.course_name_label, 0, 0)
        offset = 1
        for i, (assignment_type_label, grade_labels) in enumerate(self._gen_labels()):
            layout.addWidget(assignment_type_label, i+offset, 0)
            for grade_label in grade_labels:
                offset += 1
                layout.addWidget(grade_label, i+offset, 1)
        self.setLayout(layout)


    def _gen_labels(self):
        for assignment_type in self.course_data["assignment_types"].keys():
            yield self._assignment_data(assignment_type)

    def _assignment_data(self, assignment_type):
        grades = self.course_data["assignment_types"][assignment_type]
        assignment_type_label = QLabel(assignment_type)
        grade_labels = [QLabel(str(i)) for i in grades]
        return (assignment_type_label, grade_labels)

class AddAssignment(QWidget):
    def __init__(self, classname, assignment_type, parent=None):
        super(AddAssignment, self).__init__(parent)

        self.addAssignment = QLabel('Add an assignment')
        self.name = QLineEdit()
        self.name.setPlaceholderText('Assignment Name')
        self.grade = QSpinBox()
        self.grade.setMinimum(0)
        self.grade.setMaximum(200)

        self.submit = QPushButton('Submit')
        self.submit.clicked.connect(lambda: self.submit_assignment(classname, assignment_type))

        layout = QVBoxLayout()
        layout.addWidget(self.addAssignment)
        layout.addWidget(self.name)
        layout.addWidget(self.grade)
        layout.addWidget(self.submit)
        self.setLayout(layout)

    def new(self):
        self.name.setText('')
        self.grade.setValue(100)

    def submit_assignment(self, classname, assignment_type):
        name = self.name.text()
        grade = self.grade.value()
        msgBox = QMessageBox()
        msgBox.setText("Assignment submitted. Class: {}, type: {}, name: {}, "
                       "grade: {}%".format(classname, assignment_type, name, grade))
        msgBox.exec_()
        self.new()
        # TODO:
        # db.add_assignment(classname, assignment_type, assignment_name, grade)


class AddClass(QWidget):
    def __init__(self, parent=None):
        super(AddClass, self).__init__(parent)

        self.add_classname = QLabel('Add another Class')
        self.name = QLineEdit()
        self.name.setPlaceholderText('Class Name')



        self.submit = QPushButton('Submit')
        self.submit.clicked.connect(lambda: self.submit_classname())

        layout= QVBoxLayout()
        layout.addWidget(self.add_classname)
        layout.addWidget(self.name)
        layout.addWidget(self.submit)
        self.setLayout(layout)


    def submit_classname(self):
        classname = self.name.text()
        msgbox = QMessageBox()
        msgbox.setText("{}, class created!".format(classname))
        msgbox.exec_()

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        grades_window = Grades()
        add_assignment_window = AddAssignment('test class', 'test assignment type')
        add_classname = AddClass()

        self.stackedLayout = QStackedLayout()
        self.stackedLayout.addWidget(grades_window)
        self.stackedLayout.addWidget(add_classname)
        self.stackedLayout.addWidget(add_assignment_window)
        # add other windows here

        self.frame = QFrame()
        self.frame.setLayout(self.stackedLayout)

        self.button1 = QPushButton('Grades')
        self.button1.clicked.connect(lambda: self.stackedLayout.setCurrentIndex(0))
        self.button2 = QPushButton('Add a Class')
        self.button2.clicked.connect(lambda: self.stackedLayout.setCurrentIndex(1))
        self.add_assignment_button = QPushButton('Add Assignment')
        self.add_assignment_button.clicked.connect(lambda: self.stackedLayout.setCurrentIndex(2))
        # add buttons for other windows here

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.button2)
        buttonLayout.addWidget(self.button1)
        buttonLayout.addWidget(self.add_assignment_button)
        # and here

        layout = QVBoxLayout(self)
        layout.addLayout(buttonLayout)
        layout.addWidget(self.frame)

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
