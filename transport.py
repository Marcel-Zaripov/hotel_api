import requests
import hashlib
import time
from .exceptions import APIError, NotJsonError


class Transport(object):
    def __init__(self, url, api_key, secret):
        self._url = url
        self._api_key = api_key
        self._secret = secret

    def _signature(self):
        return hashlib.sha256(
            "{}{}{}".format(
                self._api_key,
                self._secret,
                int(time.time()))
            ).hexdigest()

    def get(self,
            url,
            extra_headers=None,
            params=None,
            sub_url=None):
        return self._request(
            'GET', url,
            extra_headers=extra_headers, params=params, sub_url=sub_url)

    def post(self,
             url,
             extra_headers=None,
             params=None,
             data=None):
        return self._request(
            'POST', url,
            extra_headers=extra_headers, params=params, data=data)

    def delete(self,
               url,
               extra_headers=None,
               params=None,
               data=None):
        return self._request(
            'DELETE', url,
            extra_headers=extra_headers, params=params, data=data)

    def _request(self,
                 method, url,
                 extra_headers=None,
                 params=None,
                 data=None,
                 sub_url=None):
        if sub_url:
            url = sub_url + url
        else:
            url = self._url + url
        headers = self._get_headers()
        if extra_headers:
            headers.update(extra_headers)
        resp = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=data)
        return self._unwrap_response(resp)

    def _get_headers(self):
        return {
            'X-Signature': self._signature(),
            'Api-Key': self._api_key,
            'Accept': 'application/json',
        }

    @staticmethod
    def _unwrap_response(resp):
        """
        Parameters
        ----------
        resp: requests.models.Response
        """
        try:
            dic = resp.json()
        except ValueError:
            raise NotJsonError(resp.text, resp.status_code)
        if resp.ok:
            return dic
        else:
            raise APIError(dic)
