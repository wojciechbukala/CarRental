from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from endpoints import *
from interface_customer import *
from interface_staff import *
from logreg import *
import sys
from rentCarBtn import *
from rentalDetailsWindow import *

# class MainWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
        # self.ui.moreClientsBtn.clicked(lambda: moreClients())
class Staff_Dashboard(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow_staff()
        self.ui.setupUi(self)

class Customer_Dashboard(QMainWindow):
    def __init__( self, email, parent=None ):
        super().__init__(parent)
        self.ui = Ui_MainWindow_customer()
        self.ui.setupUi(self)
        self.customer_data = get_customer_by_email(email)[1][0]
        self.ui.customerName.setText(self.customer_data[1])
        self.availableCars = get_available_cars()
        self.fillCarsTable()
        # print("Response:")
        # print(self.availableCars)
    def fillCarsTable(self):
        id=1
        for car in self.availableCars:
            self.tmpBrand = QLabel(self.ui.frame_6)
            self.tmpBrand.setText(car[1])
            self.ui.gridLayout.addWidget(self.tmpBrand, id, 0, 1, 1)
            self.tmpModel = QLabel(self.ui.frame_6)
            self.tmpModel.setText(car[0])
            self.ui.gridLayout.addWidget(self.tmpModel, id, 1, 1, 1)
            self.tmpYear = QLabel(self.ui.frame_6)
            self.tmpYear.setText(car[2])
            self.ui.gridLayout.addWidget(self.tmpYear, id, 2, 1, 1)
            self.tmpPrice = QLabel(self.ui.frame_6)
            self.tmpPrice.setText("$100")
            self.ui.gridLayout.addWidget(self.tmpPrice, id, 3, 1, 1)
            self.tmpBtn = rentCarBtn(car[1],car[0])
            self.tmpBtn.setText("Rent now!")
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.tmpBtn.sizePolicy().hasHeightForWidth())
            self.tmpBtn.setSizePolicy(sizePolicy)
            self.tmpBtn.setMinimumSize(QtCore.QSize(100, 30))
            self.tmpBtn.setStyleSheet("*{\n"
                                    "    background-color: #2596be;\n"
                                    "    border-radius: 10px;\n"
                                    "}\n")
            self.ui.gridLayout.addWidget(self.tmpBtn, id, 4, 1, 1)
            if id==5: break
            id+=1
        pass
    def on_startDate_select(self, date):    
        self.ui.startDateLabel.setText(date.toString("dd.MM.yyyy"))
    def on_endDate_select(self, date):
        self.ui.endDateLabel.setText(date.toString("dd.MM.yyyy"))
    def on_startDateBtn_pressed(self):
        self.calendar = QCalendarWidget()
        self.calendar.clicked.connect(self.on_startDate_select)
        self.calendar.clicked.connect(self.calendar.close)
        self.calendar.show()
    def on_endDateBtn_pressed(self):
        self.calendar = QCalendarWidget()
        self.calendar.clicked.connect(self.on_endDate_select)
        self.calendar.clicked.connect(self.calendar.close)
        self.calendar.show()
class LoginRegister(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form() 
        self.ui.setupUi(self)

    def on_staffLoginBtn_toggled(self, staffFlag):
        self.staffLoginFlag = staffFlag
        if staffFlag:
            self.ui.reg.hide()
            self.ui.widget_2.hide()
            self.ui.label.setText("STAFF LOGIN")
        else:
            self.ui.reg.show()
            self.ui.widget_2.show()
            self.ui.label.setText("LOGIN")
    def on_loginBtn_pressed(self):
        # TO DO: implement staff login based on the status of staffLoginFlag
        password = self.ui.lineEdit_2.text()
        email = self.ui.lineEdit.text()
        if(password != "" and email != ""):
            login_status = login(email, password)
            if login_status == 0:
                self.hide()
                self.window = Customer_Dashboard(email)
                self.window.show()
                self.ui.lineEdit_2.setText("")
                self.ui.lineEdit.setText("")
            else:
                print("Login failed!")
        else:
            print("No email or password!")

    def on_createAccountBtn_pressed(self):
        firstname = self.ui.lineEdit_7.text()
        lastname = self.ui.lineEdit_6.text()
        password = self.ui.lineEdit_4.text()
        email = self.ui.lineEdit_3.text()
        if((firstname!="")&(lastname!="")&(email!="")&(password!="")):
            register(firstname, lastname, email, password)
            dialogWindow = addressDialog()
            if dialogWindow.exec():
                [address1, address2, postal_code, city, country, phone_number] = dialogWindow.returnAddress()
                register_address(email, address1, address2, postal_code, city, country, phone_number)


if __name__== '__main__':
    app  = QApplication(sys.argv)
    windowL  = LoginRegister()
    windowL.show()
    app.exec()    