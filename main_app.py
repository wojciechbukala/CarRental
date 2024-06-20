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
import ast
from rentCarBtn import *
from rentalDetailsWindow import *

# class MainWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
        # self.ui.moreClientsBtn.clicked(lambda: moreClients())
class Staff_Dashboard(QMainWindow):
    def __init__(self, email, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.customers = get_all_customers()
        self.rentals = get_all_rentals()
    #     self.fillRentalTables()
    # def fillRentalTables(self):
    #     self.addCusomer(car, row)
    #     self.addModel(car, row)
    #     self.addYear(car, row)
    #     self.addPrice(car, row)
    #     self.addRentBtn(car, row)

class Customer_Dashboard(QMainWindow):
    def __init__( self, email, parent=None ):
        super().__init__(parent)
        self.ui = Ui_MainWindow_customer()
        self.ui.setupUi(self)
        self.ui.leftMenu.hide()
        self.ui.profileMenu.hide()
        self.customer_data = get_customer_by_email(email)[1][0]
        self.ui.customer_name.setText(self.customer_data[1])
        self.availableCars = get_available_cars()
        self.fillCarsTable()
        self.ui.searchInput.setPlaceholderText("brand: desired_brand, model: desired_model, segment: desired_segment")
        # print("Response:")
        # print(self.availableCars)
    def fillCarsTable(self):
        id=1
        for car in self.availableCars:
            self.createNewRentOffer(car, id)
            if id==5: break
            id+=1

    def createNewRentOffer(self, car, row):
        self.addBrand(car, row)
        self.addModel(car, row)
        self.addYear(car, row)
        self.addPrice(car, row)
        self.addRentBtn(car, row)

    def addBrand(self, car, row):
        self.tmpBrand = QLabel(self.ui.frame_6)
        self.tmpBrand.setText(car[1])
        self.ui.gridLayout.addWidget(self.tmpBrand, row, 0, 1, 1)

    def addModel(self, car, row): 
        self.tmpModel = QLabel(self.ui.frame_6)
        self.tmpModel.setText(car[2])
        self.ui.gridLayout.addWidget(self.tmpModel, row, 1, 1, 1)

    def addYear(self, car, row):
        self.tmpYear = QLabel(self.ui.frame_6)
        year = car[3].split(" ")[3]
        self.tmpYear.setText(year)
        self.ui.gridLayout.addWidget(self.tmpYear, row, 2, 1, 1)

    def addPrice(self, car, row):
        self.tmpPrice = QLabel(self.ui.frame_6)
        self.tmpPrice.setText("$100")
        self.ui.gridLayout.addWidget(self.tmpPrice, row, 3, 1, 1)

    def addRentBtn(self, car, row):
        self.tmpBtn = rentCarBtn(car[1],car[0])
        self.tmpBtn.setText("Rent now!")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tmpBtn.sizePolicy().hasHeightForWidth())
        self.tmpBtn.setSizePolicy(sizePolicy)
        self.tmpBtn.setMinimumSize(QtCore.QSize(100, 30))
        self.tmpBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tmpBtn.setStyleSheet("*{\n"
                                    "    background-color: #2596be;\n"
                                    "    border-radius: 10px;\n"
                                    "}\n")
        self.ui.gridLayout.addWidget(self.tmpBtn, row, 4, 1, 1)
        
    def on_startDate_select(self, date):    
        self.ui.startDateLabel.setText(date.toString('dd-MM-yyyy'))
    def on_endDate_select(self, date):
        self.ui.endDateLabel.setText(date.toString('dd-MM-yyyy'))

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
    
    def on_searchBtn_pressed(self):
        keys = ["segment", "brand", "model"]
        searchInput = self.ui.searchInput.text()
        print(f'search input: {searchInput}')
        startDate = self.ui.startDateLabel.text()
        endDate = self.ui.endDateLabel.text()
        searchDict = self.parse(searchInput)
        for key in keys:
            if key not in searchDict:
                searchDict[key] = None
        self.availableCars = get_available_cars(startDate, endDate, searchDict["segment"], searchDict["brand"], searchDict["model"])


    def on_menuBtn_pressed(self):
        if(self.ui.leftMenu.isVisible()):
            self.ui.leftMenu.hide()
        else:
            self.ui.leftMenu.show()
    def on_accountBtn_pressed(self):
        if(self.ui.profileMenu.isVisible()):
            self.ui.profileMenu.hide()
        else:
            self.ui.profileMenu.show()

    def parse(self, searchInput):
        searchInput = "segment: B, brand: toyota, model: auris"
        pairs = searchInput.split(",")
        dict = {}
        for pair in pairs:
            key,val = pair.split(":")
            key = key.strip()
            val = val.strip()
            dict[key] = val
        return dict

class LoginRegister(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form() 
        self.ui.setupUi(self)
        self.staffLoginFlag = False

    def on_staffLoginBtn_toggled(self, staffFlag):
        self.staffLoginFlag = staffFlag
        if staffFlag:
            self.ui.reg.hide()
            self.ui.widget_2.hide()
            self.ui.lineEdit_2.hide()
            self.ui.label_8.hide()
            self.ui.label.setText("STAFF LOGIN")
            self.ui.loginBtn.clicked.connect(self.on_loginBtn_pressed_staff)
            
        else:
            self.ui.reg.show()
            self.ui.widget_2.show()
            self.ui.lineEdit_2.show()
            self.ui.label_8.show()
            self.ui.label.setText("LOGIN")
            self.ui.loginBtn.clicked.connect(self.on_loginBtn_pressed)
            self.ui.loginBtn.clicked.disconnect(self.on_loginBtn_pressed_staff)
    def on_loginBtn_pressed_staff(self):
        email = self.ui.lineEdit.text()
        if(email != ""):
            login_status = login_staff(email)
            if login_status == 0:
                self.hide()
                self.window = Staff_Dashboard(email)
                self.window.show()
                self.ui.lineEdit_2.setText("")
                self.ui.lineEdit.setText("")
            else:
                print("Login failed!")
                pass
        else:
            print("No email or password!")
    def on_loginBtn_pressed(self):
        password = self.ui.lineEdit_2.text()
        email = self.ui.lineEdit.text()
        if(password != "" and email != "" and not self.staffLoginFlag):
            login_status = login(email, password)
            if login_status == 0:
                self.hide()
                self.window = Customer_Dashboard(email)
                self.window.show()
                self.ui.lineEdit_2.setText("")
                self.ui.lineEdit.setText("")
            else:
                print("Login failed!")

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