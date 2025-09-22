from fastapi import APIRouter, Query

from schemas.goods import GoodsResponseSchema
from cruds.goods import get_cached_goods


router = APIRouter(prefix="/goods", tags=["Goods APIs"])


@router.get("/", response_model=GoodsResponseSchema)
def parse_goods(
    image_url: str,
    page: int = Query(1, ge=1),
    limit: int = Query(30, ge=1, le=100)
) -> GoodsResponseSchema:
    return get_cached_goods(image_url, page, limit)
