# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 15:59:57 2022
Presenter file of customer page
@author: Calvin
"""
from PyQt5 import QtWidgets
from customerPage import Ui_MainWindowCustomer
import presenterLogin
from customer import Customer
import presenterTopUpBalance
import presenterRentVehicle


class PresenterCustomer():
    def __init__(self, window: QtWidgets.QMainWindow, customer: Customer):
        """
        Constructor of PresenterCustomer class

        Parameters
        ----------
        window : QtWidgets.QMainWindow
            Main Window to visualise UI to user.
        customer : Customer
            Object of current signed in customer.

        Returns
        -------
        None.

        """
        self.uiCustomer = Ui_MainWindowCustomer() # Create an instance of our class
        self.uiCustomer.setupUi(window)
        self.currentCustomer = customer
        self.window = window
        self.uiCustomer.rentVehicleButton.clicked.connect(lambda: self.rentVehicle())
        self.uiCustomer.signOutButton.clicked.connect(lambda: self.signOut())
        self.uiCustomer.topUpBalanceButton.clicked.connect(lambda: self.topUpBalance())

    