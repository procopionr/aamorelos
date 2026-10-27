from typing import Any, Dict

from repositories.region_repository import RegionRepository
from schemas.catalog import RegionSchema


class RegionService:
    def __init__(self, repository: RegionRepository):
        self.repository = repository

    def get_all_regions(self) -> Dict[str, Any]:
        regions = self.repository.get_all()
        data = [RegionSchema.model_validate(r).model_dump() for r in regions]
        return {
            "ok": True,
            "total_registros": len(data),
            "data": data,
        }
