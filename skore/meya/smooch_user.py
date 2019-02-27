from skore.user import User

class SmoochUser( User ):
  def __init__(self, meya_user):
    integrations = meya_user.get('_integrations')
    if 'smooch' not in integrations: return
    self.meya_user = meya_user
    super( SmoochUser, self ).__init__(
      integrations['smooch']['user_id'],
      meya_user.get('token'),
      meya_user.get('token_refresh')
    )

  def update_credentials(self, token, token_refresh):
    super( SmoochUser, self ).update_credentials(token, token_refresh)
    self.meya_user.set('token', token)
    self.meya_user.set('token_refresh', token_refresh)
    # Included to keep compatibility with legacy
    self.meya_user.set('jwt_token', token)
    self.meya_user.set('refresh_token', token_refresh)
