from database.database import Base
from sqlalchemy import Column, VARCHAR


class Country(Base):
    __tablename__ = "countries"
    id = Column(VARCHAR(10), primary_key=True)
    name = Column(VARCHAR(100), unique=True, nullable=False)
    code = Column(VARCHAR(3), unique=True)
