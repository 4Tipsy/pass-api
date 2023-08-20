from pydantic import BaseModel
from typing import Optional, Literal


class FsEntityModel(BaseModel):
  name: str
  path: str # ./folder1/folder2/name
  type: Literal['file', 'folder']
  fileType: Optional[ Literal['img', 'txt', 'other'] ] = None # # not passed in request
  sizeInMB: Optional[ float ] = None # # not passed in request



class FsEntityInReqModel(BaseModel):
  name: str
  path: str # ./folder1/folder2/name
  type: Literal['file', 'folder']