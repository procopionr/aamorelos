from database.database import Base
from sqlalchemy import Column, Integer, Text, VARCHAR
from sqlalchemy.dialects.postgresql import JSONB


class Evento(Base):
    __tablename__ = "eventos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(VARCHAR(50), nullable=False)
    slug = Column(VARCHAR(100), unique=True, nullable=False)
    url = Column(Text)
    title = Column(VARCHAR(255), nullable=False)
    subtitle = Column(VARCHAR(255))
    image = Column(Text, nullable=False)
    alt = Column(VARCHAR(255))
    footer = Column(VARCHAR(255))
    epigrafe = Column(Text)
    kicker = Column(VARCHAR(100))
    frase_reflexion = Column(Text)
    paragraphs = Column(JSONB)
    resumen_fechas = Column(JSONB)
    contacto = Column(JSONB)
    bloques_itinerario = Column(JSONB)
