# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 11:31:23 2022

@author: ZHOU
"""
import sys
from PyQt5 import QtWidgets
from moveVehiclePage import Ui_MainWindowOperatorMoveVehicle
import presenterOperator
# import presenterRegistration
# this can be removed if system is connected
# sys.path.insert(1, 'C:/Users/Calvin Pfob/Documents/sqlKristen')
import mySQL as mySQL
from PyQt5 import QtCore, QtGui, QtWidgets


class presenterOperatorMoveVehicle():
    def __init__(self, window,operator):

        self.operator =operator
        self.uiOperatorMoveVehicle = Ui_MainWindowOperatorMoveVehicle() # Create an instance of our class
        # self.operator = operator
        self.uiOperatorMoveVehicle.setupUi(window)

        self.updatevehicle()
        self.updatecity()
        
        self.uiOperatorMoveVehicle.backButton.clicked.connect(lambda: presenterOperator.presenterOperator(window,operator))
        self.uiOperatorMoveVehicle.moveButton.clicked.connect(lambda: self.moveVehicle(window))
        # omit this part of the code
     
 