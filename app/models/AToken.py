from pydantic import BaseModel



class ATokenModel:
  """Model for jwt auth token"""
  id: int
  epoch: int