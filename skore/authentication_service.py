import requests

LOGIN_URL = "{url}/workspace/v3/login"
REFRESH_API_URL = "{host}/workspace/v1/refresh_token"
CREATE_API_URL = "{host}/workspace/v1/users/{user_id}/sessions"

class AuthenticationService:
    def __init__(self, host, enviroment, company_id, skore_token):
        self.enviroment = enviroment
        self.host = host
        self.company_id = company_id
        self.skore_token = skore_token

    def login(self, email_or_username, password):
        data = {
            'email': email_or_username, 
            'password': password, 
            'company_id': self.company_id
        }
        headers = {
            'Content-Type': 'application/json'
        }    
        response = requests.post(
            url=LOGIN_URL.format(url=self.host),
            json=data,
            headers=headers)
        if response.status_code != 200: return response.raise_for_status()

        return response.json()

    def refresh_token(self, token, token_refresh):
        url = REFRESH_API_URL.format(host=self.host)
        headers = { 'Content-Type': 'application/json' }
        data = {
          'token': token, 
          'token_refresh': token_refresh
        }
        return requests.post(url=url, json=data, headers=headers)

    def create_session(self, skore_user_id):
      url = CREATE_API_URL.format(host=self.host, user_id=skore_user_id)
      headers = {
          'Content-Type': 'application/json',
          'Authorization': self.skore_token
      }
      data = {
          'client_type': 'meya'
      }
      return requests.post(url=url, json=data, headers=headers)
