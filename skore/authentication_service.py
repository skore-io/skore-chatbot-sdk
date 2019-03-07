import requests

LOGIN_URL = "{url}/workspace/v3/login"
REFRESH_API_URL = "{host}/workspace/v1/refresh_token"
CREATE_API_URL = "{host}/workspace/v1/users/{user_id}/sessions"

class AuthenticationService:
    def __init__(self, host, enviroment):
        self.enviroment = enviroment
        self.host = host

    def login(self, email_or_username, password, company_id):
        data = {
            'email': email_or_username,
            'password': password,
            'company_id': company_id
        }
        headers = {
            'Content-Type': 'application/json'
        }
        return requests.post(
            url=LOGIN_URL.format(url=self.host),
            json=data,
            headers=headers)

    def refresh_token(self, token, token_refresh):
        url = REFRESH_API_URL.format(host=self.host)
        headers = { 'Content-Type': 'application/json' }
        data = {
          'token': token,
          'token_refresh': token_refresh
        }
        return requests.post(url=url, json=data, headers=headers)

    def create_session(self, skore_user_id, app_skore_token):
      url = CREATE_API_URL.format(host=self.host, user_id=skore_user_id)
      headers = {
          'Content-Type': 'application/json',
          'Authorization': app_skore_token
      }
      data = {
          'client_type': 'meya'
      }
      return requests.post(url=url, json=data, headers=headers)
