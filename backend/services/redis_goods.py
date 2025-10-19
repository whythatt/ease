import asyncio
import json
import os
import redis.asyncio as redis
from dotenv import load_dotenv

# load_dotenv()

# redis_url = os.getenv("REDIS_URL")
# redis_client = redis.from_url(redis_url)
redis_client = redis.Redis()


async def get_goods_cache(key, start, end):
    cache = await redis_client.lrange(key, start, end)
    return cache


async def add_goods_to_cache(key, products: dict):
    await redis_client.rpush(key, products)
    await redis_client.expire(key, 600)
