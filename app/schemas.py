from pydantic import BaseModel
from typing import Optional, List

# ── Chat ──
class ChatRequest(BaseModel):
    model: str = "llama3"
    message: str
    system_prompt: Optional[str] = "You are a helpful assistant."
    temperature: Optional[float] = 0.7

class ChatResponse(BaseModel):
    model: str
    message: str
    done: bool

# ── Embeddings ──
class EmbeddingRequest(BaseModel):
    model: str = "nomic-embed-text"
    input: str

class EmbeddingResponse(BaseModel):
    model: str
    embedding: List[float]
    dimensions: int

# ── Models ──
class ModelInfo(BaseModel):
    name: str
    size: str
    modified: str

class ModelsResponse(BaseModel):
    models: List[ModelInfo]