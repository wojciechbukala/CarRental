from PyQt5 import QtCore, QtGui, QtWidgets
from controller import *
from rentalDetailsWindow import *

class rentCarBtn(QtWidgets.QPushButton):
    def __init__(self,brand, model, parent=None):
        super().__init__(parent)
        self.brand = brand
        self.model = model
        self.pressed.connect(self.on_rentCarBtn_pressed)

    def on_rentCarBtn_pressed(self):
        print("renting...")
        self.rentWindow = rentalDetailsWindow(self.brand, self.model)
        self.rentWindow.show()