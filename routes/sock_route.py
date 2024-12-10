from flask_sock import Sock
import uuid
from app.redis import redis_client
import json

def register_sock_routes(app):
    sock = Sock(app)

    @sock.route('/echo')
    def echo(ws):
        client_id = str(uuid.uuid4())
        redis_client.set(f"client:{client_id}", "connected")
        print(f"Client {client_id} connected")
        ws.send(f"Welcome to the server, your client ID is {client_id}")
        
        # Subscribe to a Redis channel for this client
        pubsub = redis_client.pubsub()
        pubsub.subscribe(f"ws:client:{client_id}")
        
        try:
            # Start a thread to listen for Redis messages
            for message in pubsub.listen():
                if message['type'] == 'message':
                    data = message['data']
                    ws.send(data)
                    
            while True:
                data = ws.receive()
                print(f"Received from {client_id}: {data}")
                ws.send(f"Echo from server: {data}")
        except Exception as e:
            print(f"Connection error with client {client_id}: {e}")
        finally:
            print(f"Client {client_id} disconnected")
            redis_client.delete(f"client:{client_id}")
            pubsub.unsubscribe()
