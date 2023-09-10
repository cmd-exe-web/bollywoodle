import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    # Mongodb Configurations
    MONGODB_SETTINGS = {"db": "bollywoodle",
                        "host": os.environ.get("MONGO_URI")}
    COLLECTION_NAME = "videos"
