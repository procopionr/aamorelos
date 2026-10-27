from typing import Any, Dict

from fastapi import HTTPException

from repositories.state_repository import StateRepository
from schemas.catalog import StateSchema


class StateService:
    def __init__(self, repository: StateRepository):
        self.repository = repository

    def get_states_by_country_id(self, country_id: str) -> Dict[str, Any]:
        parent = self.repository.get_parent_by_id(country_id)
        if not parent:
            raise HTTPException(status_code=404, detail="País no encontrado")
        states = self.repository.get_by_parent_id(country_id)
        data = [StateSchema.model_validate(s).model_dump() for s in states]
        return {
            "ok": True,
            "total_registros": len(data),
            "country_id": country_id,
            "data": data,
        }
