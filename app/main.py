import uvicorn
from fastapi import FastAPI

from api.core import user_router

app = FastAPI(title="Bookshelf")


app.include_router(user_router)


@app.get("/")
async def hello_index():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8080,
        reload=True,
    )
