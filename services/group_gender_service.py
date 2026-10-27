from typing import Any, Dict

from repositories.group_gender_repository import GroupGenderRepository
from schemas.catalog import CatalogSchema


class GroupGenderService:
    def __init__(self, repository: GroupGenderRepository):
        self.repository = repository

    def get_all(self) -> Dict[str, Any]:
        items = self.repository.get_all()
        data = [CatalogSchema.model_validate(i).model_dump() for i in items]
        return {
            "ok": True,
            "total_registros": len(data),
            "data": data,
        }

    get_all_group_genders = get_all
