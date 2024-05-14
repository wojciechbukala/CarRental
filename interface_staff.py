# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_staff(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(963, 595)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("*{\n"
"    color: #000;\n"
"    border: none;\n"
"}\n"
"\n"
"#leftMenu{\n"
"    background-color: #2596be;\n"
"}\n"
"#mainBody{    \n"
"    background-color: #747474;\n"
"}\n"
"QLineEdit{\n"
"    background: transparent;\n"
"}\n"
"#searchFrame{\n"
"    border-radius: 10px;\n"
"    border: 2px solid #212121;\n"
"}\n"
"#appHeader{\n"
"}\n"
"#card1, #card2, #card3, #card4{\n"
"    background-color: #A0A0A0;\n"
"    border-radius: 20px;\n"
"}\n"
"#viewMoreBtn{\n"
"    background-color: #2596be;\n"
"    border-radius: 10px;\n"
"}\n"
"#menuBtn{\n"
"    background-color: #2596be;\n"
"    border-radius: 10px;\n"
"}\n"
"#widget_4{\n"
"    background-color: #A0A0A0;\n"
"    border-radius: 20px;\n"
"}\n"
"#widget_5{\n"
"    background-color: #A0A0A0;\n"
"    border-radius: 20px;\n"
"}\n"
"#moreClientsBtn{\n"
"    background-color: #2596be;\n"
"    border-radius: 10px;\n"
"}\n"
"#accountBtn{\n"
"    background-color: #2596be;\n"
"    border-radius: 10px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftMenu = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenu.sizePolicy().hasHeightForWidth())
        self.leftMenu.setSizePolicy(sizePolicy)
        self.leftMenu.setObjectName("leftMenu")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.leftMenu)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_9 = QtWidgets.QFrame(self.leftMenu)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_8 = QtWidgets.QFrame(self.frame_9)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_33 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_14.addWidget(self.label_33, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.verticalLayout_10.addWidget(self.frame_8)
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_11.setSpacing(30)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_10)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_11.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_10)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/icons/database.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon1)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_11.addWidget(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_10)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/icons/code.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon2)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_11.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_10)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/icons/info.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon3)
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_11.addWidget(self.pushButton_14)
        self.verticalLayout_10.addWidget(self.frame_10, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_9.addWidget(self.frame_9, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.leftMenu)
        self.mainBody = QtWidgets.QWidget(self.centralwidget)
        self.mainBody.setObjectName("mainBody")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainBody)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerFrame = QtWidgets.QWidget(self.mainBody)
        self.headerFrame.setObjectName("headerFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.headerFrame)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.menuBtn = QtWidgets.QPushButton(self.widget)
        self.menuBtn.setMinimumSize(QtCore.QSize(40, 40))
        self.menuBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("assets/icons/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuBtn.setIcon(icon4)
        self.menuBtn.setIconSize(QtCore.QSize(32, 32))
        self.menuBtn.setObjectName("menuBtn")
        self.horizontalLayout_3.addWidget(self.menuBtn, 0, QtCore.Qt.AlignLeft)
        self.appHeader = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.appHeader.setFont(font)
        self.appHeader.setObjectName("appHeader")
        self.horizontalLayout_3.addWidget(self.appHeader, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.widget, 0, QtCore.Qt.AlignLeft)
        self.widget_2 = QtWidgets.QWidget(self.headerFrame)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.searchFrame = QtWidgets.QFrame(self.widget_2)
        self.searchFrame.setMinimumSize(QtCore.QSize(160, 40))
        self.searchFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searchFrame.setObjectName("searchFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.searchFrame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.searchFrame)
        self.label_2.setMinimumSize(QtCore.QSize(30, 30))
        self.label_2.setMaximumSize(QtCore.QSize(30, 30))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("assets/icons/search.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.searchFrame)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.horizontalLayout_4.addWidget(self.searchFrame, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.widget_2, 0, QtCore.Qt.AlignHCenter)
        self.widget_3 = QtWidgets.QWidget(self.headerFrame)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.accountBtn = QtWidgets.QPushButton(self.widget_3)
        self.accountBtn.setMinimumSize(QtCore.QSize(40, 40))
        self.accountBtn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("assets/icons/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.accountBtn.setIcon(icon5)
        self.accountBtn.setIconSize(QtCore.QSize(32, 32))
        self.accountBtn.setObjectName("accountBtn")
        self.horizontalLayout_6.addWidget(self.accountBtn)
        self.horizontalLayout_2.addWidget(self.widget_3, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.headerFrame, 0, QtCore.Qt.AlignTop)
        self.cardsFrame = QtWidgets.QWidget(self.mainBody)
        self.cardsFrame.setObjectName("cardsFrame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.cardsFrame)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.card1 = QtWidgets.QFrame(self.cardsFrame)
        self.card1.setMinimumSize(QtCore.QSize(160, 0))
        self.card1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card1.setObjectName("card1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.card1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.card1)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(40, 40))
        self.label.setMaximumSize(QtCore.QSize(40, 40))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("assets/icons/shopping-cart.svg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignTop)
        self.label_3 = QtWidgets.QLabel(self.card1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_7.addWidget(self.card1)
        self.card3 = QtWidgets.QFrame(self.cardsFrame)
        self.card3.setMinimumSize(QtCore.QSize(160, 0))
        self.card3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card3.setObjectName("card3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.card3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.card3)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setMinimumSize(QtCore.QSize(40, 40))
        self.label_10.setMaximumSize(QtCore.QSize(40, 40))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("assets/icons/credit-card.svg"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.label_8 = QtWidgets.QLabel(self.card3)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_7.addWidget(self.card3)
        self.card2 = QtWidgets.QFrame(self.cardsFrame)
        self.card2.setMinimumSize(QtCore.QSize(160, 0))
        self.card2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card2.setObjectName("card2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.card2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.card2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setMinimumSize(QtCore.QSize(40, 40))
        self.label_7.setMaximumSize(QtCore.QSize(40, 40))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("assets/icons/align-left.svg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.label_5 = QtWidgets.QLabel(self.card2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_7.addWidget(self.card2)
        self.card4 = QtWidgets.QFrame(self.cardsFrame)
        self.card4.setMinimumSize(QtCore.QSize(160, 0))
        self.card4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card4.setObjectName("card4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.card4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.card4)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_11.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.frame_4)
        self.label_13.setMinimumSize(QtCore.QSize(40, 40))
        self.label_13.setMaximumSize(QtCore.QSize(40, 40))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("assets/icons/users.svg"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_11.addWidget(self.label_13)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.label_11 = QtWidgets.QLabel(self.card4)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_7.addWidget(self.card4)
        self.verticalLayout.addWidget(self.cardsFrame)
        self.mainFrame = QtWidgets.QWidget(self.mainBody)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setObjectName("mainFrame")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.mainFrame)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.widget_4 = QtWidgets.QWidget(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_5 = QtWidgets.QFrame(self.widget_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setContentsMargins(11, -1, -1, -1)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_14 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_13.addWidget(self.label_14, 0, QtCore.Qt.AlignLeft)
        self.viewMoreBtn = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewMoreBtn.sizePolicy().hasHeightForWidth())
        self.viewMoreBtn.setSizePolicy(sizePolicy)
        self.viewMoreBtn.setMinimumSize(QtCore.QSize(100, 0))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("assets/icons/arrow-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewMoreBtn.setIcon(icon6)
        self.viewMoreBtn.setIconSize(QtCore.QSize(24, 24))
        self.viewMoreBtn.setObjectName("viewMoreBtn")
        self.horizontalLayout_13.addWidget(self.viewMoreBtn, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_6.addWidget(self.frame_5, 0, QtCore.Qt.AlignTop)
        self.frame_6 = QtWidgets.QFrame(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout.setContentsMargins(11, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.label_17 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.frame_6)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 1, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 0, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.frame_6)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 2, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.frame_6)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 1, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.frame_6)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 2, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.frame_6)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 2, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.frame_6)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 1, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.frame_6)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 3, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.frame_6)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 3, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.frame_6)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 3, 2, 1, 1)
        self.verticalLayout_6.addWidget(self.frame_6, 0, QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout_12.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.mainFrame)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setContentsMargins(9, 6, 9, 6)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_27 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_7.addWidget(self.label_27, 0, QtCore.Qt.AlignTop)
        self.frame_7 = QtWidgets.QFrame(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_6 = QtWidgets.QWidget(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_15.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout_15.setSpacing(3)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_28 = QtWidgets.QLabel(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_15.addWidget(self.label_28)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_2.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_2.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_2.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("assets/icons/at-sign.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon7)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_15.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignLeft)
        self.pushButton = QtWidgets.QPushButton(self.widget_6)
        self.pushButton.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("assets/icons/map-pin.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon8)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_15.addWidget(self.pushButton, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_8.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.frame_7)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_16.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout_16.setSpacing(3)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_29 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_16.addWidget(self.label_29)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_3.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_3.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon7)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_16.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_4.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_4.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon8)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_16.addWidget(self.pushButton_4)
        self.verticalLayout_8.addWidget(self.widget_7)
        self.widget_10 = QtWidgets.QWidget(self.frame_7)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_19.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout_19.setSpacing(3)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_32 = QtWidgets.QLabel(self.widget_10)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_19.addWidget(self.label_32)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_10)
        self.pushButton_9.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_9.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_9.setText("")
        self.pushButton_9.setIcon(icon7)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_19.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_10)
        self.pushButton_10.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_10.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_10.setText("")
        self.pushButton_10.setIcon(icon8)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_19.addWidget(self.pushButton_10)
        self.verticalLayout_8.addWidget(self.widget_10)
        self.widget_9 = QtWidgets.QWidget(self.frame_7)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_18.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout_18.setSpacing(3)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_31 = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_18.addWidget(self.label_31)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_7.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_7.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_7.setText("")
        self.pushButton_7.setIcon(icon7)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_18.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_8.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_8.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_8.setText("")
        self.pushButton_8.setIcon(icon8)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_18.addWidget(self.pushButton_8)
        self.verticalLayout_8.addWidget(self.widget_9)
        self.widget_8 = QtWidgets.QWidget(self.frame_7)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_17.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout_17.setSpacing(3)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_30 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_17.addWidget(self.label_30)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_5.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_5.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_5.setText("")
        self.pushButton_5.setIcon(icon7)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_17.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_6.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_6.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_6.setText("")
        self.pushButton_6.setIcon(icon8)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_17.addWidget(self.pushButton_6)
        self.verticalLayout_8.addWidget(self.widget_8)
        self.verticalLayout_7.addWidget(self.frame_7)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.moreClientsBtn = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.moreClientsBtn.sizePolicy().hasHeightForWidth())
        self.moreClientsBtn.setSizePolicy(sizePolicy)
        self.moreClientsBtn.setIcon(icon6)
        self.moreClientsBtn.setIconSize(QtCore.QSize(24, 24))
        self.moreClientsBtn.setObjectName("moreClientsBtn")
        self.verticalLayout_7.addWidget(self.moreClientsBtn)
        self.horizontalLayout_12.addWidget(self.widget_5, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout.addWidget(self.mainFrame)
        self.horizontalLayout.addWidget(self.mainBody)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_33.setText(_translate("MainWindow", "Car Rental"))
        self.pushButton_11.setText(_translate("MainWindow", "Home"))
        self.pushButton_12.setText(_translate("MainWindow", "Data Base"))
        self.pushButton_13.setText(_translate("MainWindow", "Repository"))
        self.pushButton_14.setText(_translate("MainWindow", "About Us"))
        self.appHeader.setText(_translate("MainWindow", "Dashbaord"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Search..."))
        self.label_4.setText(_translate("MainWindow", "2.000.000"))
        self.label_3.setText(_translate("MainWindow", "USD"))
        self.label_9.setText(_translate("MainWindow", "+30"))
        self.label_8.setText(_translate("MainWindow", "Stock"))
        self.label_6.setText(_translate("MainWindow", "58"))
        self.label_5.setText(_translate("MainWindow", "Rents"))
        self.label_12.setText(_translate("MainWindow", "20k"))
        self.label_11.setText(_translate("MainWindow", "Clients"))
        self.label_14.setText(_translate("MainWindow", "Latest Products"))
        self.viewMoreBtn.setText(_translate("MainWindow", "View More"))
        self.label_17.setText(_translate("MainWindow", "Price"))
        self.label_20.setText(_translate("MainWindow", "Warszawa"))
        self.label_16.setText(_translate("MainWindow", "Store"))
        self.label_21.setText(_translate("MainWindow", "Silnik"))
        self.label_19.setText(_translate("MainWindow", "$10"))
        self.label_22.setText(_translate("MainWindow", "$20"))
        self.label_23.setText(_translate("MainWindow", "Poznań"))
        self.label_15.setText(_translate("MainWindow", "Product"))
        self.label_18.setText(_translate("MainWindow", "Żuk"))
        self.label_24.setText(_translate("MainWindow", "Autobus"))
        self.label_25.setText(_translate("MainWindow", "$30"))
        self.label_26.setText(_translate("MainWindow", "Wrocław"))
        self.label_27.setText(_translate("MainWindow", "Client contacts"))
        self.label_28.setText(_translate("MainWindow", "Ania"))
        self.label_29.setText(_translate("MainWindow", "Kasia"))
        self.label_32.setText(_translate("MainWindow", "Paweł"))
        self.label_31.setText(_translate("MainWindow", "Ania"))
        self.label_30.setText(_translate("MainWindow", "Ania"))
        self.moreClientsBtn.setText(_translate("MainWindow", "More Clients"))
