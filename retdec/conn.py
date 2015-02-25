"""
    API connection.

    :copyright: © 2015 by Petr Zemek <s3rvac@gmail.com> and contributors
    :license: MIT, see the ``LICENSE`` file for more details
"""

import re

import requests

from retdec.file import File


class APIConnection:
    """Connection to the API."""

    def __init__(self, base_url, api_key):
        """Initializes an API connection.

        :param str base_url: Base URL from which all subsequent URLs are
                             constructed.
        :param str api_key: API key to be used for authentication.
        """
        self._base_url = base_url
        self._api_key = api_key

    def send_get_request(self, path='', params=None):
        """Sends a GET request to the given path with the given parameters.

        :param str path: Path to which the request should be sent.
        :param dict params: Request parameters.

        :returns: Response from the API (parsed JSON).

        If `path` is the empty string, it sends the request to the base URL
        from which the connection was initialized.
        """
        response = self._send_request('get', path, params=params)
        return response.json()

    def send_post_request(self, path='', params=None, files=None):
        """Sends a POST request to the given path with the given parameters.

        :param str path: Path to which the request should be sent.
        :param dict params: Request parameters.
        :param dict files: Request files.

        :returns: Response from the API (parsed JSON).

        If `path` is the empty string, it sends the request to the base URL
        from which the connection was initialized.
        """
        response = self._send_request('post', path, params=params, files=files)
        return response.json()

    def get_file(self, path='', params=None):
        """GETs a file from the given path with the given parameters.

        :param str path: Path to which the request should be sent.
        :param dict params: Request parameters.

        :returns: File from `path` (:class:`retdec.file.File`).

        If `path` is the empty string, it sends the request to the base URL
        from which the connection was initialized.
        """
        response = self._send_request('get', path, params=params, stream=True)
        # File responses contain the Content-Disposition header, which includes
        # the name of the file in "filename=name-of-file".
        # https://retdec.com/api/docs/essential_information.html#id3
        m = re.search('filename=(\S+)', response.headers['Content-Disposition'])
        return File(response.raw, m.group(1))

    @property
    def _session(self):
        """Session to be used to send requests."""
        # We create and store a session into self under key '_session'. In this
        # way, we can check whether the session already exists and if so, we
        # may directly return it without re-creating it.
        if '_session' not in self.__dict__:
            self.__dict__['_session'] = self._start_new_session()

        return self.__dict__['_session']

    def _start_new_session(self):
        """Starts a new session to be used to send requests and returns it."""
        session = requests.Session()

        # We have to authenticate ourselves by using the API key, which should
        # be passed as 'username' in HTTP Basic Auth. The 'password' part
        # should be left empty.
        # https://retdec.com/api/docs/essential_information.html#authentication
        session.auth = (self._api_key, '')

        return session

    def _send_request(self, method, path, **kwargs):
        """Sends a request through the given method with the given arguments.

        :returns: Response from the request.
        """
        url = self._base_url + path
        return getattr(self._session, method)(url, **kwargs)