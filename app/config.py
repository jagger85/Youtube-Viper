import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    @property
    def JWT_SECRET_KEY(self):
        return os.getenv("JWT_SECRET_KEY")

    @property
    def CELERY_BROKER_URL(self):
        return os.getenv("CELERY_BROKER_URL")

    @property
    def CELERY_RESULT_BACKEND(self):
        return os.getenv("CELERY_RESULT_BACKEND")


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = "development"
    HOST = "0.0.0.0"
    PORT = 8080

class ProductionConfig(Config):
    DEBUG = False
    ENV = "production"

class StagingConfig(Config):
    DEBUG = False
    ENV = "staging"

def get_config():
    env = os.getenv("FLASK_ENV", "development")
    config_selector = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
        "staging": StagingConfig,
    }
    return config_selector.get(env, DevelopmentConfig)


