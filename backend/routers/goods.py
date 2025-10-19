from fastapi import APIRouter, Form, Query, File, UploadFile

from backend.schemas.goods import GoodsResponseSchema
from backend.crud.goods import get_goods_by_url, get_goods_by_file

router = APIRouter(prefix="/goods", tags=["Goods APIs"])


@router.get("/", response_model=GoodsResponseSchema)
async def goods_by_url(
    page_index: int,
    image_url: str,
) -> GoodsResponseSchema:
    return await get_goods_by_url(page_index, image_url)


@router.post("/")
async def goods_by_file(page_index: int = Form(...), file: UploadFile = File(...)):
    binary_image = await file.read()
    return await get_goods_by_file(page_index, binary_image)
