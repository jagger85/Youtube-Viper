import redis
import os

# Initialize the Redis client with environment-aware configuration
redis_client = redis.StrictRedis(
    host=os.getenv('REDIS_HOST', 'redis'),  # Use 'redis' service name in Docker, fallback to 'redis'
    port=int(os.getenv('REDIS_PORT', 6379)),  # Default Redis port
    db=int(os.getenv('REDIS_DB', 0)),        # Default database
    decode_responses=True,
    password=os.getenv('REDIS_PASSWORD')
)
