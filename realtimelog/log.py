import json
import requests


REAL_TIME_LOG_BASE_URL = 'https://realtimelog.herokuapp.com:443/'


class Client():
  """REAL-TIME log client."""


  def __init__(self, app_id):
    if app_id:
      self.url = REAL_TIME_LOG_BASE_URL + app_id
    else:
      res = requests.get(REAL_TIME_LOG_BASE_URL)
      self.url = res.url


  def get_url(self):
    return self.url


  def msg(self, data):
    requests.post(
      self.url,
      headers={'Content-Type': 'application/json'},
      data=json.dumps(data),
    )
