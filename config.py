import os

class Config:
    pass

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
