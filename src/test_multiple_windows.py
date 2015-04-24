import sys
from PySide import QtGui

class TestWidget1(QtGui.QWidget):
    def __init__(self, parent=None):
        super(TestWidget1, self).__init__(parent)

        self.textEdit = QtGui.QTextEdit('Text Edit')
        self.listWidget = QtGui.QListWidget()
        self.listWidget.addItem('List Widget')
        self.listWidget.addItem('Second List Widget')

        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.textEdit)
        layout.addWidget(self.listWidget)

class TestWidget2(QtGui.QWidget):
    def __init__(self, parent=None):
        super(TestWidget2, self).__init__(parent)

        self.listWidget = QtGui.QListWidget()
        self.listWidget.addItem('List Widget2')
        self.listWidget.addItem('Second List Widget2')
        self.label = QtGui.QLabel('Label')

        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.listWidget)
        layout.addWidget(self.label)

class Window(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        testWidget1 = TestWidget1()
        testWidget2 = TestWidget2()

        self.stackedLayout = QtGui.QStackedLayout()
        self.stackedLayout.addWidget(testWidget1)
        self.stackedLayout.addWidget(testWidget2)

        self.frame = QtGui.QFrame()
        self.frame.setLayout(self.stackedLayout)

        self.button1 = QtGui.QPushButton('test1')
        self.button1.clicked.connect(lambda: self.stackedLayout.setCurrentIndex(0))
        self.button2 = QtGui.QPushButton('test2')
        self.button2.clicked.connect(lambda: self.stackedLayout.setCurrentIndex(1))

        buttonLayout = QtGui.QHBoxLayout()
        buttonLayout.addWidget(self.button1)
        buttonLayout.addWidget(self.button2)

        layout = QtGui.QVBoxLayout(self)
        layout.addLayout(buttonLayout)
        layout.addWidget(self.frame)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    w = Window()
    w.show()

    sys.exit(app.exec_())
