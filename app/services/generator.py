import torch
from app.core.config import settings
from transformers import pipeline
from transformers import AutoModelForCausalLM, AutoTokenizer
from typing import List, Dict

tokenizer = AutoTokenizer.from_pretrained(settings.MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(settings.MODEL_NAME, torch_dtype=torch.bfloat16, trust_remote_code=True)
model_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device_map="auto",
)

def format_prompt(prompt: str, instructions: str = "", history: List[Dict[str, str]] = []) -> str:
    if instructions:
        instructions = f"<start_of_turn>system\n{instructions}<end_of_turn>\n"
    
    history_str = ""
    for message in history[-10:]:  # Truncate history to the last 10 messages
        history_str += f"<start_of_turn>{message['role']}\n{message['content']}<end_of_turn>\n"
    
    return f"{instructions}{history_str}<start_of_turn>user\n{prompt}<end_of_turn>\n<start_of_turn>model\n"

def generate_text(prompt: str, max_new_tokens: int = 256, instructions: str = "", history: List[Dict[str, str]] = []) -> Dict[str, str]:
    formatted_prompt = format_prompt(prompt, instructions, history)
    result = model_pipeline(
        formatted_prompt,
        max_new_tokens=max_new_tokens,
    )
    response = result[0]["generated_text"]

    # Remove prompt from response
    if response.startswith(formatted_prompt):
        response = response[len(formatted_prompt):].strip()
    
    # Update the history with the new interaction
    history.append({"role": "user", "content": prompt})
    history.append({"role": "bot", "content": response})

    return {
        "prompt": prompt,
        "response": response,
        "history": history  # Return the updated history
    }
