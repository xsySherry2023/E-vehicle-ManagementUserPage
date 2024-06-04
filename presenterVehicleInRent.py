# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 18:13:58 2022
Presenter of vehicle in rent page.
@author: Calvin 
"""
from PyQt5 import QtWidgets
from vehicleInRentPage import Ui_MainWindowVehicleInRent
import presenterCustomer
from customer import Customer
from Order import Order
import pandas as pd

class PresenterVehicleInRent():
    def __init__(self, window: QtWidgets.QMainWindow, customer: Customer, order: Order, cityLocations: pd.DataFrame):
        """
        Constructor of Presenter Vehicle in rent class 

        Parameters
        ----------
        window : QtWidgets.QMainWindow
            Main window to show page to user.
        customer : Customer
            current customer that is logged in.
        order : Order
            current order that is active.
        cityLocations : pd.DataFrame
            Data from all available city locations.

        Returns
        -------
        None.

        """
        self.uiVehicleInRent = Ui_MainWindowVehicleInRent()  # Create an instance ui class
        self.window = window
        self.uiVehicleInRent.setupUi(self.window)
        self.currentCustomer = customer
        self.currentOrder = order
        # omit this part of the code

