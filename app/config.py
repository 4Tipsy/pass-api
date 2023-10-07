from dotenv import load_dotenv
import os

load_dotenv()






# GLOBALS
class Cfg:
  """Global vars"""

  APP_PORT: str = os.environ.get('APP_PORT')
  JWT_SECRET_KEY: str = os.environ.get('JWT_SECRET_KEY')

  DEFAULT_AVAILABLE_SPACE_IN_MB: str = os.environ.get('DEFAULT_AVAILABLE_SPACE_IN_MB')

  API_VERSION: str = os.environ.get('API_VERSION')







# DESCRIPTIONS FOR DOCS
class Desc:
  """Descriptions for auto docs"""




  MAIN_APP_DESC: str = f"""
  ![img][uwu]

  ### **PASS** is just a small app designed to store user files, nothing outstanding!
  ---
  
  **[!]** Each user has 3 "storages", aka `file_field`, the corresponding **field** is included in each request associated with the pass file-system.

  **[!]** Errors not related to the validation of the request, although marked with the code `400`, may return other codes (`401`, `403`, `...`), nevertheless, their body remains indelibly typed.

  **[!]** I don't store raw passwords! Only hashed ones, only security.

  **[!]** Some (many) requests require user authentication. Currently, i use authentication via `JWT`, which are transmitted with cookies. In requests requiring it, this is indicated in the description.

  ---
  My GitHub: [link!][my-github]  
  Source code API: [link!][source-code]  
  UwU: [link!][uwu]  

  ---
  [Swagger doc][doc-url]  
  [Redoc][redoc-url]  

  ---
  API routes are below. You can make requests from wherever, whether it is `curl`, our [**cli app (not made yet...)**][get-cli] or something else! Have fun <3


  [my-github]: https://github.com/4Tipsy
  [source-code]: https://github.com/4Tipsy/pass-server

  [uwu]: /api/utility-service/uwu

  [get-cli]: #

  [doc-url]: /api/docs
  [redoc-url]: /api/redoc
  """
