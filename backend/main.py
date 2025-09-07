from fastapi import FastAPI
from routers import goods
import uvicorn


app = FastAPI()

app.include_router(goods.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
