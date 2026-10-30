from database.database import Base
from sqlalchemy import Column, Text, VARCHAR


class Evento(Base):
    __tablename__ = "eventos"
    id = Column(VARCHAR(50), primary_key=True)
    image = Column(Text, nullable=False)
    alt = Column(VARCHAR(255))
    url = Column(Text, nullable=False)
    title = Column(VARCHAR(255), nullable=False)
    detail = Column(Text, nullable=False)
