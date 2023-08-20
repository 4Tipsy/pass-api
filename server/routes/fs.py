from fastapi import APIRouter, Depends, UploadFile
from pydantic import BaseModel
from typing import Literal

from ..dependencies.auth import auth
from ..controllers.FsEntity import FsEntityController

from ..models.FsEntity import FsEntityModel, FsEntityInReqModel






router = APIRouter(prefix='/api/fs-service', tags=['File system service'])

class ResponseModel(BaseModel):
  result: Literal['success']





# NEW FOLDER
class CreateNewFolderReqModel(BaseModel):
  fsEntity: FsEntityInReqModel
  fileField: Literal['mere', 'unmere', 'reserved']

@router.post('/create-new-folder')
def handle_create_new_folder(request: CreateNewFolderReqModel, user_id=Depends(auth)) -> ResponseModel:

  
  FsEntityController.create_entity(request.fsEntity, request.fileField, user_id)
  return {'result': 'success'}







# NEW FILE
class UploadNewFileReqModel(BaseModel):
  fsEntity: FsEntityInReqModel
  fileField: Literal['mere', 'unmere', 'reserved']
  file: UploadFile

@router.post('/upload-new-file')
def handle_upload_new_file(request: UploadNewFileReqModel, user_id=Depends(auth)) -> ResponseModel:
  

  FsEntityController.create_entity(request.fsEntity, request.fileField, user_id, file=UploadFile)
  return {'result': 'success'}





# RENAME
class RenameEntityReqModel(BaseModel):
  fsEntity: FsEntityInReqModel
  fileField: Literal['mere', 'unmere', 'reserved']
  newName: str

@router.post('/rename-entity')
def handle_rename_entity(request: RenameEntityReqModel, user_id=Depends(auth)) -> ResponseModel:
  

  FsEntityController.rename_entity(request.fsEntity, request.fileField, user_id, new_name=request.newName)
  return {'result': 'success'}






# DELETE
class DeleteEntityReqModel(BaseModel):
  fsEntity: FsEntityInReqModel
  fileField: Literal['mere', 'unmere', 'reserved']
  newName: str

@router.post('/delete-entity')
def handle_delete_entity(request: DeleteEntityReqModel, user_id=Depends(auth)) -> ResponseModel:
  

  FsEntityController.delete_entity(request.fsEntity, request.fileField, user_id)
  return {'result': 'success'}






# GET FS LAYER
class GetFsLayerReqModel(BaseModel):
  pathToLayer: str
  fileField: Literal['mere', 'unmere', 'reserved']

class GetFsLayerResModel(BaseModel):
  result: Literal['success']
  fsLayer: list[FsEntityModel]

@router.post('/get-fs-layer')
def handle_get_fs_layer(request: GetFsLayerReqModel, user_id=Depends(auth)) -> GetFsLayerResModel:
  

  fs_layer = FsEntityController.get_fs_layer(request.pathToLayer, request.fileField, user_id)
  return {'result': 'success', 'fsLayer': fs_layer}