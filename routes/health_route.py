from flask import Blueprint

bp_health = Blueprint("health", __name__)

@bp_health.route("/health")
def health():
    return {"status": "ok"}

@bp_health.route("/ping")
def ping():
    return {"status": "pong"}