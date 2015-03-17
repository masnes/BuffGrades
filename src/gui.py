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

def main():
    app = QApplication(sys.argv)
    grades = Grades()
    grades.show()
    app.exec_()

if __name__ == '__main__':
    main()