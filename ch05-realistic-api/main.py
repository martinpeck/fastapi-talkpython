import fastapi
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles

api = fastapi.FastAPI()

api.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates('templates')


@api.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {'request': request})
    
    
if __name__ == "__main__":
    uvicorn.run(api, port=8000, host="127.0.0.1")