from ..base import ClientBase


class HotelsClient(ClientBase):
    endpoint = '/hotels'

    def check_availability(self, data):
        """
        :param data: dict
                     json request
        :return: json response
                 includes list of hotels,
                 checkIn and checkOut dates,
                 total number of hotels found
        """
        return self._get_hotels_list(
                    self.transport.post(
                        self._url(),
                        data=data))

    def check_specific(self, hotel_code,
                       checkIn, checkOut,
                       adults, children,
                       rooms, paxes):
        """
        :param hotel_code: int
                           internal hotel code
        :param checkIn: str
        :param checkOut: str
        :param adults: int
        :param children: int
        :param rooms: int
        :param paxes: list
                      list of pax types of format: AD-30
        :return: json response
        """
        payload = {'checkIn': checkIn,
                   'checkOut': checkOut,
                   'occupancies': '{}~{}~{}~{}'.format(
                                    rooms, adults,
                                    children, ';'.join(paxes)
                   )}
        return self.transport.get(
                    self._url(hotel_code),
                    params=payload)

    def _get_hotels_list(self, resp):
        return resp['hotels']
