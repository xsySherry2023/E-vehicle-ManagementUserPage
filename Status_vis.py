# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Status_vis.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets
import icon_rc


class Ui_WindowStatus_vis(object):
    def setupUi(self, WindowStatus_vis):
        WindowStatus_vis.setObjectName("WindowStatus_vis")
        WindowStatus_vis.resize(1019, 672)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WindowStatus_vis.setWindowIcon(icon)
        WindowStatus_vis.setIconSize(QtCore.QSize(25, 25))
        self.customerPage = QtWidgets.QWidget(WindowStatus_vis)
        self.customerPage.setObjectName("customerPage")
        self.backgroundFrame = QtWidgets.QFrame(self.customerPage)
        self.backgroundFrame.setGeometry(QtCore.QRect(0, 0, 1091, 681))
        self.backgroundFrame.setStyleSheet("background:rgba(0, 0, 0, 50)")
        self.backgroundFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.backgroundFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.backgroundFrame.setObjectName("backgroundFrame")
        self.layoutWidget = QtWidgets.QWidget(self.backgroundFrame)
        self.layoutWidget.setGeometry(QtCore.QRect(-90, -60, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.backgroundFrame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(-90, -60, 2, 2))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtWidgets.QWidget(self.backgroundFrame)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1022, 670))
        self.widget.setStyleSheet("\n"
"background-color: rgb(228, 250, 251);")
        self.widget.setObjectName("widget")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 191, 631))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(29, 40, 131, 101))
        self.frame_4.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(10, 10, 111, 81))
        self.frame_5.setStyleSheet("image: url(:/icon/icon.png);\n"
"background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.homelabel = QtWidgets.QLabel(self.frame)
        self.homelabel.setGeometry(QtCore.QRect(60, 280, 72, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(11)
        self.homelabel.setFont(font)
        self.homelabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.homelabel.setObjectName("homelabel")
        self.ReturnButton = QtWidgets.QPushButton(self.frame)
        self.ReturnButton.setGeometry(QtCore.QRect(50, 330, 91, 51))
        self.ReturnButton.setStyleSheet("image: url(:/icon/9022554_key_return_duotone_icon.png);\n"
"background-color: rgb(0, 170, 255);")
        self.ReturnButton.setText("")
        self.ReturnButton.setObjectName("ReturnButton")
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setGeometry(QtCore.QRect(30, 480, 141, 101))
        self.frame_9.setStyleSheet("background-color: rgba(85, 255, 255,50);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.frame_6 = QtWidgets.QFrame(self.frame_9)
        self.frame_6.setGeometry(QtCore.QRect(20, 20, 101, 61))
        self.frame_6.setStyleSheet("image: url(:/icon/crown.png);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.returnlabel = QtWidgets.QLabel(self.frame)
        self.returnlabel.setGeometry(QtCore.QRect(50, 390, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(11)
        self.returnlabel.setFont(font)
        self.returnlabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.returnlabel.setObjectName("returnlabel")
        self.homeButton = QtWidgets.QPushButton(self.frame)
        self.homeButton.setGeometry(QtCore.QRect(50, 220, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.homeButton.setFont(font)
        self.homeButton.setStyleSheet("image: url(:/icon/216242_home_icon.png);\n"
"background-color: rgb(0, 170, 255);\n"
"")
        self.homeButton.setText("")
        self.homeButton.setObjectName("homeButton")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setGeometry(QtCore.QRect(230, 20, 751, 111))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.title = QtWidgets.QLabel(self.frame_7)
        self.title.setGeometry(QtCore.QRect(30, 10, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(18)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.exitbutton = QtWidgets.QPushButton(self.frame_7)
        self.exitbutton.setGeometry(QtCore.QRect(620, 20, 51, 51))
        self.exitbutton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"image: url(:/icon/鸣人头像.jpg);")
        self.exitbutton.setText("")
        self.exitbutton.setObjectName("exitbutton")
        self.orderlabel = QtWidgets.QLabel(self.frame_7)
        self.orderlabel.setGeometry(QtCore.QRect(30, 10, 271, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.orderlabel.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        self.orderlabel.setFont(font)
        self.orderlabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.orderlabel.setObjectName("orderlabel")
        self.frame_17 = QtWidgets.QFrame(self.frame_7)
        self.frame_17.setGeometry(QtCore.QRect(320, 10, 91, 71))
        self.frame_17.setStyleSheet("image: url(:/icon/2376772_bike_bicycle_cycling_sport_icon.png);")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_4.addWidget(self.frame_7)
        self.frame_3 = QtWidgets.QFrame(self.widget)
        self.frame_3.setGeometry(QtCore.QRect(230, 130, 751, 521))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_3)
        self.scrollArea.setGeometry(QtCore.QRect(20, 10, 721, 501))
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 721, 501))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWebEngineWidgets.QWebEngineView(self.scrollAreaWidgetContents)

        self.widget_2.load(QtCore.QUrl("file:///image4.html"))

        self.widget_2.setStyleSheet("background-color: qconicalgradient(cx:0.5,cy:0.5,angle:90,stop:0 rgb(235, 252, 254),stop :1 rgb(184,233,234));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2.addWidget(self.widget_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_3 = QtWidgets.QWidget(self.backgroundFrame)
        self.layoutWidget_3.setGeometry(QtCore.QRect(-90, -60, 2, 2))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        WindowStatus_vis.setCentralWidget(self.customerPage)

        self.retranslateUi(WindowStatus_vis)
        QtCore.QMetaObject.connectSlotsByName(WindowStatus_vis)

    def retranslateUi(self, WindowStatus_vis):
        _translate = QtCore.QCoreApplication.translate
        WindowStatus_vis.setWindowTitle(_translate("WindowStatus_vis", "E-Vehicle Share System"))
        self.homelabel.setText(_translate("WindowStatus_vis", ">HOME<"))
        self.returnlabel.setText(_translate("WindowStatus_vis", ">RETURN<"))
        self.title.setText(_translate("WindowStatus_vis", "Data visualisation"))
        self.orderlabel.setText(_translate("WindowStatus_vis", "Proportion of vehicle  \n"
" status in each block"))

