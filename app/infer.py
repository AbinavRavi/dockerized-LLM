from pydantic import BaseModel
from fastapi import FastAPI, Request


class InputModel(BaseModel):
    new_input: str
    context: str


app = FastAPI()


@app.post("/chat")
def respond(input: InputModel, request: Request):
    pass


# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf")

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
