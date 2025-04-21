from app.config import get_config
from app import create_app
from services import FileManager
import logging
from flask import redirect

logger = logging.getLogger(__name__)

config = get_config()

app = create_app()

file_manager = FileManager()

@app.route('/')
def home():
    return redirect("/api/docs")

@app.teardown_appcontext
def cleanup_temp_dir(exception):
    if file_manager:
        file_manager.cleanup_temp_dir()

if __name__ == "__main__":
    try:
        app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise
    finally:
        if file_manager:
            file_manager.cleanup_temp_dir()
