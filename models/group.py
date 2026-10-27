from database.database import Base
from sqlalchemy import Column, ForeignKey, Integer, TEXT,Date, Numeric, VARCHAR
from sqlalchemy.orm import relationship


class Group(Base):
    __tablename__ = "groups"
    id = Column(VARCHAR(50), primary_key=True)
    district_id = Column(VARCHAR(50), ForeignKey("districts.id"), nullable=False)
    municipality_id = Column(
        VARCHAR(10), ForeignKey("municipalities.id"), nullable=False
    )
    type_id = Column(Integer, ForeignKey("group_types.id"))
    language_id = Column(Integer, ForeignKey("languages.id"))
    gender_id = Column(Integer, ForeignKey("group_genders.id"))

    name = Column(TEXT, nullable=False)
    creation_date = Column(Date)
    address = Column(TEXT)
    neighborhood = Column(VARCHAR(100))
    postal_code = Column(VARCHAR(10))
    reference = Column(TEXT)
    locality = Column(VARCHAR(100))
    cpr = Column(VARCHAR(50))
    schedule_monday = Column(TEXT)
    schedule_tuesday = Column(TEXT)
    schedule_wednesday = Column(TEXT)
    schedule_thursday = Column(TEXT)
    schedule_friday = Column(TEXT)
    schedule_saturday = Column(TEXT)
    schedule_sunday = Column(TEXT)
    schedule_observation = Column(TEXT)
    language_detail = Column(TEXT)
    smoking_allowed = Column(Integer)
    is_active = Column(Integer)
    latitude = Column(Numeric(10, 8))
    longitude = Column(Numeric(11, 8))
    smoking_text = Column(VARCHAR(50))

    district = relationship("District")
    municipality = relationship("Municipality")
    group_type = relationship("GroupType")
    language = relationship("Language")
    gender = relationship("GroupGender")
