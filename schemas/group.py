from datetime import date
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict


class GroupResponseSchema(BaseModel):
    id_grupo: str
    grupo: str
    fecha_creacion: Optional[date] = None
    domicilio: Optional[str] = None
    colonia: Optional[str] = None
    codigo_postal: Optional[str] = None
    referencia: Optional[str] = None
    localidad: Optional[str] = None
    cpr: Optional[str] = None

    horario_lunes: Optional[str] = None
    horario_martes: Optional[str] = None
    horario_miercoles: Optional[str] = None
    horario_jueves: Optional[str] = None
    horario_viernes: Optional[str] = None
    horario_sabado: Optional[str] = None
    horario_domingo: Optional[str] = None
    horario_observacion: Optional[str] = None

    lengua: Optional[str] = None
    fumar: Optional[int] = None
    activo: Optional[int] = None
    latitud: Optional[str] = None
    longitud: Optional[str] = None
    se_fuma: Optional[str] = None

    municipio: Optional[str] = None
    distrito: Optional[str] = None
    tipo: Optional[str] = None
    idioma: Optional[str] = None
    genero: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def from_model(cls, g) -> "GroupResponseSchema":
        data = {
            "id_grupo": g.id,
            "grupo": g.name,
            "fecha_creacion": g.creation_date,
            "domicilio": g.address,
            "colonia": g.neighborhood,
            "codigo_postal": g.postal_code,
            "referencia": g.reference,
            "localidad": g.locality,
            "cpr": g.cpr,
            "horario_lunes": g.schedule_monday,
            "horario_martes": g.schedule_tuesday,
            "horario_miercoles": g.schedule_wednesday,
            "horario_jueves": g.schedule_thursday,
            "horario_viernes": g.schedule_friday,
            "horario_sabado": g.schedule_saturday,
            "horario_domingo": g.schedule_sunday,
            "horario_observacion": g.schedule_observation,
            "lengua": g.language_detail,
            "fumar": g.smoking_allowed,
            "activo": g.is_active,
            "latitud": str(g.latitude) if g.latitude is not None else None,
            "longitud": str(g.longitude) if g.longitude is not None else None,
            "se_fuma": g.smoking_text,
            "municipio": g.municipality_id,
            "distrito": g.district_id,
            "tipo": getattr(getattr(g, "group_type", None), "name", None),
            "idioma": getattr(getattr(g, "language", None), "name", None),
            "genero": getattr(getattr(g, "gender", None), "name", None),
        }
        return cls.model_validate(data)


class GroupListResponseSchema(BaseModel):
    ok: bool
    total_registros: int
    skip: int
    limit: int
    data: list[GroupResponseSchema]


class GroupByDistrictResponseSchema(BaseModel):
    id: str
    district_id: str
    municipality_id: str
    type_id: Optional[int] = None
    language_id: Optional[int] = None
    gender_id: Optional[int] = None
    name: str
    creation_date: Optional[date] = None
    address: Optional[str] = None
    neighborhood: Optional[str] = None
    postal_code: Optional[str] = None
    reference: Optional[str] = None
    locality: Optional[str] = None
    cpr: Optional[str] = None
    schedule_monday: Optional[str] = None
    schedule_tuesday: Optional[str] = None
    schedule_wednesday: Optional[str] = None
    schedule_thursday: Optional[str] = None
    schedule_friday: Optional[str] = None
    schedule_saturday: Optional[str] = None
    schedule_sunday: Optional[str] = None
    schedule_observation: Optional[str] = None
    language_detail: Optional[str] = None
    smoking_allowed: Optional[int] = None
    is_active: Optional[int] = None
    latitude: Optional[Decimal] = None
    longitude: Optional[Decimal] = None
    smoking_text: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class GroupByDistrictListResponseSchema(BaseModel):
    ok: bool
    district_id: str
    total_registros: int
    data: list[GroupByDistrictResponseSchema]


class GroupByStateListResponseSchema(GroupByDistrictListResponseSchema):
    state_id: str
    district_id: str | None = None
    data: list[GroupByDistrictResponseSchema]
