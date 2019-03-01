from skore.user import User

class MeyaUser( User ):
  def __init__(self, meya_db_user):
    self.user = meya_db_user


