from typing import List
from sqlalchemy.orm import Session

import models


class MunicipalityRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_state_id(self, state_id: str) -> List[models.Municipality]:
        return (
            self.db.query(models.Municipality)
            .filter(models.Municipality.state_id == state_id)
            .all()
        )
