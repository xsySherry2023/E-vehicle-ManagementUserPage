# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 15:14:22 2022
Presenter file of rent vehicle page
@author: Calvin 
"""
from PyQt5 import QtWidgets
from rentVehiclePage import Ui_MainWindowRentVehicle
import presenterVehicleInRent
import presenterCustomer
from customer import Customer
from mySQL import loadAllCityLocations, loadVehicles
import pandas as pd
from Order import Order


class PresenterRentVehicle():
    def __init__(self, window: QtWidgets.QMainWindow, customer: Customer):
        """
        Constructor of PresenterRentVehicle class

        Parameters
        ----------
        window : QtWidgets.QMainWindow
            Main window to visualize UI page to user.
        customer : Customer
            Object of customer that is currently logged in.

        Returns
        -------
        None.

        """
        self.uiRentVehicle = Ui_MainWindowRentVehicle()  # Create an instance ui class
        self.window = window
        self.uiRentVehicle.setupUi(self.window)
        self.currentCustomer = customer

         # omit this part of the code

