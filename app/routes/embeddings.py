from fastapi import APIRouter, HTTPException
from app.schemas import EmbeddingRequest, EmbeddingResponse
from langchain_ollama import OllamaEmbeddings
import os

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
router = APIRouter()

@router.post("/embeddings", response_model=EmbeddingResponse)
async def embeddings(request: EmbeddingRequest):
    try:
        model = OllamaEmbeddings(
            model=request.model,
            base_url=OLLAMA_URL
        )
        vector = model.embed_query(request.input)
        return EmbeddingResponse(
            model=request.model,
            embedding=vector,
            dimensions=len(vector)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))