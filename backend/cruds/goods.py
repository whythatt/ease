import redis

import sys
import math
import json
import hashlib
from pathlib import Path

from schemas.goods import GoodsResponseSchema

# Добавляем путь к папке python в sys.path
python_path = Path(__file__).parent.parent.parent  # /Users/niktar/python
sys.path.insert(0, str(python_path))

# Теперь импортируем абсолютным путем
from parser.main import fetch_data


redis_client = redis.Redis()


def get_cached_goods(image_url: str, page: int, limit: int) -> GoodsResponseSchema:
    encode_url = hashlib.md5(image_url.encode()).hexdigest()[
        :12
    ]  # Кодирую url, чтобы он был короче
    cached_goods = redis_client.get(f"products:{encode_url}")

    if not cached_goods:
        cached_goods = fetch_data(image_url)
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
