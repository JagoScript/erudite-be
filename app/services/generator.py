import torch
from app.core.config import settings
from transformers import pipeline
from torch.profiler import profile, record_function, ProfilerActivity
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(settings.MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(settings.MODEL_NAME, torch_dtype=torch.bfloat16, trust_remote_code=True)
model_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device_map="auto",
    # load_in_4bit=True,
)

def generate_text(prompt: str, max_new_tokens: int = 256) -> str:
    result = model_pipeline(
        prompt,
        max_new_tokens=max_new_tokens,
        num_return_sequences=1,
        temperature=0.7,
        top_p=0.95,
        use_cache=True,
        repetition_penalty=1.2, 
        do_sample=True,
    )
    response = result[0]["generated_text"]

    # Profiling
    with profile(activities=[ProfilerActivity.CPU, ProfilerActivity.CUDA]) as prof:
        with record_function("model_inference"):
            model_pipeline(prompt)
    print(prof.key_averages().table(sort_by="cuda_time_total"))

    # Remove prompt from response
    if response.startswith(prompt):
        response = response[len(prompt):].strip()
    
    return response

def truncate_to_last_sentence(response: str) -> str:
    sentences = response.split('.')
    if len(sentences) > 1:
        return sentences[-2] + '.'
    return response
