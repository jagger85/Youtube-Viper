from flask import Flask
from routes import register_routes
from .config import get_config, Config
from flask_jwt_extended import JWTManager
from flask_sock import Sock

def create_app():
    app = Flask(__name__)
    config = get_config()
    jwt = JWTManager(app)
    app.config["JWT_SECRET_KEY"] = Config().JWT_SECRET_KEY
    app.config.update(
        CELERY_BROKER_URL=Config().CELERY_BROKER_URL,
        CELERY_RESULT_BACKEND=Config().CELERY_RESULT_BACKEND
    )

    register_routes(app)
    
    # Initialize Sock for WebSocket support
    sock = Sock(app)

    return app


