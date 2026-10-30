from typing import Any, Dict
from repositories.reflexion_repository import ReflexionRepository
from schemas.reflexion import ReflexionResponseSchema


class ReflexionService:
    def __init__(self, repository: ReflexionRepository):
        self.repository = repository

    def get_all_reflexiones(self) -> Dict[str, Any]:
        reflexiones = self.repository.get_all()
        data = [ReflexionResponseSchema.model_validate(r).model_dump() for r in reflexiones]
        return {
            "ok": True,
            "total_registros": len(data),
            "data": data,
        }
