import os

from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE = os.getenv("DATABASE")
    ALGORITHM = os.getenv("ALGORITHM")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

settings = Settings()



