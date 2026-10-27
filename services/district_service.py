from typing import Any, Dict

from fastapi import HTTPException

from repositories.area_repository import AreaRepository
from repositories.district_repository import DistrictRepository
from schemas.district import DistrictResponseSchema


class DistrictService:
    def __init__(self, district_repository: DistrictRepository, area_repository: AreaRepository):
        self.district_repository = district_repository
        self.area_repository = area_repository

    def obtener_distritos_por_area(self, area_id: str) -> Dict[str, Any]:
        area = self.area_repository.get_by_id(area_id)
        if not area:
            raise HTTPException(status_code=404, detail="Área no encontrada")

        districts = self.district_repository.get_by_area_id(area_id)
        data = [DistrictResponseSchema.model_validate(d).model_dump() for d in districts]

        return {
            "ok": True,
            "area_id": area_id,
            "total_registros": len(data),
            "data": data,
        }
