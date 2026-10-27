from typing import Any, Dict

from fastapi import HTTPException

from repositories.area_repository import AreaRepository
from repositories.region_repository import RegionRepository
from schemas.catalog import AreaSchema


class AreaService:
    def __init__(self, area_repository: AreaRepository, region_repository: RegionRepository):
        self.area_repository = area_repository
        self.region_repository = region_repository

    def obtener_areas_por_region(self, region_id: str) -> Dict[str, Any]:
        region = self.region_repository.get_by_id(region_id)
        if not region:
            raise HTTPException(status_code=404, detail="Región no encontrada")

        areas = self.area_repository.get_by_region_id(region_id)
        data = [AreaSchema.model_validate(a).model_dump() for a in areas]
        return {
            "ok": True,
            "region_id": region_id,
            "total_registros": len(data),
            "data": data,
        }
