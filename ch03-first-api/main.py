from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import uvicorn

api = FastAPI()


@api.get("/")
def index():
    body = (
        "<html>"
        "<body style='padding:10px'>"
        "<h1>Welcome ot the API</h1>"
        "<div>"
        "Try it: <a href='/api/calculate?x=76&y=11'>/api/calculate?x=76&y=11</a>"
        "</div>"
        "</body>"
        "</html>"
    )
    return HTMLResponse(body)


@api.get("/api/calculate")
def calculate(x: int, y: int, z: Optional[int] = None):

    if z is not None and z == 0:
        raise HTTPException(400, "z must not be zero")        

    value = x + y

    if z is not None:
        value /= z

    return {"value": value}


if __name__ == "__main__":
    uvicorn.run(api, port=8000, host="127.0.0.1")
