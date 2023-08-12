from llama_cpp import Llama
import time


class Inference:
    def __init__(self) -> None:
        self.model_path = "./models/llama-2-7b.ggmlv3.q4_0.bin"
        self.llm = Llama(self.model_path)

    def generate(self, prompt: str) -> str:
        output = self.llm(f"{prompt}", max_tokens=64, echo=True)
        generated_text = output["choices"][0]["text"]
        return generated_text


if __name__ == "__main__":
    start_time = time.time()
    inference = Inference()
    output = inference.generate("Can you write a small email for quitting")
    end_time = time.time() - start_time
    print(end_time)
    print(output["choices"][0]["text"])
