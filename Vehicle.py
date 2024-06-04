import pymysql
import pandas as pd

import mySQL


class Vehicle():

     """
     The Vehicle class contains the attributes:
        - vehicleType
        - vehicleId
        - vechicleStatus
        - batterySoc
        - drivenMinutes
        
     and the methods:
         (- constructor)
         - reduceBattery
         - defectVehicle
         - repairVehicle
         - chargeVehicle
         - changeLocation
    """
     vehicleTypeId: int
     vehicleId: int
     batterySoc: float
     # drivenMinutes: float
     cityLocationId: int
     vehicleStatus: int
     pricePerMin: float


     def __init__(self, vehicleId: int):
         #get the data from SQL database for specific vehicleId
         # Dummy data
         '''self.databaseConnection = databaseConnection
         self.vehicleType = vehicleType
         self.vehicleId = vehicleId
         self.vehicleStatus = vehicleStatus
         self.pricePerMinute = 0.5
         self.batterySoc = batterySoc
         self.drivenMinutes = drivenMinutes
         self.citylocationId = cityLocationId
         '''


         if vehicleId is not None :

             # query data from sql database for existing order in database
             vehiclesDF = mySQL.loadVehicles()
             vehiclesDF2 = vehiclesDF[vehiclesDF["vehicleID"] == vehicleId]
             print(vehiclesDF2)
             if vehiclesDF2.empty:
                 raise ValueError("Not found the vehicle")
             else :
                 vehiclesDF2.set_index('vehicleID', inplace=True)
                 # print(vehiclesDF2)
                 self.vehicleId =vehicleId
                 self.pricePerMin = vehiclesDF2.loc[vehicleId, 'pricePerMin']
                 self.vehicleTypeId = vehiclesDF2.loc[vehicleId, 'vehicleTypeId']
                   #self.vehicleId = vehiclesDF2.loc[vehicleId, 'vehicleId']
                 self.vehicleStatus = vehiclesDF2.loc[vehicleId, 'vehicleStatus']
                 self.batterySoc = vehiclesDF2.loc[vehicleId, 'batterySoc']
                 self.cityLocationId  = vehiclesDF2.loc[vehicleId, 'cityLocationId']
                 
                 #self.drivenMinutes = vehiclesDF2.loc[vehicleId, 'deivenMinutes']


# omit this part of the code