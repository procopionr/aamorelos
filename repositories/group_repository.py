from typing import List, Optional

from sqlalchemy import or_
from sqlalchemy.orm import Session, selectinload

import models


class GroupRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_district_id(self, district_id: str) -> List[models.Group]:
        return (
            self.db.query(models.Group)
            .options(
                selectinload(models.Group.group_type),
                selectinload(models.Group.language),
                selectinload(models.Group.gender),
                selectinload(models.Group.municipality),
                selectinload(models.Group.district),
            )
            .filter(models.Group.district_id == district_id)
            .all()
        )

    def get_by_municipality_ids(self, municipality_ids: List[str]) -> List[models.Group]:
        if not municipality_ids:
            return []
        return (
            self.db.query(models.Group)
            .options(
                selectinload(models.Group.group_type),
                selectinload(models.Group.language),
                selectinload(models.Group.gender),
                selectinload(models.Group.municipality),
                selectinload(models.Group.district),
            )
            .filter(models.Group.municipality_id.in_(municipality_ids))
            .all()
        )

    def get_filtered(
        self,
        municipality_id: str,
        type_id: Optional[int] = None,
        language_id: Optional[int] = None,
        gender_id: Optional[int] = None,
        smoking_allowed: Optional[int] = None,
        search: Optional[str] = None,
        skip: int = 0,
        limit: int = 100,
    ) -> List[models.Group]:
        query = self.db.query(models.Group).options(
            selectinload(models.Group.group_type),
            selectinload(models.Group.language),
            selectinload(models.Group.gender),
            selectinload(models.Group.municipality),
            selectinload(models.Group.district),
        )

        query = query.filter(models.Group.municipality_id == municipality_id)

        if type_id is not None:
            query = query.filter(models.Group.type_id == type_id)
        if language_id is not None:
            query = query.filter(models.Group.language_id == language_id)
        if gender_id is not None:
            query = query.filter(models.Group.gender_id == gender_id)
        if smoking_allowed is not None:
            query = query.filter(models.Group.smoking_allowed == smoking_allowed)

        if search is not None and search.strip() != "":
            search_term = search.strip()
            search_filter = or_(
                models.Group.address.ilike(f"%{search_term}%"),
                models.Group.neighborhood.ilike(f"%{search_term}%"),
                models.Group.postal_code.ilike(f"%{search_term}%"),
                models.Group.reference.ilike(f"%{search_term}%"),
                models.Group.locality.ilike(f"%{search_term}%"),
                models.Group.name.ilike(f"%{search_term}%"),
            )
            query = query.filter(search_filter)

        if limit < 0:
            limit = 100
        if limit > 500:
            limit = 500
        if skip < 0:
            skip = 0

        return query.offset(skip).limit(limit).all()

    def count_filtered(
        self,
        municipality_id: str,
        type_id: Optional[int] = None,
        language_id: Optional[int] = None,
        gender_id: Optional[int] = None,
        smoking_allowed: Optional[int] = None,
        search: Optional[str] = None,
    ) -> int:
        query = self.db.query(models.Group)

        query = query.filter(models.Group.municipality_id == municipality_id)

        if type_id is not None:
            query = query.filter(models.Group.type_id == type_id)
        if language_id is not None:
            query = query.filter(models.Group.language_id == language_id)
        if gender_id is not None:
            query = query.filter(models.Group.gender_id == gender_id)
        if smoking_allowed is not None:
            query = query.filter(models.Group.smoking_allowed == smoking_allowed)

        if search is not None and search.strip() != "":
            search_term = search.strip()
            search_filter = or_(
                models.Group.address.ilike(f"%{search_term}%"),
                models.Group.neighborhood.ilike(f"%{search_term}%"),
                models.Group.postal_code.ilike(f"%{search_term}%"),
                models.Group.reference.ilike(f"%{search_term}%"),
                models.Group.locality.ilike(f"%{search_term}%"),
                models.Group.name.ilike(f"%{search_term}%"),
            )
            query = query.filter(search_filter)

        return query.count()
