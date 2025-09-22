import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base

class SafetyValve(Base):
    __tablename__ = "safety_valve"

    uuid = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    description = Column(String(100), nullable=False)
    tag = Column(String(50), nullable=False)
    manufacturer = Column(String(100), nullable=False)
    serial_number = Column(String(100), nullable=True)
    model = Column(String(100), nullable=True)
    size = Column(String(20), nullable=False)
    actuation_range = Column(String(50), nullable=False)
