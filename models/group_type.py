from database.database import Base
from sqlalchemy import Column, Integer, VARCHAR


class GroupType(Base):
    __tablename__ = "group_types"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100), unique=True, nullable=False)
