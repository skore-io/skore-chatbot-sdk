import requests

HOST = "https://knowledge{enviroment}.skore.io"
MEYA_ERROR = "{host}/integration/v1/meya/erros"

class IntegrationServices:
  def __init__(self, host, enviroment = 'staging'):
    enviroment_format = ''
    if enviroment == 'staging': enviroment_format = '-%s' % enviroment    
    self.host = HOST.format(enviroment=enviroment_format)

  def send_meya_error(self, data, headers):
    url = MEYA_ERROR.format(self.host)
    response = requests.post(__url(), json=data, headers=headers())
    return response.status_code
