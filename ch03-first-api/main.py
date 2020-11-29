from typing import Optional
import fastapi
from fastapi.responses import JSONResponse, 
import uvicorn

api = fastapi.FastAPI()

@api.get('/')
def index():
    body = "<html>" \
        "<body style='padding:10px'>" \
        "<h1>Welcome ot the API</h1>" \
        "<div>" \
        "Try it: <a href='/api/calculate?x=76&y=11'>/api/calculate?x=76&y=11</a>" \
        "</div>" \
        "</body>" \
        "</html>"

@api.get('/api/calculate')
def calculate(x: int, y: int, z: Optional[int] = None):

    if z is not None and z == 0:
        return JSONResponse(content={"error": "z must not be zero"},
                            status_code=400)

    value = x + y

    if z is not None:
        value /= z

    return {
        'value': value
    }


uvicorn.run(api, port=8000, host="127.0.0.1")
