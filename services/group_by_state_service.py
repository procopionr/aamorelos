from typing import Any, Dict

from fastapi import HTTPException

from repositories.group_repository import GroupRepository
from repositories.municipality_repository import MunicipalityRepository
from repositories.state_repository import StateRepository
from schemas.group import GroupByDistrictResponseSchema


class GroupByStateService:
    def __init__(
        self,
        group_repository: GroupRepository,
        municipality_repository: MunicipalityRepository,
        state_repository: StateRepository,
    ):
        self.group_repository = group_repository
        self.municipality_repository = municipality_repository
        self.state_repository = state_repository

    def obtener_grupos_por_estado(self, state_id: str) -> Dict[str, Any]:
        state = self.state_repository.get_by_id(state_id)
        if not state:
            raise HTTPException(status_code=404, detail="Estado no encontrado")

        municipalities = self.municipality_repository.get_by_state_id(state_id)
        municipality_ids = [m.id for m in municipalities]

        groups = self.group_repository.get_by_municipality_ids(municipality_ids)
        data = [GroupByDistrictResponseSchema.model_validate(g).model_dump() for g in groups]
        return {
            "ok": True,
            "state_id": state_id,
            "total_registros": len(data),
            "data": data,
        }
