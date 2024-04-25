from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from endpoints import *
import requests

class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        uic.loadUi("form.ui", self)
        self.show()
        self.Quit.clicked.connect(lambda: quit())
        self.Connect.clicked.connect(lambda: connect(self))


def connect(self):
    message = QMessageBox()
    message.setText("Connected!")
    message.exec()

    response = requests.get('http://127.0.0.1:5000/address')
    data = response.json()

    self.DBinfo.setText(data[0][1])

def main():
    app  = QApplication([])
    widnow  = MyWidget()
    app.exec()

if __name__== '__main__':
    main()