
from fastapi import FastAPI
from app.routes import api_router

app = FastAPI(title="FastAPI Official Tutorial")
app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

