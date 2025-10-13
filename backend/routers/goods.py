from fastapi import APIRouter, Query, File, UploadFile

from backend.schemas.goods import GoodsResponseSchema
from backend.cruds.goods import get_cached_goods_by_url, get_cached_goods_by_file

router = APIRouter(prefix="/goods", tags=["Goods APIs"])


@router.get("/", response_model=GoodsResponseSchema)
async def goods_by_url(
    image_url: str,
    page_index: int,
) -> GoodsResponseSchema:
    return await get_cached_goods_by_url(image_url, page_index)


@router.post("/")
async def get_image_url(file: UploadFile = File(...)):
    binary_image = await file.read()
    return await get_cached_goods_by_file(binary_image)
