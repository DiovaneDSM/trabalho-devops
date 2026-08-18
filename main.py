from fastapi import FastAPI
import random


app = FastAPI()

@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}

@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": "deu certo",
            "num_aleatorio": random.randint(0, 20000)}
