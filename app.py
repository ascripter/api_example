from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/add")
def add(x: float, y: float) -> float:
    return x + y


@app.get("/subtract")
def subtract(x: float, y: float) -> float:
    return x - y


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9321)
