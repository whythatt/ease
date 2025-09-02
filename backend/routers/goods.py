from fastapi import APIRouter
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
def parse_goods(image_url: str) -> GoodsResponseSchema:
    parser_data = fetch_data(image_url=image_url)
    return parser_data
