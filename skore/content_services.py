from skore.base_services import BaseServices

CHEF_API_URL = "{host}/chef/v1/chef/{recipe_id}?amountItemsByFlow={items}&amountFlows={flow}&grouped={grouped}"
CURRENT_USER_URL = "{host}/workspace/v1/users/current"

class ContentServices( BaseServices ):
  def __init__(self, host, app_token, user):
    super( ContentServices, self ).__init__(host, app_token, user)

  def current_user(self):
    url = CURRENT_USER_URL.format(host=self.host)    
    return self.get(url).json()

  def recommendation(self, recipe_id, options = {'flow': 1, 'items':1, 'grouped': 'false'}):
    response = self.__query_chef(recipe_id, options)
    return response.json()
    
  def __query_chef(self, recipe_id, options):
    flow = options['flow'] if 'flow' in options else 1
    items = options['items'] if 'items' in options else 1
    grouped = options['grouped'] if 'grouped' in options else 'false'

    url = CHEF_API_URL.format(
      host=self.host,
      recipe_id=recipe_id,
      flow=flow,
      items=items,
      grouped=grouped
    )
    return self.get(url)
