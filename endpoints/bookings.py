from ..base import ClientBase


class BookingsClient(ClientBase):
    endpoint = "/bookings"

    def confirm(self, data):
        """
        :param data: dict
                     json request
        :return: json response
        """
        return self.transport.post(
                    self._url(),
                    data=data)

    def get(self, booking_id):
        """
        :param booking_id: str
                           id in format: XXX-XXXXXXX
        :return: json response
        """
        return self.transport.get(
                    self._url(booking_id))

    def list(self, start_date, end_date,
             filter_type="CREATION",
             cancelled=True,
             list_from=1, list_to=25):
        """
        :param start_date: str
                           date in ISO format: YYYY-MM-DD
        :param end_date: str
                           date in ISO format: YYYY-MM-DD
        :param filter_type: str
                            indicates if dates refer to booking
                            creation or check in date
        :param cancelled: bool
                          whether to include cancelled or
                          only confirmed
        :param list_from: int
                          booking list from
        :param list_to: int
                        booking list to
        :return: json response
        """

        payload = {'start': start_date,
                   'end': end_date,
                   'filterType': filter_type,
                   'includeCancelled': cancelled,
                   'from': list_from,
                   'to': list_to}
        return self.transport.get(
                    self._url(),
                    params=payload)

    def cancel(self, booking_id,
               flag="SIMULATION"):
        """
        :param booking_id: str
                           id in format: XXX-XXXXXXX
        :param flag: str
                     If CANCELLATION performs the cancellation.
                     If SIMULATION only a simulation of
                     the cancellation is done
                     to check the cancellation policies
        :return: json response
        """
        payload = {'cancellationFlag': flag}
        return self.transport.delete(
                    self._url(booking_id),
                    params=payload)
