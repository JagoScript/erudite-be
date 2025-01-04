from pydantic import BaseModel
from typing import List, Dict

class ChatMessage(BaseModel):
    role: str
    content: str

class TextGenerationRequest(BaseModel):
    prompt: str
    instructions: str = "Nama kamu Erudite, Asisten AI hebat yang dibuat oleh Tim Wikramaster & Jagoscript."
    history: List[ChatMessage] = []

class TextGenerationResponse(BaseModel):
    prompt: str
    response: str
    history: List[ChatMessage]
