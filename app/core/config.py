import os

class Settings:
    MODEL_NAME = os.getenv("MODEL_NAME", "unsloth/gemma-2b-it-bnb-4bit")

settings = Settings()