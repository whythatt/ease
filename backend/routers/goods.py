from fastapi import APIRouter
from fastapi import APIRouter, Depends


router = APIRouter(prefix="/goods", tags=["Goods APIs"])

@router.get('/')
async def parse_goods():
    pass