# no db lol
from fastapi import HTTPException
from ..models.User import UserModel


import json


class DbController:


  
  _path_to_users_json: str = '../STORAGE/users.json'
    







  @staticmethod
  def get_user(user_id: int) -> UserModel:

    # get users
    with open(DbController._path_to_users_json, 'r', encoding='utf8') as read_file:
      users: list = json.load(read_file)


    # pick user
    return [user for user in users if user['id'] == user_id][0]







  @staticmethod
  def get_user_by_name(name: str) -> UserModel:

    # get users
    with open(DbController._path_to_users_json, 'r', encoding='utf8') as read_file:
      users: list = json.load(read_file)


    # pick user
    return [user for user in users if user['name'] == name][0]








  @staticmethod
  def add_user(new_user: UserModel) -> int:

    # open
    with open(DbController._path_to_users_json, 'r', encoding='utf8') as read_file:
      users: list = json.load(read_file)


    # check if username is free + id
    # # thats why we need users to be sorted by id
    new_id = 1
    for user in users:
      if user['id'] == new_id:
        new_id += 1
      if user['name'] == new_user['name']:
        raise Exception('Username is already used')
      
    # still id
    new_user['id'] = new_id

    
    # add
    users.append(new_user)

    # SORT!!!
    users = sorted(users, key=lambda u: u['id'])


    # save
    with open(DbController._path_to_users_json, 'w', encoding='utf8') as write_file:
      json.dump(users, write_file, indent=4)

    # return user_id
    return new_id