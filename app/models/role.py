from app.db.database import Base
from sqlalchemy import Column, String
import uuid

class Role(Base):
    __tablename__ = "roles"
    uuid = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
