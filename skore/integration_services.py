import requests

HOST = "https://knowledge{enviroment}.skore.io"
MEYA_ERROR = "{host}/integration/v1/meya/erros"

class IntegrationServices:
  def __init__(self, host, enviroment = 'staging'):
    self.enviroment = enviroment
    self.host = host

  def send_meya_error(self, data, headers):
    url = MEYA_ERROR.format(host=self.host)
    response = requests.post(__url(), json=data, headers=headers())
    return response.status_code
