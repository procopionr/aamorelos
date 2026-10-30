from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class DistrictResponseSchema(BaseModel):
    id: str
    area_id: Optional[str] = None
    municipality_id: Optional[str] = None
    name: str
    district_number: Optional[int] = None
    creation_date: Optional[date] = None
    address: Optional[str] = None
    neighborhood: Optional[str] = None
    postal_code: Optional[str] = None
    reference: Optional[str] = None
    phone: Optional[str] = None
    service_hours: Optional[str] = None
    is_active: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)


class DistrictByStateResponseSchema(DistrictResponseSchema):
    municipality: Optional[str] = None
    area: Optional[str] = None

    @classmethod
    def from_model(cls, d) -> "DistrictByStateResponseSchema":
        base_data = DistrictResponseSchema.model_validate(d).model_dump()
        base_data.update({
            "municipality": getattr(getattr(d, "municipality", None), "name", None),
            "area": getattr(getattr(d, "area", None), "name", None),
        })
        return cls.model_validate(base_data)


class DistrictListResponseSchema(BaseModel):
    ok: bool
    area_id: str
    total_registros: int
    data: list[DistrictResponseSchema]


class DistrictByStateListResponseSchema(DistrictListResponseSchema):
    state_id: str
    area_id: Optional[str] = None
    data: list[DistrictByStateResponseSchema]


# Backward compatibility
DistrictSchema = DistrictResponseSchema
