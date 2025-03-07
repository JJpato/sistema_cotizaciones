import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    BIND_API_KEY = os.getenv("BIND_API_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False