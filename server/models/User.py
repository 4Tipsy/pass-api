from pydantic import BaseModel, Field


class UserModel(BaseModel):
  """Model of user in pass system"""
  id: int # # not passed in request # # not passed in response
  name: str
  password: str # # not passed in response

  verified: bool # # not passed in request
  jwtEpoch: int # # not passed in request # # not passed in response

  spaceUsedInMb: int # # not passed in request
  spaceAvailableInMb: int # # not passed in request



class UserInReqModel(BaseModel):
  """Only 'name' and 'password'"""
  name: str
  password: str




# this one is returned to client
class UserInResModel(UserModel):
  """Only fields crucial for client"""

  id: int = Field(exclude=True)
  password: str = Field(exclude=True)
  jwtEpoch: int = Field(exclude=True)
