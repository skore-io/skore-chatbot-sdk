
from meya.cards import Card, Cards, Button
from skore.recommendation_service import RecommendationService

class RecommendationCard(object):
  def __init__(self, host):
    self.service = RecommendationService(host)

  def build(self, token, recipe_id, flows=None, items=None, grouped=None):
    response = self.service.perform(token, recipe_id)
    if response.status_code != 200: return response.raise_for_status()

    flows = response.json()
    elements = []
    for content in flows:
      content_url = content['url']
      buttons = [
          Button(text='Ver Agora', webview_height_ratio='full', url=content_url,
                  fallback_url=content_url),
          Button(text='Manda Outro', flow='chef')
      ]
      element = Card(
          title=content['name'], image_url=content['thumb_url'],
          buttons=buttons
      )
      elements.append(element)

    return Cards(elements=elements)
