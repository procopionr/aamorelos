from database.database import Base
from sqlalchemy import Column, ForeignKey, VARCHAR


class State(Base):
    __tablename__ = "states"
    id = Column(VARCHAR(10), primary_key=True)
    country_id = Column(VARCHAR(10), ForeignKey("countries.id"), nullable=False)
    name = Column(VARCHAR(100), nullable=False)
