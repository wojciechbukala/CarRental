from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from endpoints import *
from interface import *
from logreg import *
import sys

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
            # connecting signals to slots
        self.ui.loginBtn.clicked.connect(self.on_loginBtn_clicked)
        self.ui.createAccountBtn.clicked.connect(self.on_createAccountBtn_clicked)

    def on_loginBtn_clicked(self):
        password = self.ui.lineEdit_2.text()
        email = self.ui.lineEdit.text()
        if(password != "" and email != ""):
            login_status = login(email, password)
            if login_status == 0:
                self.hide()
                self.window = MainWindow()
                self.window.show()
            else:
                print("Login failed!")
        else:
            print("No email or password!")
            # GET user where user.username == username
            # if user.password == password:
            #   login()
            # else: 
            #   ERROR
            # print("Logging in!")

    def on_createAccountBtn_clicked(self):
        firstname = self.ui.lineEdit_7.text()
        lastname = self.ui.lineEdit_6.text()
        password = self.ui.lineEdit_4.text()
        email = self.ui.lineEdit_3.text()
        if((firstname!="")&(lastname!="")&(email!="")&(password!="")):
            register(firstname, lastname, email, password)
            dialogWindow = addressDialog()
            if dialogWindow.exec():
                [address1, address2, postal_code, city, country, phone_number] = dialogWindow.returnAddress()
                print(address1)
                register_address(email, address1, address2, postal_code, city, country, phone_number)


if __name__== '__main__':
    app  = QApplication(sys.argv)
    windowL  = LoginRegister()
    windowL.show()
    app.exec()    