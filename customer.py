import mySQL as sql
from user import User
from Vehicle import Vehicle
from CityLocation import CityLocation
from Order import Order


class Customer(User):
    orderId: int = None          # will be generated when new order is created
    # omit this part of the code
