from typing import Any, Dict, Optional

from repositories.group_repository import GroupRepository
from schemas.group import GroupResponseSchema


class GroupService:
    def __init__(self, repository: GroupRepository):
        self.repository = repository

    def get_filtered(
        self,
        municipality_id: str,
        type_id: Optional[int] = None,
        language_id: Optional[int] = None,
        gender_id: Optional[int] = None,
        smoking_allowed: Optional[int] = None,
        search: Optional[str] = None,
        skip: int = 0,
        limit: int = 100,
    ) -> Dict[str, Any]:
        groups = self.repository.get_filtered(
            municipality_id=municipality_id,
            type_id=type_id,
            language_id=language_id,
            gender_id=gender_id,
            smoking_allowed=smoking_allowed,
            search=search,
            skip=skip,
            limit=limit,
        )
        total = self.repository.count_filtered(
            municipality_id=municipality_id,
            type_id=type_id,
            language_id=language_id,
            gender_id=gender_id,
            smoking_allowed=smoking_allowed,
            search=search,
        )
        data = [GroupResponseSchema.from_model(g).model_dump() for g in groups]
        return {
            "ok": True,
            "total_registros": total,
            "skip": skip,
            "limit": limit,
            "data": data,
        }

    get_filtered_groups = get_filtered
