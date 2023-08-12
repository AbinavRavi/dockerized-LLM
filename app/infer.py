from pydantic import BaseModel
from fastapi import FastAPI
from app.features.inference import Inference


class Input(BaseModel):
    prompt: str


class Output(BaseModel):
    response: str


app = FastAPI()


@app.post("/chat", response_model=Output)
def respond(input: Input):
    model = Inference()
    output = model.generate(input.prompt)
    return {"response": output}
