
import googlemaps
import dataclasses
from dataclasses import dataclass
from GMPk import gmp




@dataclass
class GMProute:
    """
    GMP Route
    """
    start: str
    end: str
    
    def get_gmaps_route(start, end, mode='driving', avoid=None, units='metric',
                        departure_time=None, traffic_model=None, c = None):
        """
        Get GMP Route
        :param start:
        :param end:
        :param mode:
        :param avoid:
        :param units:
        :param departure_time:
        :param traffic_model:
        :return:
        
        """
        gmaps = googlemaps.Client(key=c)



