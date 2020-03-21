from ..base import ClientBase


class Search(ClientBase):
    endpoint = '/search'

    def __init__(self, client):
        self.client = client
        self.endpoint = client.endpoint[:-4] + self.endpoint

    def destination(self, text):
        return self.transport.get(url=self._url('Zone'),
                                  params={'query': '*{}*'.format(text),
                                          'language': 'ENG'},
                                  sub_url='http://testapi.hotelbeds.com')

    def zone(self, text):
        return self.transport.get(url=self._url('Zone'),
                                  params={'query': '*{}*'.format(text),
                                          'language': 'ENG'},
                                  sub_url='http://testapi.hotelbeds.com')
