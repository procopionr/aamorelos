from typing import Any, Dict

from fastapi import HTTPException

from repositories.area_repository import AreaRepository
from repositories.municipality_repository import MunicipalityRepository
from repositories.state_repository import StateRepository
from schemas.catalog import AreaSchema


class AreaByStateService:
    def __init__(
        self,
        area_repository: AreaRepository,
        municipality_repository: MunicipalityRepository,
        state_repository: StateRepository,
    ):
        self.area_repository = area_repository
        self.municipality_repository = municipality_repository
        self.state_repository = state_repository

    def obtener_areas_por_estado(self, state_id: str) -> Dict[str, Any]:
        state = self.state_repository.get_by_id(state_id)
        if not state:
            raise HTTPException(status_code=404, detail="Estado no encontrado")

        municipalities = self.municipality_repository.get_by_state_id(state_id)
        result = []
        for municipality in municipalities:
            areas = self.area_repository.get_by_municipality_id(municipality.id)
            for area in areas:
                result.append(AreaSchema.model_validate(area).model_dump())
        return {
            "ok": True,
            "state_id": state_id,
            "total_registros": len(result),
            "data": result,
        }
