import os
import math
import json
import hashlib
import redis.asyncio as redis
from dotenv import load_dotenv
from backend.schemas.goods import GoodsResponseSchema
from parser.main import AsyncParser

load_dotenv()

redis_url = os.getenv("REDIS_URL")
redis_client = redis.from_url(redis_url)
# redis_client = redis.Redis()


async def get_cached_goods_by_url(
    image_url: str, page_index: int
) -> GoodsResponseSchema:
    encode_url = hashlib.md5(image_url.encode()).hexdigest()[:12]
    cached_goods = await redis_client.lrange(
        f"products:{encode_url}", page_index // 3 - 1, page_index // 3 - 1
    )

    if cached_goods == []:
        cached_goods = await AsyncParser.fetch_all_pages(image_url, page_index)
        await redis_client.rpush(f"products:{encode_url}", json.dumps(cached_goods))
        await redis_client.expire(f"products:{encode_url}", 600)
        cached_goods = cached_goods["products"]
    else:
        cached_goods = json.loads(cached_goods[0])["products"]

    total = len(cached_goods)
    page = page_index // 3

    return {
        "products": cached_goods,
        "page": page,
        "total": total,
    }


async def get_cached_goods_by_file(file: bytes):
    image_url = await AsyncParser.fetch_image_url_from_file(file)
    return {"image_url": image_url}
