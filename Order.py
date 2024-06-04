# -*- coding: utf-8 -*-

import datetime
import mySQL
import pandas as pd
import numpy as np

class Order:
    """
    The order class contains the attributes:
        - orderId
        - vehicleId
        - userId
        - timeOrder
        - priceTotal
        - orderStatus
        - orderTimestamp
        - rentCityLocationId
        - returnCityLocationId
     and the methods:
         (- constructor)
         - returnVehicle
         - payOrder
    """

    orderId: int
    vehicleId: int
    # vehicleType could make sense here to add
    userId: int
    timeOrder: float
    priceTotal: float
    orderStatus: int
    orderTimestamp: str
    rentCityLocationId: int
    returnCityLocationId: int


  