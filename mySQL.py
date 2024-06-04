#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 14:59:11 2022.
    
"""


# load MySQL, Pandas, Numpy libraries
import pymysql
import pandas as pd
import datetime


class MySql:
    def __init__(self, host, port, user, password, database):

        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.cursor = self.__Connection()

    def __Connection(self):
        """
        Get info of connection.

        Returns
        -------
        db.cursor()

        """
        if not self.database:
            raise(NameError, "There isn't such a database")
        self.db = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            charset='utf8')
        cursor = self.db.cursor()
        if not cursor:
            raise(NameError, "Connect Failed")
        else:
            print("Connect successful")
            return cursor

    def Query(self, sql):
        """
        Execute the query statement.

        Parameters
        ----------
        sql : STR
            The query statement need to execute
            Eg: SELECT * FROM users

        Returns
        -------
        list includes all the results after execution

        """
        # connect the database
        #cursor = self.__Connection()
        # execute the sql
        self.cursor.execute(sql)
        # store all the returning results into res
        records = self.cursor.fetchall()

        reList = []
        # convert every record(row) into list
        for record in records:
            reList.append(list(record))
        # close connection
        # self.db.close()
        return reList

    def NonQuery(self, sql):
        """
        Execute INSERT, DELETE, UPDATE statement.

        Parameters
        ----------
        sql : STR
        the query statement need to execute
        Eg: INSERT INTO tableName VALUES("xxxx")

        Returns
        -------
        None.

        """
        #cursor = self.__Connection()
        self.cursor.execute(sql)
        # if there is any alteration, you must commit the operation before close
        self.db.commit()
        # self.db.close()




# connect the database
db = MySql(host='localhost', port=3306, user='root', password='Xsyseven1', database='E_vehicle')



def loadUsers():
    """
    Load whole table of users.
    Direcly call it

    Returns
    -------
    result1 : dataFrame
        This dataframe contains the whole table of users.

    """
    # SQL query statement:load user data
    sql = 'SELECT userId,userName, userPassword, ut.userTypeName,balance FROM users u JOIN userTypes ut ON u.userType=ut.userTypeID'
    # return a list, every element in this list is a record(a row in database)
    result = db.Query(sql)

    # convert list into dataframe
    result1 = pd.DataFrame(list(result), columns=['userID', 'userName', 'userPassword', 'userType', 'balance'])

    #print(result1)
    return result1



def loadVehicles():
    """
    Load whole table of vehicles.
    Direcly call it

    Returns
    -------
    result2 : dataFrame
        This dataframe contains the whole table of vehicles.

    """
    # SQL query statement:load vehicle data
    sql = """SELECT vehicleID,v.vehicleTypeId,vt.vehicleTypeName, v.vehicleStatusId,vs.vehicleStatusName, pricePerMinute, batterySoc,v.cityLocationId, c.cityLocationName
             FROM vehicles v
             JOIN vehicleTypes vt ON v.vehicleTypeId=vt.vehicleTypeId
             JOIN vehicleStatuses vs ON v.vehicleStatusId=vs.vehicleStatusId
             JOIN cityLocations c ON v.cityLocationId=c.cityLocationId
             """
    # return a list, every element in this list is a record(a row in database)
    result = db.Query(sql)

    # convert list into dataframe
    result2 = pd.DataFrame(list(result), columns=['vehicleID', 'vehicleTypeId', 'vehicleTypeName', 'vehicleStatus', 'vehicleStatusName', 'pricePerMin', 'batterySoc', 'cityLocationId', 'cityLocationName'])

    #print(result2)
    return result2



def loadOrders():
    """
    Load whole table of orders.
    Direcly call it

    Returns
    -------
    result3 : dataFrame
        This dataframe contains the whole table of orders.
    """
    # SQL query statement:load order data
    sql = """SELECT orderId,vehicleId,userId,timeOrder,priceTotal,orderStatusId,orderTimestamp,rentCityLocationId,returnCityLocationId
           FROM orders
        """
    # return a list, every element in this list is a record(a row in database)
    result = db.Query(sql)

    # convert list into dataframe
    result3 = pd.DataFrame(list(result), columns=['orderId', 'vehicleId', 'userId', 'timeOrder', 'priceTotal', 'orderStatus', 'orderTimestamp', 'rentCityLocationId', 'returnCityLocationId'])

    #print(result3)
    return result3


def loadAvailableVehicles(cityLocationId:int,vehicleTypeId:int):
    """
    Load all the available vehicles in a citylocation.
    Directly call it

    Parameters
    ----------
    cityLocationId : int
        the cityLocationId you want to check its available vehicles.
    vehicleTypeId : int
         type of vehicle which you look for .

    Returns
    -------
    result4 : dataFrame
        This dataframe contains the list of specific kind of vehicles in specific cityLocation.

    """
    # SQL query statement:load available vehicles data
    sql = f"""SELECT cityLocationId, vehicleId, vehicleTypeId
           FROM vehicles
           WHERE  vehicleStatusId=1 AND cityLocationId='{str(cityLocationId)}' AND vehicleTypeId='{str(vehicleTypeId)}'"""

    # return a list, every element in this list is a record(a row in database)
    result = db.Query(sql)

    # convert list into dataframe
    result4 = pd.DataFrame(list(result), columns=['cityLocationId', 'vehicleId', 'vehicleTypeId'])
    #print(result4)
    return result4


def loadTheLatestIdInOrders():
    """
    Load all the latest order in descending sequence of orders table.
    Directly call it

    Returns
    -------
    result5 : dataFrame
        This dataframe contains the latest order in descending sequence of orders table.

    """
    sql = 'SELECT orderId from orders ORDER BY orderId DESC'

    # return a list, every element in this list is a record(a row in database)
    result = db.Query(sql)

    # convert list into dataframe
    result5 = pd.DataFrame(list(result), columns=['orderId'])
    #print(result5)
    return result5


def loadCityLocations(cityLocationId:int):
    """
    Load information of specific location.
    Direcly call it

    Parameters
    ----------
    cityLocationId : int
        Id of cityLocation you look for.

    Returns
    -------
    result6 : dataFrame
        This dataframe contains the information of specific location.

    """
    sql = 'SELECT * FROM cityLocations WHERE cityLocationId='+str(cityLocationId)

    # return a list, every element in this list is a record(a row in database)
    result = db.Query(sql)

    # convert list into dataframe
    result6 = pd.DataFrame(list(result), columns=['cityLocationId', 'cityLocationName', 'Altitude', 'Longitude'])
    #print(result6)
    return result6


def loadAllCityLocations():
    """
    Load all the citylocations in table.

    Returns
    -------
    result6 : dataFrame
        This dataframe contains the information of all location.

    """
    sql = 'SELECT * FROM cityLocations '

    # return a list, every element in this list is a record(a row in database)
    result = db.Query(sql)

    # convert list into dataframe
    result7 = pd.DataFrame(list(result), columns=['cityLocationId', 'cityLocationName', 'Altitude', 'Longitude'])
    #print(result7)
    return result7


def addNewUser(userName: str, userPassword: int, userType: int):
    """
    Add new user into users table.

    Parameters
    ----------
    userName : str
        name of new user.
    userPassword : int
        password of new user.
    userType : int
        type of user(1-manager,2-operator,3-customer).

    Returns
    -------
    None.

    """
    sql = f"""
        INSERT INTO users(userName,userPassword,userTYpe)
        VALUES('{userName}','{str(userPassword)}','{str(userType)}')
    """
    db.NonQuery(sql)















