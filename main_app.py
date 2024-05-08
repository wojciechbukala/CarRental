from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from endpoints import *
from interface import *
from logreg import *
import sys

# clipboard dump
        # # connecting signals to slots
        # self.loginBtn.clicked.connect(self.on_loginBtn_clicked)
        # self.createAccountBtn.clicked.connect(self.on_createAccountBtn_clicked)
        # def on_loginBtn_clicked(self):
        #     password = self.lineEdit_2.text()
        #     username = self.lineEdit.text()
        #     if(password != "" and username != ""):
        # # GET user where user.username == username
        # # if user.password == password:
        # #   login()
        # # else: 
        # #   ERROR
        #     print("Logging in!")
        # def on_createAccountBtn_clicked(self):
        #     password = self.lineEdit_4.text()
        #     username = self.lineEdit_3.text()
        #     if((password == self.lineEdit_5.text()) & (username!= "") ):
            
        # # POST user(
        # #   VALUES:
        # #   username = username,
        # #   password = password )
        #     print("Registered!")

# class MyWidget(QWidget):
#     def __init__(self):
#         super(MyWidget, self).__init__()
#         uic.loadUi("form.ui", self)
#         self.show()
#         self.Quit.clicked.connect(lambda: quit())
#         self.Connect.clicked.connect(lambda: connect(self))


# def connect(self):
#     message = QMessageBox()
#     message.setText("Connected!")
#     message.exec()

#     response = requests.get('http://127.0.0.1:5000/address')
#     data = response.json()

#     self.DBinfo.setText(data[0][1])
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.moreClientsBtn.clicked(lambda: moreClients())
class LoginRegister(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
# def main():
#     app  = QApplication(sys.argv)
#     window  = MainWindow()
#     window.show()
#     app.exec()
    

if __name__== '__main__':
    app  = QApplication(sys.argv)
    windowL  = LoginRegister()
    windowL.show()
    # window = MainWindow()
    # window.show()
    app.exec()