from flask import Flask
from routes import register_routes
from config import get_config

app = Flask(__name__)
config = get_config()

register_routes(app)


if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
