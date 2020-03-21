from ..base import ClientBase
from ..exceptions import APIError, NotJsonError


class StatusClient(ClientBase):
    endpoint = "/status"

    def check(self):
        try:
            return self.transport.get(self._url())
        except (APIError, NotJsonError) as e:
            return {'status': e.as_dict()['status_code'],
                    'error': e.as_dict()['error']}
