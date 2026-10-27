from typing import Optional

from pydantic import BaseModel, ConfigDict


class CatalogSchema(BaseModel):
    id: int | str
    name: str

    model_config = ConfigDict(from_attributes=True)


class CatalogListResponseSchema(BaseModel):
    ok: bool
    total_registros: int
    data: list[CatalogSchema]


class CountrySchema(BaseModel):
    id: str
    name: str

    model_config = ConfigDict(from_attributes=True)


class CountryListResponseSchema(BaseModel):
    ok: bool
    total_registros: int
    data: list[CountrySchema]


class RegionSchema(BaseModel):
    id: str
    name: str

    model_config = ConfigDict(from_attributes=True)


class RegionListResponseSchema(BaseModel):
    ok: bool
    total_registros: int
    data: list[RegionSchema]


class StateSchema(BaseModel):
    id: str
    name: str
    country_id: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class StateListResponseSchema(BaseModel):
    ok: bool
    total_registros: int
    country_id: Optional[str] = None
    data: list[StateSchema]


class AreaSchema(BaseModel):
    id: str
    region_id: Optional[str] = None
    municipality_id: Optional[str] = None
    name: str
    creation_date: Optional[str] = None
    address: Optional[str] = None
    neighborhood: Optional[str] = None
    postal_code: Optional[str] = None
    reference: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    service_hours: Optional[str] = None
    is_active: Optional[int] = None
    website: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class AreaListResponseSchema(BaseModel):
    ok: bool
    region_id: Optional[str] = None
    total_registros: int
    data: list[AreaSchema]


class GroupGenderSchema(CatalogSchema):
    pass


class GroupTypeSchema(CatalogSchema):
    pass


class LanguageSchema(CatalogSchema):
    pass
