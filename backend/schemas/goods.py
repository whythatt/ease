from typing import List
from pydantic import BaseModel


class GoodsSchema(BaseModel):
    image_url: str | None
    title: str | None
    price: str | None
    shop_url: str | None
    shop_name: str | None
    shop_domain: str | None


class GoodsResponseSchema(BaseModel):
    products: List[GoodsSchema]
    page: int | None
    limit: int | None
    total: int | None
    pages: int | None
    has_more: bool | None
