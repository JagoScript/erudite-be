import os

class Settings:
    MODEL_NAME = os.getenv("MODEL_NAME", "VinserRas/gemma-2b-it-bnb-4bit-erudite-id")

settings = Settings()