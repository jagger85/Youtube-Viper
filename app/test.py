import time
from app.celery_app import celery
from constants.speecher_task_status import SpeecherTaskStatus
from constants.message_types import MessageType
from app.redis import redis_client
from .audio_downloader import download_audio
from .speech_recognition import transcribe_audio
from .brain import summarize_long_text
import json

@celery.task
def test_task(task_id, client_id, video_url):
    # Convert UUID to string if it's a UUID object
    task_id = str(task_id)
    result = None 
    
    redis_client.set(f"speecher task id:{task_id}", SpeecherTaskStatus.PENDING.value)
    send_message(client_id, {'task_id': task_id, 'status': SpeecherTaskStatus.PENDING.value, 'type': MessageType.OPERATION_STATUS.value})

    redis_client.set(f"speecher task id:{task_id}", SpeecherTaskStatus.DOWNLOADING.value)
    send_message(client_id, {'task_id': task_id, 'status': SpeecherTaskStatus.DOWNLOADING.value, 'type': MessageType.OPERATION_STATUS.value})
    audio_file_path = download_audio(video_url)

    redis_client.set(f"speecher task id:{task_id}", SpeecherTaskStatus.TRANSCRIBING.value)
    send_message(client_id, {'task_id': task_id, 'status': SpeecherTaskStatus.TRANSCRIBING.value, 'type': MessageType.OPERATION_STATUS.value})
    transcribed_text = transcribe_audio(audio_file_path)

   # redis_client.set(f"speecher task id:{task_id}", SpeecherTaskStatus.PROCESSING.value)
   # send_message(client_id, {'task_id': task_id, 'status': SpeecherTaskStatus.PROCESSING.value, 'type': MessageType.OPERATION_STATUS.value})
   # result = summarize_long_text(transcribed_text)

    redis_client.set(f"speecher task id:{task_id}", SpeecherTaskStatus.COMPLETED.value)
    send_message(client_id, {'task_id': task_id, 'status': SpeecherTaskStatus.COMPLETED.value, 'type': MessageType.OPERATION_STATUS.value})
    return transcribed_text

def send_message(client_id, message):
    print(f"Sending message to client {client_id}: {message}")
    if redis_client.get(f"client:{client_id}") == "connected":
        # Publish the message to the client's Redis channel
        redis_client.publish(f"ws:client:{client_id}", json.dumps(message))
        print(f"Message sent to client {client_id}")
    else:
        print(f"Client {client_id} not found or disconnected")
