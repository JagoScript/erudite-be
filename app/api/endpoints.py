from fastapi import APIRouter
from app.services.generator import generate_text
from app.models.schemas import TextGenerationRequest, TextGenerationResponse

router = APIRouter()

@router.post("/generate", response_model=TextGenerationResponse)
async def generate_text_endpoint(request: TextGenerationRequest):
    response = generate_text(request.prompt)
    return {"response": response}
 