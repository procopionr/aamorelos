from typing import Any, Dict

from dependencies import get_area_by_state_service, get_district_by_state_service, get_group_by_state_service
from fastapi import APIRouter, Depends
from schemas.catalog import AreaListResponseSchema
from schemas.district import DistrictByStateListResponseSchema
from schemas.group import GroupByStateListResponseSchema
from services.area_by_state_service import AreaByStateService
from services.district_by_state_service import DistrictByStateService
from services.group_by_state_service import GroupByStateService

router = APIRouter(prefix="/api/v1/states", tags=["Estados"])


@router.get("/{state_id}/areas", response_model=AreaListResponseSchema)
def get_areas_by_state(
    state_id: str,
    service: AreaByStateService = Depends(get_area_by_state_service),
) -> Dict[str, Any]:
    return service.obtener_areas_por_estado(state_id)


@router.get("/{state_id}/districts", response_model=DistrictByStateListResponseSchema)
def get_districts_by_state(
    state_id: str,
    service: DistrictByStateService = Depends(get_district_by_state_service),
) -> Dict[str, Any]:
    return service.obtener_distritos_por_estado(state_id)


@router.get("/{state_id}/groups", response_model=GroupByStateListResponseSchema)
def get_groups_by_state(
    state_id: str,
    service: GroupByStateService = Depends(get_group_by_state_service),
) -> Dict[str, Any]:
    return service.obtener_grupos_por_estado(state_id)
