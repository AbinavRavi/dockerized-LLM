import transformers
import torch
from transformers import AutoTokenizer
from transformers import pipeline

name = "mosaicml/mpt-7b-chat"

config = transformers.AutoConfig.from_pretrained(name, trust_remote_code=True)
config.max_seq_len = 4096  # (input + output) tokens can now be up to 4096

model = transformers.AutoModelForCausalLM.from_pretrained(
    name, config=config, trust_remote_code=True
)

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neox-20b")


pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, device="cuda:0")

with torch.autocast("cuda", dtype=torch.bfloat16):
    print(
        pipe(
            "Here is a recipe for vegan banana bread:\n",
            max_new_tokens=100,
            do_sample=True,
            use_cache=True,
        )
    )
