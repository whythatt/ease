from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import goods
import uvicorn


app = FastAPI()

# Разрешить все origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все домены
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST, etc.)
    allow_headers=["*"],  # Разрешить все заголовки
)

app.include_router(goods.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
