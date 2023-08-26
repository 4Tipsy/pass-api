from pydantic import BaseModel, Field
from typing import Optional, Literal




class FsEntityModel(BaseModel):
  """Model of file or folder in pass \"file-system\""""

  name: str
  path: str # ./folder1/folder2/name
  type: Literal['file', 'folder']
  fileType: Literal['img', 'txt', 'other'] # # not passed in request
  sizeInMB: float # # not passed in request



class FsEntityInReqModel(BaseModel):
  """Only non-computable, received from client fields"""
  # for some reason `Field(exclude=True)` doesn't work here...

  name: str
  path: str # ./folder1/folder2/name
  type: Literal['file', 'folder']
  # fileType: None
  # sizeInMB: None