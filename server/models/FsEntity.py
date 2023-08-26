from pydantic import BaseModel, Field
from typing import Optional, Literal


class FsEntityModel(BaseModel):
  """Model of file or folder in pass \"file-system\""""
  name: str
  path: str # ./folder1/folder2/name
  type: Literal['file', 'folder']
  fileType: Optional[ Literal['img', 'txt', 'other'] ] = None # # not passed in request
  sizeInMB: Optional[ float ] = None # # not passed in request



class FsEntityInReqModel(FsEntityModel):
  """Only non-computable, received from client fields"""
  fileType: str = Field(exclude=True)
  sizeInMB: float = Field(exclude=True)