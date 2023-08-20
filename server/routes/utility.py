from fastapi import APIRouter
from pydantic import BaseModel
from typing import Literal




router = APIRouter(prefix='/api/utility-service', tags=['Utility service'])

class ResponseModel(BaseModel):
  result: Literal['success']






# CHECK SERVER STATUS

@router.get('/get-server-status')
def handle_get_server_status() -> ResponseModel:
  
  return {
    'result': 'success'
  }