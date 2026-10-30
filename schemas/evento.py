from typing import Optional
from pydantic import BaseModel, ConfigDict


class EventoResponseSchema(BaseModel):
    id: str
    image: str
    alt: Optional[str] = None
    url: str
    title: str
    detail: str

    model_config = ConfigDict(from_attributes=True)


class EventoListResponseSchema(BaseModel):
    ok: bool
    total_registros: int
    data: list[EventoResponseSchema]
