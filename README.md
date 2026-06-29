# AI API Starter

A FastAPI app wrapping Ollama with three endpoints — chat, embeddings, and models.

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /chat | Chat with any Ollama model |
| POST | /embeddings | Generate embeddings |
| GET | /models | List installed models |

## Requirements

- Python 3.11+
- Docker Desktop
- Ollama running locally

## Run locally

```bash
git clone https://github.com/yourusername/ai-api-starter
cd ai-api-starter
docker compose up --build
```

Open http://localhost:8000/docs

## Stack

- FastAPI
- LangChain Ollama
- Docker