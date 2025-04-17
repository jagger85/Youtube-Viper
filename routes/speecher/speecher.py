from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.test import test_task
from flask import request
import uuid


bp_speecher = Blueprint("speecher", __name__)


@bp_speecher.route("/api/speecher")
@jwt_required()
def index():
    if not request.args.get("client_id"):
        return jsonify({"error": "client_id is required"}), 400
    elif not request.args.get("video_url"):
        return jsonify({"error": "video_url is required"}), 400
    else:
        client_id = request.args.get("client_id")
        video_url = request.args.get("video_url")
        prompt = request.args.get("prompt")
        task_id = uuid.uuid4()

        # Start the task
        task = test_task.delay(task_id, client_id, video_url, prompt)
        
    # Wait for the task to complete and get the result
    result = task.get(timeout=3000)  # Adjust timeout as needed
    
    
    return jsonify({"result": result})