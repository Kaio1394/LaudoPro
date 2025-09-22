import uuid
from sqlalchemy import Column, String, Date
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base

class WorkOrder(Base):
    __tablename__ = "work_order"

    uuid = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    work_order_number = Column(String(20), unique=True, nullable=True)
    calibration_date = Column(Date, nullable=True)
    validate_date = Column(Date, nullable=True)
    issue_date = Column(Date, nullable=True)