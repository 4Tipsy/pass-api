from pydantic import BaseModel


class UserModel(BaseModel):
  id: int # # not passed in request
  name: str
  password: str

  verified: bool # # not passed in request
  jwtEpoch: int # # not passed in request

  spaceUsedInMb: int # # not passed in request
  spaceAvailableInMb: int # # not passed in request



class UserInReqModel(BaseModel):
  name: str
  password: str