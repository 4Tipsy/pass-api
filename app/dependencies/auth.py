from fastapi import Request, HTTPException, status
import jwt
from jwt.exceptions import InvalidTokenError

from ..config import Cfg

from ..database.DbController import DbController


from ..models.AToken import ATokenModel



def auth(request: Request) -> int | HTTPException:
  """
  Checks jwt token and return user_id(encoded in token) if everything is ok;
  return error if jwt is invalid, not exist, out of epoch, or user is not verified
  """
  

  a_token = request.cookies.get('a-token')

  # if no token
  if not a_token:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User is not logged')


  # validate jwt
  try:
    a_token: ATokenModel = jwt.decode(a_token, Cfg.JWT_SECRET_KEY, algorithms=["HS256"])

  except InvalidTokenError:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid auth token')


  # checks
  current_user = DbController.get_user(a_token['id'])

  if not current_user['verified']:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User is not verified")
  if current_user['jwtEpoch'] != a_token['epoch']:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid auth token')
  


  # if ok
  return a_token['id']