from fastapi import HTTPException, status
import jwt
import re

from ..database.DbController import DbController

from ..utils.hashing_password import HashingPassword


from ..models.User import UserModel, UserInReqModel, UserInResModel
from ..models.AToken import ATokenModel

from ..config import Cfg


# !!!
from .FsEntity import FsEntityController




class UserController:




  @staticmethod
  def create_user(new_user: UserInReqModel) -> None | HTTPException: # takes {name, password}
    """Will add new user to DB, and create corresponding user folder"""

    # checks
    if not re.match("[a-zA-z0-9\\\h.,()-_]", new_user.name):
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Unacceptable username')
    if not re.match("[a-zA-z0-9\\\h.,()-_]", new_user.password):
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Unacceptable password')
    

    # get hashed password
    hashed_password = HashingPassword.get_hashed_password(new_user.password)

    # creating new user
    new_user_obj = {}
    new_user_obj['name'] = new_user.name
    new_user_obj['password'] = hashed_password
    new_user_obj['verified'] = False
    new_user_obj['jwtEpoch'] = 1
    new_user_obj['spaceAvailableInMb'] = Cfg.DEFAULT_AVAILABLE_SPACE_IN_MB
    new_user_obj['spaceUsedInMb'] = 0
    #new_user['id'] = will be assigned in DbController


    # db connect
    user_id = DbController.add_user(new_user_obj)

    # create user folder
    FsEntityController.create_new_user_folder(user_id)








  @staticmethod
  def get_auth_token(user_to_auth: UserInReqModel) -> ATokenModel | HTTPException:
    """Will get user from DB by name, check password, and if ok return ready a_token"""

    current_user: UserModel = DbController.get_user_by_name(user_to_auth.name)


    # password check
    if not HashingPassword.check_if_password_valid(user_to_auth.password, current_user['password']):
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password or name is wrong")
    


    payload = {
        'id': current_user['id'],
        'epoch': current_user['jwtEpoch']
      }
    
    a_token = jwt.encode(payload, Cfg.JWT_SECRET_KEY, algorithm="HS256")


    return a_token
  











  @staticmethod
  def get_user(user_id: int) -> UserInResModel:

    user = DbController.get_user(user_id)

    
    return user