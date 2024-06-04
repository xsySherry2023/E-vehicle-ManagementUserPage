"""Script contains the CityLocation class."""
import Vehicle
from mySQL import loadCityLocations, loadAvailableVehicles

class CityLocation():
    """
    The CityLocation class contains the attributes:
        - cityLocationId
    and the methods:
        (- constructor)
        - assignVehicle
    """
    cityLocationId: int

    def __init__(self, cityLocationIdRequested: int):
        """
        Constructor of the class. Query the data from data base for a specified cityLocationId

        Parameters
        ----------
        cityLocationIdRequested : int
            cityLocationId where data should be queried from database.

        Raises
        ------
        ValueError
            Raises ValueError if cityLocationIdRequested has been handed over which is not available in database.

        Returns
        -------
        Object of Class CityLocation

        """
        # omit this part of the code