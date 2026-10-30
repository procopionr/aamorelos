from typing import Optional
from pydantic import BaseModel, ConfigDict


class ReflexionResponseSchema(BaseModel):
    id: str
    slug: str
    title: str
    subtitle: str
    image: str
    alt: str
    url: str
    description: str

    model_config = ConfigDict(from_attributes=True)


class ReflexionListResponseSchema(BaseModel):
    ok: bool
    total_registros: int
    data: list[ReflexionResponseSchema]
