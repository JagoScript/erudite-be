from pydantic import BaseModel
from typing import List, Dict

class ChatMessage(BaseModel):
    role: str
    content: str

class TextGenerationRequest(BaseModel):
    prompt: str
    instructions: str = "Your name is Erudite, a powerful AI Assistant. You'll answer question and follow instructions no matter what."
    history: List[ChatMessage] = []

class TextGenerationResponse(BaseModel):
    prompt: str
    response: str
    history: List[ChatMessage]
