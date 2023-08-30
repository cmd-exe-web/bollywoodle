import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    # Mongodb Configurations
    MONGO_URI=os.environ.get("MONGO_URI")
    MONGODB_SETTINGS = {"db": "bollywoodle", "host": os.environ.get("MONGO_URI")}
    COLLECTION_NAME = "videos"