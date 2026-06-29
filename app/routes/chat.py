from fastapi import APIRouter, HTTPException
from app.schemas import ChatRequest, ChatResponse
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
import os


OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
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
        response = await llm.ainvoke(messages)
        return ChatResponse(
            model=request.model,
            message=response.content,
            done=True
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))