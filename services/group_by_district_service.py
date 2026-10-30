from typing import Any, Dict

from fastapi import HTTPException

from repositories.district_repository import DistrictRepository
from repositories.group_repository import GroupRepository
from schemas.group import GroupByStateResponseSchema


class GroupByDistrictService:
    def __init__(self, group_repository: GroupRepository, district_repository: DistrictRepository):
        self.group_repository = group_repository
        self.district_repository = district_repository

    def obtener_grupos_por_distrito(self, district_id: str) -> Dict[str, Any]:
        district = self.district_repository.get_by_id(district_id)
        if not district:
            raise HTTPException(status_code=404, detail="Distrito no encontrado")

        groups = self.group_repository.get_by_district_id(district_id)
        data = [GroupByStateResponseSchema.from_model(g).model_dump() for g in groups]
        return {
            "ok": True,
            "district_id": district_id,
            "total_registros": len(data),
            "data": data,
        }
