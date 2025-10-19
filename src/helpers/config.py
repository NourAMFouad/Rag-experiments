# all classes and another files use this file 

# need to inherite from BaseSettings, SettingsConfigDict
# create class(Settings) and write anoter one  for config to write the path pf .env 
# where the role of pydantic 
      # --> so you need to add the data from .env with it format for Validation So if user add any uncorrect datatype it appears the error data automatic

# add function in Settings class called get_settings() and return Settings object object 
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str

   # FILE_ALLOWED_EXTENTIONS: list
    FILE_ALLOWED_TYPES: list[str]
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int
    DEBUG: bool
   
    class Config:
        env_file = "assets/.env"

def get_settings():
    return Settings()