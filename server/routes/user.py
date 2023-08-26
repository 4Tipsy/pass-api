from fastapi import APIRouter, Response, Depends
from pydantic import BaseModel
from typing import Literal

from datetime import datetime, timedelta


from ..dependencies.auth import auth
from ..controllers.User import UserController

from ..models.User import UserModel, UserInReqModel, UserInResModel





router = APIRouter(prefix='/api/user-service', tags=['User service'])

class ResponseModel(BaseModel):
  """Default response model"""
  result: Literal['success']






# NEW USER
class CreateNewUserReqModel(BaseModel):
  newUser: UserInReqModel

@router.post('/create-new-user')
def handle_create_new_user(request: CreateNewUserReqModel) -> ResponseModel:
  

  UserController.create_user(request.newUser)
  return {'result': 'success'}





# GET AUTH TOKEN | LOGIN
class LoginReqModel(BaseModel):
  userToLogin: UserInReqModel

@router.post('/login')
def handle_login(request: LoginReqModel, response: Response) -> ResponseModel:


  a_token = UserController.get_auth_token(request.userToLogin)


  # get current_time + 30days to pass in cookie expires
  expires_time = datetime.utcnow() + timedelta(days=30)
  expires_time = expires_time.strftime('%a, %d %b %Y %H:%M:%S GMT')


  response.set_cookie(key='a-token', value=a_token, expires=expires_time)
  return {'result': 'success'}





# GET USER
class GetUserResModel(BaseModel):
  result: Literal['success']
  user: UserInResModel

@router.get('/get-user', description='**(auth needed)**')
def handle_get_user(user_id=Depends(auth)) -> GetUserResModel:
  

  user = UserController.get_user(user_id)
  return {'result': 'success', 'user': user}