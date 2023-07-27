from pathlib import Path
import redis

ROOT = str(Path(__file__).parent.parent)

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
