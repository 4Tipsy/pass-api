from fastapi import FastAPI, HTTPException, Request, status, APIRouter
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from typing import Literal

import os

# desc
from server.config import Desc

# modules
from server.routes.fs import router as fs_router
from server.routes.user import router as user_router
from server.routes.utility import router as utility_router






# default on_error response | place me before app init
class OnErrorResModel(BaseModel):
  result: Literal['error']
  error: str



# app init
os.chdir(os.path.dirname(__file__)) # cwd = ./server
app = FastAPI(
  title='PASS API documentation',
  version='API 1.0',
  description=Desc.MAIN_APP_DESC,

  docs_url='/api/docs',
  redoc_url='/api/redoc',
  openapi_url='/api/openapi.json',

  responses={400: {'model': OnErrorResModel}}
)
# cors
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)



# routers
app.include_router(fs_router)
app.include_router(user_router)
app.include_router(utility_router)



# exception handlers overwrite
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException) -> OnErrorResModel:
  return JSONResponse(
      status_code=exc.status_code,
      content={'result': 'error', 'error': exc.detail}
    )

@app.exception_handler(Exception)
async def internal_server_exception_handler(request: Request, exc: HTTPException) -> OnErrorResModel:
  return JSONResponse(
      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
      content={'result': 'error', 'error': 'Internal server error'}
    )