import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Bookshelf")


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
