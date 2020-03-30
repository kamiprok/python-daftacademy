from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def root():
    return {"message": "Hello World during the coronavirus pandemic!"}


class HelloNameResp(BaseModel):
    message: str


@app.get('/hello/{name}', response_model=HelloNameResp)
def hello_name(name: str):
    return HelloNameResp(message=f"Hello {name}")


@app.get('/method')
def method_get():
    return {"method": "GET"}


@app.post('/method')
async def method_post():
    return {"method": "POST"}


@app.put('/method')
async def method_put():
    return {"method": "PUT"}


@app.delete('/method')
async def method_delete():
    return {"method": "DELETE"}


count: int = 0
@app.post('/patient')
async def patient(name: str, surename: str):
    global count
    count += 1
    return {"id": count, "patient": {"name": name, "surename": surename}}
