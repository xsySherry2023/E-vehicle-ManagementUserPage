# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 17:35:52 2022

@author: ZHOU
"""
import sys
from PyQt5 import QtWidgets
from trackVehiclePage import Ui_MainWindowOperatorTrackVehicle
import presenterOperator
import mySQL as mySQL
# this can be removed if system is connected
# sys.path.insert(1, 'C:/Users/Calvin Pfob/Documents/sqlKristen')
#import presenterLogin


class presenterTrackVehicle():
    def __init__(self, window,operator):
        """
        Constructor of presenterTrackVehicle class.

        Parameters
        ----------
        window : QtWidgets.QMainWindow
            Main Window to visualize page in UI.
        operator : Operator
           Object of operator that is currently logged in.

        Returns
        -------
        None.

        """
        self.operator =operator
        self.uiOperatorTrackVehcile = Ui_MainWindowOperatorTrackVehicle()
        
        self.uiOperatorTrackVehcile.setupUi(window)
        self.updatevehicle()
        self.updatecity()
        # self.uiOperatorTrackVehcile.retranslateUi(window)
        self.uiOperatorTrackVehcile.backButton.clicked.connect(lambda: presenterOperator.presenterOperator(window,operator))
        self.uiOperatorTrackVehcile.trackButton.clicked.connect(lambda: self.updatetxt())
        # omit this part of the code
    