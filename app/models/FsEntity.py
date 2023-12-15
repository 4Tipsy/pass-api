from pydantic import BaseModel, Field
from typing import Optional, Literal









class FsEntityModel(BaseModel):
  """Model of file or folder in pass \"file-system\""""

  name: str
  absPathToEntity: str # /folder1/folder2/name
  type: Literal['file', 'folder']
  mimeType: Optional[str] = None # # not passed in request
  sizeInMB: Optional[float] = None # # not passed in request



class FsEntityInReqModel(BaseModel):
  """Only non-computable, received from client fields"""
  # for some reason `Field(exclude=True)` doesn't work here...

  name: str
  absPathToEntity: str # /folder1/folder2/name
  type: Literal['file', 'folder']
  # mimeType: None
  # sizeInMB: None
