from pydantic import BaseModel
from fastapi import FastAPI, Request


class InputModel(BaseModel):
    new_input: str
    context: str


app = FastAPI()


@app.post("/chat")
def respond(input: str, request: Request):
    pass
