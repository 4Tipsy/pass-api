from fastapi import APIRouter
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Literal

from ..config import Cfg




router = APIRouter(prefix='/api/utility-service', tags=['Utility service'])

class ResponseModel(BaseModel):
  """Default response model"""
  result: Literal['success']






# CHECK SERVER STATUS
class ResponseModel(BaseModel):
  result: Literal['success']
  apiVersion: str

@router.get('/get-api-version')
def handle_get_api_version() -> ResponseModel:
  
  return {
    'result': 'success',
    'apiVersion': f'PASS API {Cfg.API_VERSION}'
    }



# in dev... cli in dev...





# lol why not?

@router.get('/uwu', include_in_schema=False)
def get_uwu() -> None:
  return FileResponse('./utils/uwu.png')