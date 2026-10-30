from typing import Any, Dict
from dependencies import get_reflexion_service
from fastapi import APIRouter, Depends
from schemas.reflexion import ReflexionListResponseSchema
from services.reflexion_service import ReflexionService

router = APIRouter(prefix="/api/v1/reflections", tags=["Reflexiones"])


@router.get("/", response_model=ReflexionListResponseSchema)
def get_reflections(service: ReflexionService = Depends(get_reflexion_service)) -> Dict[str, Any]:
    return service.get_all_reflexiones()
