from flask import Blueprint, jsonify
from app.video_process_task import video_process_task
from flask import request
import uuid

bp_speecher = Blueprint("speecher", __name__)

@bp_speecher.route("/api/speecher")
def index():
    if not request.args.get("client_id"):
        return jsonify({"error": "client_id is required"}), 400
    elif not request.args.get("video_url"):
        return jsonify({"error": "video_url is required"}), 400
    else:
        client_id = request.args.get("client_id")
        video_url = request.args.get("video_url")
        operation_type = request.args.get("operation_type")
                
        if request.args.get("prompt"):
            prompt = request.args.get("prompt")
        else:
            prompt = "Summarize the text in no more than 10 words"
        task_id = uuid.uuid4()

        # Start the task
        task = video_process_task.delay(task_id, client_id, video_url, prompt, operation_type)
        
    # Wait for the task to complete and get the result
    result = task.get(timeout=3000)
    
    
    return jsonify({"result": result})