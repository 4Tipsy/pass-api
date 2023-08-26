from fastapi import APIRouter
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Literal




router = APIRouter(prefix='/api/utility-service', tags=['Utility service'])

class ResponseModel(BaseModel):
  """Default response model"""
  result: Literal['success']






# CHECK SERVER STATUS

@router.head('/get-server-status', response_model=None)
def handle_get_server_status() -> None:
  
  return





# GET PASS CLI VERSION
# in dev... cli in dev...





# lol why not?

@router.get('/uwu', include_in_schema=False)
def get_uwu() -> None:
  return FileResponse('./utils/uwu.png')