from pydantic import BaseModel, ConfigDict


class MunicipalitySchema(BaseModel):
    id: str
    name: str

    model_config = ConfigDict(from_attributes=True)
