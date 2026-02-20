# app/core/config.py
from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME", "Integration Hub")
    ENV = os.getenv("ENV", "dev")
    PORT = int(os.getenv("PORT", 8000))
    VERSION_GHL = os.getenv("VERSION")
    GHL_AUTH = os.getenv("AUTH")
    GHL_URL = os.getenv("BASE_URL")
    ID_LOCATION = os.getenv("LOCATION")

settings = Settings()
