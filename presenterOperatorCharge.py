# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 11:16:57 2022

@author: ZHOU
"""
import sys
from PyQt5 import QtWidgets
from chargeVehiclePage import Ui_MainWindowOperatorCharge
import presenterOperator
# import presenterRegistration
# this can be removed if system is connected
# sys.path.insert(1, 'C:/Users/Calvin Pfob/Documents/sqlKristen')
from mySQL import loadUsers

class presenterOperatorCharge():
    def __init__(self, window,operator):

        self.operator =operator
        self.uiLogIn = Ui_MainWindowOperatorCharge() # Create an instance of our class
        self.uiLogIn.setupUi(window)
        self.uiLogIn.backButton.clicked.connect(lambda: presenterOperator.presenterOperator(window,operator))   
        self.uiLogIn.chargeConfirmButton.clicked.connect(lambda: self.chargeAllVehicle())   
        # omit this part of the code
        
   