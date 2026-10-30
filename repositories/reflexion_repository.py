from typing import List, Optional
from sqlalchemy.orm import Session
import models


class ReflexionRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[models.Reflexion]:
        return self.db.query(models.Reflexion).all()

    def get_by_id(self, reflexion_id: str) -> Optional[models.Reflexion]:
        return self.db.query(models.Reflexion).filter(models.Reflexion.id == reflexion_id).first()
