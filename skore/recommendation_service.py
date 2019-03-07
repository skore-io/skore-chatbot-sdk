import requests

CHEF_URL = "{host}/chef/v1/chef/{recipe_id}?amountItemsByFlow={items}&amountFlows={flows}&grouped=true"

class RecommendationService(object):

  def __init__(self, host):
    self.host = host

  def perform(self, token, recipe_id, flows=1, items=1):
    url = CHEF_URL.format(
        host=self.host,
        recipe_id=recipe_id,
        flows=flows,
        items=items)
    return requests.get(
        url=url,
        headers={'Authorization': token}
    )
