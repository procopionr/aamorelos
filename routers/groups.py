from typing import Any, Dict, Optional

from dependencies import get_group_service
from fastapi import APIRouter, Depends, Query
from schemas.group import GroupListResponseSchema
from services.group_service import GroupService

router = APIRouter(prefix="/api/v1/groups", tags=["Grupos"])


@router.get("/", response_model=GroupListResponseSchema)
def get_groups(
    municipality_id: str = Query(..., min_length=1),
    type_id: Optional[int] = Query(None),
    language_id: Optional[int] = Query(None),
    gender_id: Optional[int] = Query(None),
    smoking_allowed: Optional[int] = Query(None),
    search: Optional[str] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    service: GroupService = Depends(get_group_service),
) -> Dict[str, Any]:
    return service.get_filtered(
        municipality_id=municipality_id,
        type_id=type_id,
        language_id=language_id,
        gender_id=gender_id,
        smoking_allowed=smoking_allowed,
        search=search,
        skip=skip,
        limit=limit,
    )
