class User( object ):
  def __init__(self, id):
    self.id = id
    self.jwt_token = None
    self.refresh_token = None
    self.skore_user_id = None
    self.meya_user = None

  def signed_in(self):
      return self.jwt_token != None and self.refresh_token != None and self.skore_user_id != None

  def clean_up_credentials(self, sync = True):
    self.jwt_token = None
    self.refresh_token = None
    if sync: self.__sync()

  def update_credentials(self, token, token_refresh, sync = True):
    self.jwt_token = token
    self.refresh_token = token_refresh
    if sync: self.__sync()

  def __sync(self):
    self.meya_user.set('jwt_token', self.jwt_token)
    self.meya_user.set('refresh_token', self.refresh_token)

  @staticmethod
  def factory(meya_user):
    if meya_user == None: return None
    class SmoochUser( User ):
        def __init__(self, id, skore_user_id):
          super( SmoochUser, self ).__init__(id)
          self.skore_user_id = skore_user_id


    class MeyaUser( User ):
        def __init__(self, id, skore_user_id):
          super( MeyaUser, self ).__init__(id)

    user = None
    try:
      integrations = meya_user.get('_integrations')
      if 'smooch' in integrations:
        user = SmoochUser(meya_user.get('id'), integrations['smooch']['user_id'])
      else:
        user = MeyaUser(meya_user.get('id'), meya_user.get('skore_user_id'))
    except KeyError:
        return user
    user.skore_company_id = meya_user.get('skore_company_id')
    user.jwt_token = meya_user.get('jwt_token')
    user.refresh_token = meya_user.get('refresh_token')
    user.name = meya_user.get('name')
    user.email = meya_user.get('email')

    user.meya_user = meya_user

    return user
