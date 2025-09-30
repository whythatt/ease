from fastapi import APIRouter, Query, File, UploadFile

from backend.schemas.goods import GoodsResponseSchema
from backend.cruds.goods import get_cached_goods_by_url, get_cached_goods_by_file


router = APIRouter(prefix="/goods", tags=["Goods APIs"])


@router.get("/", response_model=GoodsResponseSchema)
def goods_by_url(
    image_url: str,
    page: int = Query(1, ge=1),
    limit: int = Query(30, ge=1, le=100),
) -> GoodsResponseSchema:
    return get_cached_goods_by_url(image_url, page, limit)


@router.post("/")
async def get_image_url(file: UploadFile = File(...)):
    binary_image = await file.read()
    return get_cached_goods_by_file(binary_image)
