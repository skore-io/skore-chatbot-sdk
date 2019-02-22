from skore.base_services import BaseServices

CURRENT_USER_URL = "{host}/workspace/v1/users/current"

class WorkspaceServices( BaseServices ):
  def __init__(self, host, app_token, user):
    super( WorkspaceServices, self ).__init__(host, app_token, user)

  def current_user(self):
    url = CURRENT_USER_URL.format(host=self.host)    
    return self.get(url).json()
