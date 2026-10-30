from typing import Any, Dict
from fastapi import HTTPException
from repositories.evento_repository import EventoRepository
from schemas.evento import EventoResponseSchema, EventoDetailResponseSchema


class EventoService:
    def __init__(self, repository: EventoRepository):
        self.repository = repository

    def get_all_eventos(self) -> Dict[str, Any]:
        eventos = self.repository.get_all()
        data = [EventoResponseSchema.model_validate(e).model_dump() for e in eventos]
        return {
            "ok": True,
            "total_registros": len(data),
            "data": data,
        }

    def get_evento_by_id(self, evento_id: int) -> Dict[str, Any]:
        evento = self.repository.get_by_id(evento_id)
        if not evento:
            raise HTTPException(status_code=404, detail="Evento no encontrado")
        return {
            "ok": True,
            "data": EventoDetailResponseSchema.model_validate(evento).model_dump(),
        }
