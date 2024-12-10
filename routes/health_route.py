from flask import Blueprint

bp_health = Blueprint("health", __name__)

@bp_health.route("/api/health")
def health():
    return {"status": "ok"}

@bp_health.route("/api/ping")
def ping():
    return {"status": "pong"}