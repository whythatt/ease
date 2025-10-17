import json
import hashlib
from backend.schemas.goods import GoodsResponseSchema
from backend.services.redis_goods import add_goods_to_cache, get_goods_cache
from parser.main import AsyncParser


async def get_goods_by_url(page_index: int, image_url: str) -> GoodsResponseSchema:
    redis_key = hashlib.md5(image_url.encode()).hexdigest()[:12]

    return await give_goods(f"products{redis_key}", image_url, page_index)


async def get_goods_by_file(page_index: int, file: bytes):
    redis_key = hashlib.sha256(file).hexdigest()[:12]
    start, end = page_index // 3 - 1, page_index // 3 - 1
    goods_data = await get_goods_cache(f"products{redis_key}", start, end)
    if goods_data == []:
        image_url = await AsyncParser.fetch_image_url_from_file(file)
        return await give_goods(f"products{redis_key}", image_url, page_index)
    else:
        goods_data = json.loads(goods_data[0])["products"]

    total = len(goods_data)
    page = page_index // 3

    return {
        "products": goods_data,
        "page": page,
        "total": total,
    }


async def give_goods(redis_key, image_url, page_index):
    start, end = page_index // 3 - 1, page_index // 3 - 1
    goods_data = await get_goods_cache(redis_key, start, end)
    if goods_data == []:
        goods_data = await AsyncParser.fetch_all_pages(image_url, page_index)
        await add_goods_to_cache(redis_key, json.dumps(goods_data))
        goods_data = goods_data["products"]
    else:
        goods_data = json.loads(goods_data[0])["products"]

    total = len(goods_data)
    page = page_index // 3

    return {
        "products": goods_data,
        "page": page,
        "total": total,
    }
