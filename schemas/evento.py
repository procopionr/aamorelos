from typing import Any, Optional
from pydantic import BaseModel, ConfigDict


class EventoResponseSchema(BaseModel):
    id: int
    tipo: str
    slug: str
    url: Optional[str] = None
    title: str
    subtitle: Optional[str] = None
    image: str
    alt: Optional[str] = None
    footer: Optional[str] = None
    epigrafe: Optional[str] = None
    kicker: Optional[str] = None
    frase_reflexion: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class EventoDetailResponseSchema(EventoResponseSchema):
    paragraphs: Optional[Any] = None
    resumen_fechas: Optional[Any] = None
    contacto: Optional[Any] = None
    bloques_itinerario: Optional[Any] = None


class EventoListResponseSchema(BaseModel):
    ok: bool
    total_registros: int
    data: list[EventoResponseSchema]
