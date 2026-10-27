from typing import List, Optional
from sqlalchemy.orm import Session

import models


class StateRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_parent_id(self, country_id: str) -> List[models.State]:
        return (
            self.db.query(models.State)
            .filter(models.State.country_id == country_id)
            .order_by(models.State.name)
            .all()
        )

    def get_parent_by_id(self, country_id: str):
        return self.db.query(models.Country).filter(models.Country.id == country_id).first()

    def get_by_id(self, state_id: str) -> Optional[models.State]:
        return self.db.query(models.State).filter(models.State.id == state_id).first()

