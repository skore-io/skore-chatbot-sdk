import requests

CURRENT_USER_URL = "{host}/workspace/v1/users/current"
PREFERENCES_USER_URL = "{host}/workspace/v1/users/preferences"
CONTENT_PROVISION_URL = "{host}/workspace/{version}/contents/{content_id}/provision"
CONTENT_SEARCH_URL = "{host}/workspace/{version}/search"

class SkoreKnowledgeService( object ):
  def __init__(self, host):
    self.host = host

  def content_provision(self, token, content_id, version = 'v1'):
    headers = {'Authorization': token }
    url = CONTENT_PROVISION_URL.format(
        host=self.host,
        version=version,
        content_id=content_id
    )
    return requests.get(url=url, headers=headers)

  def current_user(self, token):
    url = CURRENT_USER_URL.format(host=self.host)
    return requests.get(
      url=url,
      headers={ 'Authorization': token }
    )

  def update_user_preferences(self, token, data):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    url = PREFERENCES_USER_URL.format(host=self.host)
    return requests.patch(url=url, json=data, headers=headers)

  def search_content(self, token, query, version = "v1", limit = 3):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    url = CONTENT_SEARCH_URL.format(
        host=self.host,
        version=version
    )
    params = {
      "q": query,
      "limit": limit
    }
    return requests.get(url = url, params = params, headers = headers)
