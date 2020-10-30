from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



@app.post("/compile/")
def compile_smartpy(code: str):
    return code
