class ClientBase(object):
    """ Other endpoints are build on top
    """
    endpoint = "/"

    def __init__(self, client):
        self.client = client
        self.endpoint = client.endpoint + self.endpoint

    @property
    def transport(self):
        """
        return type: transport.Transport
        """
        return self.client.transport

    def _url(self, *params):
        url = (self.endpoint + ''.join(
                                '/' + str(p)
                                for p in params
                                if p is not None))
        return url
