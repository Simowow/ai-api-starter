from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.schemas import ChatRequest
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
import os

router = APIRouter()
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")

@router.post("/chat")
async def chat(request: ChatRequest):
    try:
        llm = ChatOllama(
            model=request.model,
            temperature=request.temperature,
            base_url=OLLAMA_URL,
            num_predict=256
        )
        messages = [
            SystemMessage(content=request.system_prompt),
            HumanMessage(content=request.message)
        ]

        async def token_generator():
            async for chunk in llm.astream(messages):
                if chunk.content:
                    yield chunk.content

        return StreamingResponse(
            token_generator(),
            media_type="text/plain"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))