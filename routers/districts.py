from typing import Any, Dict

from dependencies import get_group_by_district_service
from fastapi import APIRouter, Depends
from schemas.group import GroupByDistrictListResponseSchema
from services.group_by_district_service import GroupByDistrictService

router = APIRouter(prefix="/api/v1/districts", tags=["Distritos"])


@router.get("/{district_id}/groups", response_model=GroupByDistrictListResponseSchema)
def get_groups_by_district(
    district_id: str,
    service: GroupByDistrictService = Depends(get_group_by_district_service),
) -> Dict[str, Any]:
    return service.obtener_grupos_por_distrito(district_id)
