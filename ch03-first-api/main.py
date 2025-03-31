import fastapi
import uvicorn

api = fastapi.FastAPI()

def calculator():
    return 2*2

uvicorn.run(api, port=8000"
            