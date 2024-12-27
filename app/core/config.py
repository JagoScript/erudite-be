import os

class Settings:
    MODEL_NAME = os.getenv("MODEL_NAME", "unsloth/Llama-3.2-1B-Instruct-bnb-4bit")

settings = Settings()