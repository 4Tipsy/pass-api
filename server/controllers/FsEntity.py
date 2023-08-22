from fastapi import HTTPException, UploadFile, status
from typing import Literal, Optional
import os, json, re, shutil

from ..models.FsEntity import FsEntityModel




class FsEntityController:
  


  @staticmethod
  def _get_path_to_entity_parent(user_folder, file_field, entity_path) -> str:
    # -> STORAGE/user_folder/file_field/*/
    path_ = os.path.join('../STORAGE', user_folder, file_field.upper(), entity_path)
    return os.path.dirname(path_)






  @staticmethod
  def _edit_parent_structure_json(action: Literal['add', 'del', 'rename'], fs_entity: FsEntityModel, path_to_parent, new_name=None) -> None:
    path_to_structure = os.path.join(path_to_parent, 'structure.json')


    # open
    with open(path_to_structure, 'r', encoding='utf8') as read_file:
      structure: list = json.load(read_file)

    # change
    if action == 'add':
      structure.append(fs_entity.model_dump(exclude_none=True))
    if action == 'del':
      structure = list(filter( lambda e: e['name'] != fs_entity.name, structure ))
    if action == 'rename':
      for e in structure:
        if e['name'] == fs_entity.name:
          e['name'] = new_name

    # save
    with open(path_to_structure, 'w', encoding='utf8') as write_file:
      json.dump(structure, write_file, indent=4)












  @staticmethod
  def create_entity(fs_entity: FsEntityModel, file_field: Literal['mere', 'unmere', 'reserved'], user_id: int, file: Optional[UploadFile]=None) -> None | HTTPException:

    # init vars
    user_folder = f"UF__{user_id}"
    path_to_parent = FsEntityController._get_path_to_entity_parent(user_folder, file_field, fs_entity.path) # from STORAGE/ to folder_where_stored/



    # additional vars for files
    if fs_entity.type == 'file':
      fs_entity.fileType = file.content_type.split('/')[0]
      fs_entity.sizeInMB = file.size / 1024 / 1024


    
    # checks
    if not re.match("[a-zA-z0-9\\\h.,()-_]", fs_entity.name):
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Unacceptable {fs_entity.type} name')
    if os.path.exists(fs_entity.path):
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Such {fs_entity.type} already exist')
    


    # create
    full_path = os.path.join(path_to_parent, fs_entity.name)

    if fs_entity.type == 'folder':
      os.mkdir(full_path)
      # creating structure.json
      with open( os.path.join(full_path, 'structure.json'), 'w', encoding='utf8') as new_file:
        json.dump([], new_file)

    
    if fs_entity.type == 'file':
      with open(full_path, 'wb') as new_file:
        while chunk := file.file.read(1024 * 1024):
          new_file.write(chunk)


    # edit structure
    FsEntityController._edit_parent_structure_json('add', fs_entity, path_to_parent)









  @staticmethod
  def delete_entity(fs_entity: FsEntityModel, file_field: Literal['mere', 'unmere', 'reserved'], user_id: int) -> None | HTTPException:
   
    # init vars
    user_folder = f"UF__{user_id}"
    path_to_parent = FsEntityController._get_path_to_entity_parent(user_folder, file_field, fs_entity.path) # from STORAGE/ to folder_where_stored/


    # checks
    if not os.path.exists(fs_entity.path):
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Such {fs_entity.type} does not exist')
    


    # delete
    full_path = os.path.join(path_to_parent, fs_entity.name)

    if fs_entity.type == 'folder':
      shutil.rmtree(full_path)

    if fs_entity.type == 'file':
      os.remove(full_path)


    # edit structure
    FsEntityController._edit_parent_structure_json('del', fs_entity, path_to_parent)









  @staticmethod
  def rename_entity(fs_entity: FsEntityModel, file_field: Literal['mere', 'unmere', 'reserved'], user_id: int, new_name: str) -> None | HTTPException:

    # init vars
    user_folder = f"UF__{user_id}"
    path_to_parent = FsEntityController._get_path_to_entity_parent(user_folder, file_field, fs_entity.path) # from STORAGE/ to folder_where_stored/


    # checks
    if not re.match("[a-zA-z0-9\\\h.,()-_]", fs_entity.name):
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Unacceptable {fs_entity.type} name')
    if not os.path.exists(fs_entity.path):
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Such {fs_entity.type} does not exist')    



    # rename
    old_path  = os.path.join(path_to_parent, fs_entity.name)
    new_path  = os.path.join(path_to_parent, new_name)
    os.rename(old_path, new_path)


    # edit structure
    FsEntityController._edit_parent_structure_json('rename', fs_entity, path_to_parent, new_name=new_name)









  @staticmethod
  def get_fs_layer(path_to_layer: str, file_field: Literal['mere', 'unmere', 'reserved'], user_id: int) -> list | HTTPException:

    # init vars
    user_folder = f"UF__{user_id}"
    _entity_path = os.path.join(path_to_layer, '[layer]') # cuz last element in path will be removed # crunch
    path_to_parent = FsEntityController._get_path_to_entity_parent(user_folder, file_field, _entity_path) # from STORAGE/ to folder_where_stored/


    #checks
    if not os.path.exists(path_to_parent):
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Such path does not exist') 


    # get layer
    path_to_structure = os.path.join(path_to_parent, 'structure.json')

    with open(path_to_structure, 'r', encoding='utf8') as read_file:
      structure: list = json.load(read_file)


    return structure
  











  @staticmethod
  def create_new_user_folder(user_id: int) -> None:

    # init vars
    user_folder = f"UF__{user_id}"


    user_folder_path = os.path.join('../STORAGE', user_folder)

    # make user folder
    os.mkdir(user_folder_path)

    # make file fields and structures.json for them
    for file_field in ['MERE', 'UNMERE', 'RESERVED']:

      # # make dir
      os.mkdir( os.path.join(user_folder_path, file_field) )

      # # structure.json
      with open( os.path.join(user_folder_path, file_field, 'structure.json'), 'w', encoding='utf8') as new_file:
        json.dump([], new_file)



  