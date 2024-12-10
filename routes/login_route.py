from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
import os
from dotenv import load_dotenv

load_dotenv()

bp_login = Blueprint("login", __name__)


@bp_login.route("/api/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    USER = os.getenv("LOGIN_USER")
    PASS = os.getenv("LOGIN_PASSWORD")

    if username == USER and password == PASS:
        access_token = create_access_token(identity=username, expires_delta=None)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401
