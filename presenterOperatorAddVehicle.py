# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 20:52:08 2022

@author: ZHOU
"""
import sys
from PyQt5 import QtWidgets
from addVehiclePage import Ui_MainWindowOperatorAddVehicle
import presenterOperator
import mySQL as mySQL
# this can be removed if sy

class presenterOperatorAddVehicle():
    def __init__(self, window,operator):

        self.operator =operator
        self.uiOperatoraddVehicle = Ui_MainWindowOperatorAddVehicle() # Create an instance of our class
        self.uiOperatoraddVehicle.setupUi(window)
        self.updatecity()
        
        self.uiOperatoraddVehicle.backButton.clicked.connect(lambda: presenterOperator.presenterOperator(window,operator))
        self.uiOperatoraddVehicle.addButton.clicked.connect(lambda: self.addVehicle())
        # omit this part of the code
    
   