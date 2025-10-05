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
    image_url: str, page: int, limit: int
) -> GoodsResponseSchema:
    encode_url = hashlib.md5(image_url.encode()).hexdigest()[:12]
    cached_goods = await redis_client.get(f"products:{encode_url}")

    if not cached_goods:
        cached_goods = await AsyncParser.fetch_all_pages(image_url)
        await redis_client.setex(
            f"products:{encode_url}", 300, json.dumps(cached_goods)
        )
        goods_list = cached_goods["products"]
    else:
        goods_list = json.loads(cached_goods)["products"]

    total = len(goods_list)
    start = (page - 1) * limit
    end = start + limit
    current_page_goods = goods_list[start:end]

    return {
        "products": current_page_goods,
        "page": page,
        "limit": limit,
        "total": total,
        "pages": math.ceil(total / limit),
        "has_more": page < math.ceil(total / limit),
    }


async def get_cached_goods_by_file(file: bytes):
    image_url = await AsyncParser.fetch_image_url_from_file(file)
    return {"image_url": image_url}
