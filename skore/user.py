
class User( object ):
  def __init__( self, id, token=None, token_refresh=None):
    self.id = id
    self.token = token
    self.token_refresh = token_refresh

  def update_credentials(self, token, token_refresh):
    self.token = token
    self.token_refresh = token_refresh
