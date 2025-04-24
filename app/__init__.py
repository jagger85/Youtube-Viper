from flask import Flask
from routes import register_routes
from .config import get_config, Config
from flask_sock import Sock
from services import FileManager
from flask_cors import CORS


import logging

logger = logging.getLogger(__name__)

def create_temp_dir():
    file_manager = FileManager()
    temp_dir = file_manager.create_temp_dir()
    logger.info(f"Created temporary directory: {temp_dir}")
    return temp_dir
    

def create_app():
    app = Flask(__name__)
    CORS(app)
    config = get_config()
    
    temp_dir = create_temp_dir()
    app.config["TEMP_DIR"] = temp_dir
    
    app.config.update(
        CELERY_BROKER_URL=Config().CELERY_BROKER_URL,
        CELERY_RESULT_BACKEND=Config().CELERY_RESULT_BACKEND
    )

    register_routes(app)
    
    # Initialize Sock for WebSocket support
    sock = Sock(app)

    return app


