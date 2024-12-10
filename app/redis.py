import redis

# Initialize the Redis client with default values
redis_client = redis.StrictRedis(
    host='localhost',  # Default host
    port=6379,         # Default port
    db=0,              # Default database
    decode_responses=True
)
