import redis
import os

REDIS_URL = os.getenv("REDIS_URL")
r = redis.Redis.from_url(REDIS_URL)

# Test connection
try:
    r.ping()
    print("Redis connected successfully")
except Exception as e:
    print("Redis connection failed:", e)
