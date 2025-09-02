from fastapi import FastAPI
from routers import goods


app = FastAPI()

app.include_router(goods.router)
