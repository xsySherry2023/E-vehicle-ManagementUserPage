# -*- coding: utf-8 -*-


import mySQL
import pandas as pd
from Vehicle import Vehicle
from user import User

class Operator(User):
    """
    The Operator class inherits of User class.

    The User class contains the inherited attributes:
        - userId
        - userName
        - userBalance
    and the methods:
        - trackVehicle
        - chargeVehicle
        - repairVehicle
        - moveVehicle
    """

    # omit this part of the code