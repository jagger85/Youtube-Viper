from app.config import get_config
from app import create_app

config = get_config()

app = create_app()

if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
