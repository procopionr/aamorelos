from typing import Any, Dict

from fastapi import HTTPException

from repositories.district_repository import DistrictRepository
from repositories.municipality_repository import MunicipalityRepository
from repositories.state_repository import StateRepository
from schemas.district import DistrictByStateResponseSchema


class DistrictByStateService:
    def __init__(
        self,
        district_repository: DistrictRepository,
        municipality_repository: MunicipalityRepository,
        state_repository: StateRepository,
    ):
        self.district_repository = district_repository
        self.municipality_repository = municipality_repository
        self.state_repository = state_repository

    def obtener_distritos_por_estado(self, state_id: str) -> Dict[str, Any]:
        state = self.state_repository.get_by_id(state_id)
        if not state:
            raise HTTPException(status_code=404, detail="Estado no encontrado")

        municipalities = self.municipality_repository.get_by_state_id(state_id)
        municipality_ids = [m.id for m in municipalities]

        districts = self.district_repository.get_by_municipality_ids(municipality_ids)
        data = [DistrictByStateResponseSchema.from_model(d).model_dump() for d in districts]
        return {
            "ok": True,
            "state_id": state_id,
            "total_registros": len(data),
            "data": data,
        }
