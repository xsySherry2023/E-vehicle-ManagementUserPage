# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 16:58:45 2022
Presenter Top Up Balance
@author: Calvin
"""
from PyQt5 import QtWidgets
from topUpBalancePage import Ui_MainWindowTopUpBalance
import presenterCustomer
from customer import Customer
from datetime import date


class PresenterTopUpBalance():
    def __init__(self, window: QtWidgets.QMainWindow, customer: Customer):
        """
        Constructor of PresenterTopUpBalacne class

        Parameters
        ----------
        window : QtWidgets.QMainWindow
            Main window for showing page to user.
        customer : Customer
            Current customer object that is logged in.

        Returns
        -------
        None.

        """
        self.uiTopUpBalance = Ui_MainWindowTopUpBalance()  # Create an instance of our class
        self.uiTopUpBalance.setupUi(window)
        self.currentCustomer = customer
        self.window = window
        self.uiTopUpBalance.goBackButton.clicked.connect(lambda: self.goBack())
        self.uiTopUpBalance.topUpButton.clicked.connect(lambda: self.topUpBalance())
        # set current Balance
        currentBalance = self.currentCustomer.userBalance
        self.uiTopUpBalance.currentBalanceOutput.setText("£‎" + str(currentBalance))
        # omit this part of the code
