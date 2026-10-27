from typing import Any, Dict

from repositories.group_type_repository import GroupTypeRepository
from schemas.catalog import CatalogSchema


class GroupTypeService:
    def __init__(self, repository: GroupTypeRepository):
        self.repository = repository

    def get_all(self) -> Dict[str, Any]:
        items = self.repository.get_all()
        data = [CatalogSchema.model_validate(i).model_dump() for i in items]
        return {
            "ok": True,
            "total_registros": len(data),
            "data": data,
        }

    get_all_group_types = get_all
