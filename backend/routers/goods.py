from fastapi import APIRouter, Query
from fastapi import APIRouter, Depends

from schemas.goods import GoodsResponseSchema

import sys
from pathlib import Path

# Добавляем путь к папке python в sys.path
python_path = Path(__file__).parent.parent.parent  # /Users/niktar/python
sys.path.insert(0, str(python_path))

# Теперь импортируем абсолютным путем
from parser.main import fetch_data


router = APIRouter(prefix="/goods", tags=["Goods APIs"])


@router.get("/", response_model=GoodsResponseSchema)
def parse_goods(
    image_url: str,
    page: int = Query(1, ge=1, description="Page number"),
    per_page: int = Query(20, ge=1, le=100, description="Goods on the page"),
) -> GoodsResponseSchema:
    parser_data = fetch_data(image_url=image_url)
    all_goods = parser_data["products"]
    total_goods = len(all_goods)

    start_index = (page - 1) * per_page
    end_index = start_index + per_page

    paginated_goods = all_goods[start_index:end_index]

    return {"products": paginated_goods}
