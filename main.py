from fastapi import FastAPI
from app.routers import items, users
import uvicorn

app = FastAPI(
    title="FastAPI App",
    description="A basic FastAPI application",
    version="0.1.0"
)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])

@app.get("/", tags=["root"])
async def root():
    return {"message": "Welcome to FastAPI application"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 