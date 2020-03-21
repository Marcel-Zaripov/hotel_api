from ..base import ClientBase


class CheckRatesClient(ClientBase):
    endpoint = "/checkrates"

    def check(self, rate_key, upselling=False, language='ENG'):
        """
        :param rate_key: str
                         unique id of product for rate/dates
                         combination
        :param upselling: bool
                          whether to include
                          additional room options
        :param language: str
        :return: json response
        """
        payload = {'rateKey': rate_key,
                   'upselling': upselling,
                   'language': language}
        return self.transport.get(
                    self._url(),
                    params=payload)
