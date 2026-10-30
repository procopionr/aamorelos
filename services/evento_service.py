from typing import Any, Dict
from repositories.evento_repository import EventoRepository
from schemas.evento import EventoResponseSchema


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
