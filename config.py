import os

from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE = os.getenv("DATABASE")
    ALGORITHM = os.getenv("ALGORITHM")

settings = Settings()



