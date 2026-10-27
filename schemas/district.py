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


class DistrictListResponseSchema(BaseModel):
    ok: bool
    area_id: str
    total_registros: int
    data: list[DistrictResponseSchema]


# Backward compatibility
DistrictSchema = DistrictResponseSchema
