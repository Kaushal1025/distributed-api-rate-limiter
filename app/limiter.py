import time
from app.redis_client import redis_client

RATE_LIMIT = 5
WINDOW_SIZE = 60  # seconds

def check_rate_limit(client_id):
    key = f"rate_limit:{client_id}"

    request_count = redis_client.get(key)

    if request_count is None:
        redis_client.setex(key, WINDOW_SIZE, 1)
        return True, RATE_LIMIT - 1

    request_count = int(request_count)

    if request_count >= RATE_LIMIT:
        return False, 0

    redis_client.incr(key)
    return True, RATE_LIMIT - (request_count + 1)