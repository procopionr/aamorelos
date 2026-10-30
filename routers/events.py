from typing import Any, Dict
from dependencies import get_evento_service
from fastapi import APIRouter, Depends
from schemas.evento import EventoListResponseSchema
from services.evento_service import EventoService

router = APIRouter(prefix="/api/v1/events", tags=["Eventos"])


@router.get("/", response_model=EventoListResponseSchema)
def get_events(service: EventoService = Depends(get_evento_service)) -> Dict[str, Any]:
    return service.get_all_eventos()


@router.get("/{evento_id}")
def get_event_by_id(
    evento_id: int,
    service: EventoService = Depends(get_evento_service),
) -> Dict[str, Any]:
    return service.get_evento_by_id(evento_id)
