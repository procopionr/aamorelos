from database.database import Base
from sqlalchemy import Column, VARCHAR


class Region(Base):
    __tablename__ = "regions"
    id = Column(VARCHAR(10), primary_key=True)
    name = Column(VARCHAR(100), nullable=False)
