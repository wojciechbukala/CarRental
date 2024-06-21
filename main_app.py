from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from endpoints import *
from interface_customer import *
from interface_staff import *
from logreg import *
from email_window import *
import sys
from search_result import *
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
        self.icon9 = QtGui.QIcon()
        self.icon9.addPixmap(QtGui.QPixmap("./assets/icons/at-sign.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon10 = QtGui.QIcon()
        self.icon10.addPixmap(QtGui.QPixmap("./ui/assets/icons/map-pin.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fillCustomerTable()
        self.fillRentalTables()

    def fillCustomerTable(self):
        for customer in self.customers:
            self.addCustomerToList(customer)

    def showEmail(self, email, customer):
        window = emailDialog(email, customer)
        window.exec()

    def addCustomerToList(self, customer):
        self.ui.widget_10 = QtWidgets.QWidget(self.ui.frame_7)
        self.ui.widget_10.setObjectName(f'{customer[1]}_widget')
        self.ui.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.ui.widget_10)
        self.ui.horizontalLayout_19.setContentsMargins(6, 0, 6, 0)
        self.ui.horizontalLayout_19.setSpacing(3)
        self.ui.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.ui.label_32 = QtWidgets.QLabel(self.ui.widget_10)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ui.label_32.setFont(font)
        self.ui.label_32.setObjectName(f'{customer[1]}_label')
        self.ui.label_32.setText(customer[0])
        self.ui.horizontalLayout_19.addWidget(self.ui.label_32)
        self.ui.pushButton_9 = QtWidgets.QPushButton(self.ui.widget_10)
        self.ui.pushButton_9.setMinimumSize(QtCore.QSize(25, 25))
        self.ui.pushButton_9.setMaximumSize(QtCore.QSize(25, 25))
        self.ui.pushButton_9.setText("")
        self.ui.pushButton_9.setIcon(self.icon9)
        self.ui.pushButton_9.setObjectName(f'{customer[1]}_email')
        self.ui.pushButton_9.clicked.connect(lambda: self.showEmail(customer[2], customer[0]))
        self.ui.horizontalLayout_19.addWidget(self.ui.pushButton_9)

    def fillRentalTables(self):
        id=1
        for rental in self.rentals:
            print(rental)
            self.createNewRentalInfo(rental, id)
            id+=1
    
    def createNewRentalInfo(self, rental, row):
        self.addCustomer(rental, row)
        self.addRentalPeriod(rental, row)
        self.addCar(rental, row)
        self.addInsurance(rental, row)
        self.addDiagnostics(rental, row)
        self.addCancelBtn(rental, row)

    def addCustomer(self, rental, row):
        self.tmpCustomer = QLabel(self.ui.frame_6)
        tmpCustomerID = rental[7] + ' ' + rental[8]
        print(tmpCustomerID)
        self.tmpCustomer.setText(tmpCustomerID)
        self.ui.gridLayout.addWidget(self.tmpCustomer, row, 0, 1, 1)


    def addCar(self, rental, row):
        self.tmpCar = QLabel(self.ui.frame_6)
        tmpCarID = rental[4] +' '+ rental[5]
        self.tmpCar.setText(tmpCarID)
        self.ui.gridLayout.addWidget(self.tmpCar, row, 1, 1, 1)
 
    def addRentalPeriod(self, rental, row):
        self.tmpDate = QLabel(self.ui.frame_6)
        dateStart = rental[1]
        dateStartTmp = dateStart.split(" ")
        dateStart = dateStartTmp[1]+'-'+dateStartTmp[2]+'-'+dateStartTmp[3]
        dateEnd = rental[2]
        dateEndTmp = dateEnd.split(" ")
        dateEnd = dateEndTmp[1]+'-'+dateEndTmp[2]+'-'+dateEndTmp[3]        
        dateLabel = dateStart+'->'+dateEnd
        self.tmpDate.setText(dateLabel)
        self.ui.gridLayout.addWidget(self.tmpDate, row, 2, 1, 1)

    def on_tmpInsurance_checkStateChanged(self, state, rental):
        print(state)
        if state == QtCore.Qt.CheckState.Checked:
            flag_insurance(True, rental[3])
        elif state == QtCore.Qt.CheckState.Unchecked:
            flag_insurance(False, rental[3])


    def addInsurance(self, rental, row):
        self.tmpInsurance = QCheckBox(self.ui.frame_6)
        car = get_cars_by_id(rental[0])
        tmpInsuranceVal = car[0][5]
        if tmpInsuranceVal:
            self.tmpInsurance.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.tmpInsurance.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.tmpInsurance.stateChanged.connect(lambda: self.on_tmpInsurance_checkStateChanged(self.tmpInsurance.checkState(), rental))
        self.ui.gridLayout.addWidget(self.tmpInsurance, row, 3, 1, 1)
    
    def on_tmpDiagnostics_checkStateChanged(self, state, rental):
        if state == QtCore.Qt.CheckState.Checked:
            flag_diagnostics(True, rental[3])
        elif state == QtCore.Qt.CheckState.Unchecked:
            flag_diagnostics(False, rental[3])

    def addDiagnostics(self, rental, row):
        self.tmpDiagnostics = QCheckBox(self.ui.frame_6)
        car = get_cars_by_id(rental[0])
        tmpDiagnosticsVal = car[0][6]
        if tmpDiagnosticsVal:
            self.tmpDiagnostics.setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.tmpDiagnostics.setCheckState(QtCore.Qt.CheckState.Unchecked)  
        self.tmpDiagnostics.stateChanged.connect(lambda: self.on_tmpDiagnostics_checkStateChanged(self.tmpDiagnostics.checkState(), rental))
        self.ui.gridLayout.addWidget(self.tmpDiagnostics, row, 4, 1, 1)

    def addCancelBtn(self,rental, row):
        self.ui.pushButton_15 = QtWidgets.QPushButton(self.ui.frame_6)
        self.ui.pushButton_15.setText("Cancel rental")
        self.ui.pushButton_15.setObjectName("pushButton_15")
        self.ui.pushButton_15.clicked.connect(lambda: self.cancelRent(rental[3]))
        self.ui.gridLayout.addWidget(self.ui.pushButton_15, row, 5, 1, 1)

    def cancelRent(self, id):
        print("pressed!")
        return_a_car_transaction(id)
        self.fillRentalTables()

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
        self.tmpBrand.setText(car[2])
        self.ui.gridLayout.addWidget(self.tmpBrand, row, 0, 1, 1)

    def addModel(self, car, row): 
        self.tmpModel = QLabel(self.ui.frame_6)
        self.tmpModel.setText(car[1])
        self.ui.gridLayout.addWidget(self.tmpModel, row, 1, 1, 1)

    def addYear(self, car, row):
        self.tmpYear = QLabel(self.ui.frame_6)
        year = car[3].split(" ")[3]
        self.tmpYear.setText(year)
        self.ui.gridLayout.addWidget(self.tmpYear, row, 2, 1, 1)

    def addPrice(self, car, row):
        self.tmpPrice = QLabel(self.ui.frame_6)
        price = car[4]
        self.tmpPrice.setText(str(price)+' zł/h')
        self.ui.gridLayout.addWidget(self.tmpPrice, row, 3, 1, 1)

    def addRentBtn(self, car, row):
        self.tmpBtn = rentCarBtn(car[2],car[1])
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
        self.ui.startDateLabel.setText(date.toString('yyyy-MM-dd'))
    def on_endDate_select(self, date):
        self.ui.endDateLabel.setText(date.toString("yyyy-MM-dd"))

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
        startDate = self.ui.startDateLabel.text()
        endDate = self.ui.endDateLabel.text()
        searchDict = self.parse(searchInput)
        for key in keys:
            if key not in searchDict:
                searchDict[key] = None
        self.availableCars = get_available_cars(startDate, endDate, searchDict["segment"], searchDict["brand"], searchDict["model"])
        self.createSearchResultWindow(self.availableCars)

    def createSearchResultWindow(self, foundCars):
        self.window = SearchResults()
        i = 0
        for car in foundCars:
            self.window.addResult(car, i)
            i += 1
        self.window.show()


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
        pairs = searchInput.split(",")
        dict = {}
        for pair in pairs:
            if pair != '':
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