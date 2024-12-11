import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = os.getenv("PROJECT_NAME")
    VERSION = os.getenv("VERSION")
    DATABASE = os.getenv("DATABASE")
    ALGORITHM = os.getenv("ALGORITHM")
    SECRET_KEY  = os.getenv("SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

settings = Settings()
