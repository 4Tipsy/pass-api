from dotenv import load_dotenv
import os

load_dotenv()



# GLOBALS

class Cfg:
  APP_PORT = os.environ.get('APP_PORT')
  JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
  PASSWORD_ENCODE_KEY = os.environ.get('PASSWORD_ENCODE_KEY')

  DEFAULT_AVAILABLE_SPACE_IN_MB = os.environ.get('DEFAULT_AVAILABLE_SPACE_IN_MB')





# DESCRIPTIONS
