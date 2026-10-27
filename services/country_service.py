from typing import Any, Dict

from pydantic import BaseModel, ConfigDict

from repositories.country_repository import CountryRepository


class CountrySchema(BaseModel):
    id: str
    name: str
    code: str | None = None

    model_config = ConfigDict(from_attributes=True)


class CountryService:
    def __init__(self, repository: CountryRepository):
        self.repository = repository

    def get_all_countries(self) -> Dict[str, Any]:
        countries = self.repository.get_all()
        data = [CountrySchema.model_validate(p).model_dump() for p in countries]
        return {
            "ok": True,
            "total_registros": len(data),
            "data": data,
        }
