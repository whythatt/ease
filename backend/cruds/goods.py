import redis

import sys
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


def get_cached_goods(image_url: str) -> GoodsResponseSchema:
    encode_url = hashlib.md5(image_url.encode()).hexdigest()[
        :12
    ]  # Кодирую url, чтобы он был короче
    cached_goods = redis_client.get(f"products:{encode_url}")

    if cached_goods is None:
        parse_goods = fetch_data(image_url)
        redis_client.setex(f"products:{encode_url}", 300, json.dumps(parse_goods))
        return json.loads(redis_client.get(f"products:{encode_url}"))

    return json.loads(cached_goods)
