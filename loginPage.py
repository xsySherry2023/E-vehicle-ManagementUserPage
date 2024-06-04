# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowLogin(object):
    def setupUi(self, MainWindowLogin):
        MainWindowLogin.setObjectName("MainWindowLogin")
        MainWindowLogin.resize(977, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/Users/Calvin Pfob/Documents/guiDevelopment/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindowLogin.setWindowIcon(icon)
        MainWindowLogin.setIconSize(QtCore.QSize(25, 25))
        self.loginPage = QtWidgets.QWidget(MainWindowLogin)
        self.loginPage.setObjectName("loginPage")
        self.title = QtWidgets.QLabel(self.loginPage)
        self.title.setGeometry(QtCore.QRect(0, 10, 981, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.backgroundPicture = QtWidgets.QLabel(self.loginPage)
        self.backgroundPicture.setGeometry(QtCore.QRect(0, 0, 981, 481))
        self.backgroundPicture.setStyleSheet("background-image: url(:/login/tier-mobility-2021-05-min.png);")
        self.backgroundPicture.setText("")
        self.backgroundPicture.setPixmap(QtGui.QPixmap(":/login/tier-mobility-2021-05-min.png"))
        self.backgroundPicture.setScaledContents(True)
        self.backgroundPicture.setObjectName("backgroundPicture")
        self.logInButton = QtWidgets.QPushButton(self.loginPage)
        self.logInButton.setGeometry(QtCore.QRect(410, 360, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.logInButton.setFont(font)
        self.logInButton.setStyleSheet("background-color: rgba(85, 153, 255, 150); color: white")
        self.logInButton.setObjectName("logInButton")
        self.registerButton = QtWidgets.QPushButton(self.loginPage)
        self.registerButton.setGeometry(QtCore.QRect(410, 410, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.registerButton.setFont(font)
        self.registerButton.setStyleSheet("background-color: rgba(85, 153, 255, 150); color: white")
        self.registerButton.setObjectName("registerButton")
        self.usernameEntry = QtWidgets.QLineEdit(self.loginPage)
        self.usernameEntry.setGeometry(QtCore.QRect(360, 150, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.usernameEntry.setFont(font)
        self.usernameEntry.setText("")
        self.usernameEntry.setObjectName("usernameEntry")
        self.passwordEntry = QtWidgets.QLineEdit(self.loginPage)
        self.passwordEntry.setGeometry(QtCore.QRect(360, 230, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(True)
        self.passwordEntry.setFont(font)
        self.passwordEntry.setText("")
        self.passwordEntry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEntry.setObjectName("passwordEntry")
        self.usernameLabel = QtWidgets.QLabel(self.loginPage)
        self.usernameLabel.setGeometry(QtCore.QRect(270, 160, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setStyleSheet("color:rgb(255, 255, 255)")
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(self.loginPage)
        self.passwordLabel.setGeometry(QtCore.QRect(270, 240, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setStyleSheet("color:rgb(255, 255, 255)")
        self.passwordLabel.setObjectName("passwordLabel")
        self.backgroundFrame = QtWidgets.QFrame(self.loginPage)
        self.backgroundFrame.setGeometry(QtCore.QRect(0, 0, 981, 481))
        self.backgroundFrame.setStyleSheet("background:rgba(0, 0, 0, 50)")
        self.backgroundFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.backgroundFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.backgroundFrame.setObjectName("backgroundFrame")
        self.backgroundPicture.raise_()
        self.backgroundFrame.raise_()
        self.title.raise_()
        self.logInButton.raise_()
        self.registerButton.raise_()
        self.usernameEntry.raise_()
        self.passwordEntry.raise_()
        self.usernameLabel.raise_()
        self.passwordLabel.raise_()
        MainWindowLogin.setCentralWidget(self.loginPage)

        self.retranslateUi(MainWindowLogin)
        QtCore.QMetaObject.connectSlotsByName(MainWindowLogin)

    def retranslateUi(self, MainWindowLogin):
        _translate = QtCore.QCoreApplication.translate
        MainWindowLogin.setWindowTitle(_translate("MainWindowLogin", "E-Vehicle Share System"))
        self.title.setText(_translate("MainWindowLogin", "<html><head/><body><p><span style=\" font-size:36pt; color:#ffffff;\">Become part of changing mobility</span></p></body></html>"))
        self.logInButton.setText(_translate("MainWindowLogin", "Log-in"))
        self.registerButton.setText(_translate("MainWindowLogin", "Register"))
        self.usernameLabel.setText(_translate("MainWindowLogin", "Username:"))
        self.passwordLabel.setText(_translate("MainWindowLogin", "Password:"))

import bg_rc
