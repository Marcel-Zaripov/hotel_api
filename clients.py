from endpoints.hotels import HotelsClient
from endpoints.check_rates import CheckRatesClient
from endpoints.bookings import BookingsClient
from endpoints.status import StatusClient
from endpoints.content_hotels import HotelsContentClient
from endpoints.content_locations import LocationsContentClient
from endpoints.content_types import TypesContentClient
from endpoints.content_search import Search
from transport import Transport


class Base(object):
    endpoint = '/'

    def __init__(self, url=None, api_key=None,
                 secret=None, transport=None):
        if transport:
            self.transport = transport
        else:
            self.transport = Transport(url=url,
                                       api_key=api_key,
                                       secret=secret)

    @classmethod
    def factory(cls, transport):
        return cls(transport=transport)


class HotelApiClient(Base):
    endpoint = '/hotel-api/1.0'

    def __init__(self, url, api_key, secret):
        """
        :param url: str
                    main API's url
        :param api_key: str
        :param secret: str
        """
        super(HotelApiClient, self).__init__(url=url,
                                             api_key=api_key,
                                             secret=secret)
        self.hotels = HotelsClient(self)
        self.rates = CheckRatesClient(self)
        self.bookings = BookingsClient(self)
        self.status = StatusClient(self)


class HotelContentClient(Base):
    endpoint = '/hotel-content-api/1.0'

    def __init__(self, url, api_key, secret):
        """
        :param url: str
                    main API's url
        :param api_key: str
        :param secret:  str
        """
        super(HotelContentClient, self).__init__(url=url,
                                                 api_key=api_key,
                                                 secret=secret)
        self.hotels = HotelsContentClient(self)
        self.locations = LocationsContentClient(self)
        self.types = TypesContentClient(self)
        self.search = Search(self)


class Client(object):

    def __init__(self, url, api_key, secret):
        self.transport = Transport(url=url,
                                   api_key=api_key,
                                   secret=secret)
        self.api = HotelApiClient.factory(self.transport)
        self.content = HotelContentClient(self.transport)

# TODO: add logger
