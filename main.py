from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def root():
    return {"message": "Hello, World!"}


class HelloNameResp(BaseModel):
    message: str


@app.get('/hello/{name}', response_model=HelloNameResp)
def hello_name(name: str):
    return HelloNameResp(message=f"Hello {name}")
