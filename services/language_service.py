from typing import Any, Dict

from repositories.language_repository import LanguageRepository
from schemas.catalog import CatalogSchema


class LanguageService:
    def __init__(self, repository: LanguageRepository):
        self.repository = repository

    def get_all(self) -> Dict[str, Any]:
        items = self.repository.get_all()
        data = [CatalogSchema.model_validate(i).model_dump() for i in items]
        return {
            "ok": True,
            "total_registros": len(data),
            "data": data,
        }

    get_all_languages = get_all
