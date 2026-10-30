from typing import List, Optional
from sqlalchemy.orm import Session
import models


class EventoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[models.Evento]:
        return self.db.query(models.Evento).all()

    def get_by_id(self, evento_id: int) -> Optional[models.Evento]:
        return self.db.query(models.Evento).filter(models.Evento.id == evento_id).first()
