import torch
from transformers import LlamaForCausalLM, LlamaTokenizer


class Inference:
    def __init__(self) -> None:
        self.snapshot_path = "./models"
        self.model = LlamaForCausalLM.AutoModelForCausalLM.from_pretrained(
            self.snapshot_path,
            quantized=True,
            torch_dtype=torch.bfloat16,
            low_cpu_mem_usage=True,
            trust_remote_code=True,
        )
        self.tokenizer = LlamaTokenizer.AutoTokenizer.from_pretrained(self.snapshot_path)

    def generate(self, prompt: str) -> str:
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        output = self.model.generate(input_ids, max_length=100)
        # Convert the generated output back to text
        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return generated_text
