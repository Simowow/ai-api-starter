from fastapi import APIRouter, HTTPException
from app.schemas import ModelsResponse, ModelInfo
import httpx

router = APIRouter()

@router.get("/models", response_model=ModelsResponse)
async def list_models():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://localhost:11434/api/tags")
            data = response.json()
        print(data)
        models = [
            ModelInfo(
                name=m["name"],
                size=f"{m['size'] / 1e9:.1f} GB",
                modified=str(m["modified_at"])
            )
            for m in data["models"]
        ]
        return ModelsResponse(models=models)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))