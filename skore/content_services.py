import sentry_sdk
from skore.base_services import BaseServices
from sentry_sdk import capture_message
import datetime

CHEF_API_URL = "{host}/chef/v1/chef/{recipe_id}?amountItemsByFlow={items}&amountFlows={flow}&grouped={grouped}"

class ContentServices( BaseServices ):
  def __init__(self, host, app_token, user):
    sentry_sdk.init("https://d8a8d0686b2c4da8b906eac1f1ecf5af@sentry.io/1400364")
    now = datetime.datetime.now()
    capture_message('Something went wrong time:%s' % str(now))
    super( ContentServices, self ).__init__(host, app_token, user)

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
