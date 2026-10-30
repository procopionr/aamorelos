from database.database import Base
from sqlalchemy import Column, Date, ForeignKey, Integer, TEXT, VARCHAR
from sqlalchemy.orm import relationship


class District(Base):
    __tablename__ = "districts"
    id = Column(VARCHAR(50), primary_key=True)
    area_id = Column(VARCHAR(10), ForeignKey("areas.id"), nullable=False)
    municipality_id = Column(
        VARCHAR(10), ForeignKey("municipalities.id"), nullable=False
    )
    name = Column(TEXT, nullable=False)
    district_number = Column(Integer)
    creation_date = Column(Date)
    address = Column(TEXT)
    neighborhood = Column(VARCHAR(100))
    postal_code = Column(VARCHAR(10))
    reference = Column(TEXT)
    phone = Column(VARCHAR(50))
    service_hours = Column(TEXT)
    is_active = Column(Integer)

    municipality = relationship("Municipality")
    area = relationship("Area")
