from flask_sock import Sock
import uuid
from app.redis import redis_client
from constants import MessageType

import json
import threading

def register_sock_routes(app):
    sock = Sock(app)

    @sock.route('/echo')
    def echo(ws):
        client_id = str(uuid.uuid4())
        redis_client.set(f"client:{client_id}", "connected")
        print(f"Client {client_id} connected")
        ws.send(json.dumps({
            "type": MessageType.LOGIN.value,
            "client_id": client_id
        }))
        
        # Subscribe to a Redis channel for this client
        pubsub = redis_client.pubsub()
        pubsub.subscribe(f"ws:client:{client_id}")
        
        def redis_listener():
            for message in pubsub.listen():
                if message['type'] == 'message':
                    data = message['data']
                    ws.send(data)
        
        # Start Redis listener in a separate thread
        redis_thread = threading.Thread(target=redis_listener)
        redis_thread.daemon = True
        redis_thread.start()
        
        try:
            while True:
                # Handle WebSocket messages from client
                data = ws.receive()
                try:
                    message = json.loads(data)
                    print(f"Received from {client_id}: {message}")
                    if message['type'] == 'test':
                        print(f"the test message is: {message['content']}")
                    
                    # Send response back to client
                    response = {
                        "type": "response",
                        "content": f"Server received: {message['content']}"
                    }
                    ws.send(json.dumps(response))
                    
                except json.JSONDecodeError:
                    print(f"Invalid JSON received from {client_id}: {data}")
                    ws.send(json.dumps({
                        "type": "error",
                        "content": "Invalid JSON format"
                    }))
                
        except Exception as e:
            print(f"Connection error with client {client_id}: {e}")
        finally:
            print(f"Client {client_id} disconnected")
            redis_client.delete(f"client:{client_id}")
            pubsub.unsubscribe()
