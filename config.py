import os

from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE = os.getenv("DATABASE")

settings = Settings()



