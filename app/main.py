from fastapi import FastAPI
from app.routes import chat, embeddings, models

app = FastAPI(
    title="AI API Starter",
    description="A FastAPI app wrapping Ollama — chat, embeddings, and models",
    version="1.0.0"
)

# ── Register routes ──
app.include_router(chat.router, tags=["Chat"])
app.include_router(embeddings.router, tags=["Embeddings"])
app.include_router(models.router, tags=["Models"])

@app.get("/")
async def root():
    return {"status": "running", "docs": "/docs"}

@app.get("/health")
async def health():
    return {"status": "ok"}