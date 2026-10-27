from database.database import Base
from sqlalchemy import Column, Integer, VARCHAR


class GroupGender(Base):
    __tablename__ = "group_genders"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100), unique=True, nullable=False)
