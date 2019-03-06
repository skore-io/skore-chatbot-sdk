import requests

CHEF_URL = "{host}/chef/v1/chef/{recipe_id}?amountItemsByFlow={items}&amountFlows={flows}&grouped={grouped}"

class RecommendationService(object):

  def __init__(self, host):
    self.host = host

  def perform(self, token, recipe_id, items=1, flows=1, grouped=False):
    url = CHEF_URL.format(
        host=self.host,
        recipe_id=recipe_id,
        flows=flows,
        items=items,
        grouped=grouped)
    return requests.get(
        url=url,
        headers={'Authorization': token}
    )
