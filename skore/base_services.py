import requests

REFRESH_API_URL = "{host}/workspace/v1/refresh_token"
CREATE_API_URL = "{host}/workspace/v1/users/{user_id}/sessions"

class BaseServices( object ):
  def __init__(self, host, app_token, user):
    self.host = host
    self.app_token = app_token
    self.user = user
    if self.user.token == None or self.user.token_refresh == None:
      self.__create_session()

  def get(self, url):
    response = requests.get(
      url=url,
      headers={ 'Authorization': self.user.token }
    )

    if response.status_code == 200: return response

    if response.status_code == 401: 
      self.__refresh_session()
      
    response = requests.get(
      url=url, 
      headers={ 'Authorization': self.user.token }
    )
    if response.status_code == 200: return response
    
    return response.raise_for_status()

  def __refresh_session(self):
      url = REFRESH_API_URL.format(host=self.host)
      headers = { 'Content-Type': 'application/json' }
      data = {
          'token': self.user.token, 
          'token_refresh': self.user.token_refresh
      }
      response = requests.post(url=url, json=data, headers=headers)
      if response.status_code != 200: return response.raise_for_status()
      self.__set_credentials(response.json())

  def __create_session(self):
      url = CREATE_API_URL.format(host=self.host, user_id=self.user.id)
      headers = {
          'Content-Type': 'application/json',
          'Authorization': self.app_token
      }
      data = {
          'client_type': 'meya'
      }
      response = requests.post(url=url, json=data, headers=headers)
      if response.status_code != 201: return response.raise_for_status()
      self.__set_credentials(response.json())

  def __set_credentials(self, credentials):
      self.user.update_credentials(
        credentials['token'],
        credentials['token_refresh']
      )
