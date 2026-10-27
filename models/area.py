from database.database import Base
from sqlalchemy import Column, Date, ForeignKey, Integer, TEXT, VARCHAR


class Area(Base):
    __tablename__ = "areas"
    id = Column(VARCHAR(10), primary_key=True)
    region_id = Column(VARCHAR(10), ForeignKey("regions.id"))
    municipality_id = Column(
        VARCHAR(10), ForeignKey("municipalities.id"), nullable=False
    )
    name = Column(TEXT, nullable=False)
    creation_date = Column(Date)
    address = Column(TEXT)
    neighborhood = Column(VARCHAR(100))
    postal_code = Column(VARCHAR(10))
    reference = Column(TEXT)
    phone = Column(VARCHAR(50))
    email = Column(VARCHAR(100))
    service_hours = Column(TEXT)
    is_active = Column(Integer)
    website = Column(TEXT)
