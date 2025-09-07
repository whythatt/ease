from fastapi import APIRouter, Query
from fastapi import APIRouter, Depends
import redis

from schemas.goods import GoodsResponseSchema
from cruds.goods import get_cached_goods


router = APIRouter(prefix="/goods", tags=["Goods APIs"])


@router.get("/", response_model=GoodsResponseSchema)
def parse_goods(image_url: str) -> GoodsResponseSchema:
    return get_cached_goods(image_url)
