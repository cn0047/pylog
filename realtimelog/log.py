""" This module contains client for REAL-TIME log. """

import json
import requests


REAL_TIME_LOG_BASE_URL = 'https://realtimelog.herokuapp.com:443/'


class Client():
    """ REAL-TIME log client. """


    def __init__(self, app_id=''):
        if app_id:
            self.url = REAL_TIME_LOG_BASE_URL + app_id
        else:
            res = requests.get(REAL_TIME_LOG_BASE_URL)
            self.url = res.url


    def get_url(self):
        """ Gets public URL to REAL-TIME log dashboard. """
        return self.url


    def msg(self, data):
        """
        Sends log message to REAL-TIME log.

        Parameters
        ----------
        data:
            Any arbitrary data which will be sent to log.
        """
        requests.post(
            self.url,
            headers={'Content-Type': 'application/json'},
            data=json.dumps(data),
        )
