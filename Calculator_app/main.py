#Import necessary libraries
import fastapi
import uvicorn
from typing import Optional

#Create FastAPI instance
api = fastapi.FastAPI()

@api.get('/')
def index():
    body = "<html>" \
           "<body style='padding: 10px;'>" \
           "<h1>Welcome to my API</h1>" \
           "<h2>FastAPI</h2>" \
           "<div>" \
           "Try it: <a href='/api/calculate?x=7&y=11'>/api/calculate?x=7&y=11</a>" \
           "</div>" \
           "</body>" \
           "</html>"
    return fastapi.responses.HTMLResponse(content=body)

@api.get('/api/calculate')
def calculate(x: int, y: int, z: Optional[int] = None):

    if z==0:
        return fastapi.responses.JSONResponse(content={"ERROR": "Error, z cannot be zero (0)"},
        status_code=400)

    value = x + y

    if z is not None:
        value /= z
    
    return {
        'x': x,
        'y': y,
        'z': z,
        'value': value
    }

uvicorn.run(api, port=8000, host='127.0.0.1')