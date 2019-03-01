import requests

CURRENT_USER_URL = "{host}/workspace/v1/users/current"

class SkoreKnowledgeService( object ):
  def __init__(self, host):
    self.host = host

  def current_user(self, token):
    url = CURRENT_USER_URL.format(host=self.host)
    return requests.get(
      url=url,
      headers={ 'Authorization': token }
    )
