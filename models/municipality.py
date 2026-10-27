from database.database import Base
from sqlalchemy import Column, ForeignKey, Integer, VARCHAR


class Municipality(Base):
    __tablename__ = "municipalities"
    id = Column(VARCHAR(10), primary_key=True)
    state_id = Column(VARCHAR(10), ForeignKey("states.id"), nullable=False)
    name = Column(VARCHAR(100), nullable=False)
