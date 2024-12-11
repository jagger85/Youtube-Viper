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
    else:
        client_id = request.args.get("client_id")
        # Start the task
        task = test_task.delay(uuid.uuid4(), client_id)
        
    # Wait for the task to complete and get the result
    result = task.get(timeout=1000)  # Adjust timeout as needed
    
    # Return the result as a JSON response
    return jsonify({"result": result})

