from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from endpoints import *

class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        uic.loadUi("form.ui", self)
        self.show()
        self.Quit.clicked.connect(lambda: quit())
        self.Connect.clicked.connect(lambda: connect(MyWidget))


def connect(MyWidget):
    message = QMessageBox()
    message.setText("Connected!")
    message.exec()
    MyWidget.DBinfo.setText("cos z bazy danych")
def main():
    app  = QApplication([])
    widnow  = MyWidget()
    app.exec()

if __name__== '__main__':
    main()