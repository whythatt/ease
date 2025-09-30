import os
import redis
from dotenv import load_dotenv

import sys
import math
import json
import hashlib
from pathlib import Path

from backend.schemas.goods import GoodsResponseSchema
from parser.main import Parser


# load_dotenv()

# redis_url = os.getenv("REDIS_URL")
# redis_client = redis.Redis.from_url(redis_url)
redis_client = redis.Redis()


def get_cached_goods_by_url(
    image_url: str, page: int, limit: int
) -> GoodsResponseSchema:
    encode_url = hashlib.md5(image_url.encode()).hexdigest()[
        :12
    ]  # Кодирую url, чтобы он был короче
    cached_goods = redis_client.get(f"products:{encode_url}")

    if not cached_goods:
        cached_goods = Parser.fetch_data_by_url(image_url)
        redis_client.setex(f"products:{encode_url}", 300, json.dumps(cached_goods))
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


def get_cached_goods_by_file(file: bytes):
    image_url = Parser.fetch_image_url_from_file(file)
    return {"image_url": image_url}
