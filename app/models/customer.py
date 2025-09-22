from app.db.database import Base
from sqlalchemy import Column, String
import uuid

class Customer(Base):
    __tablename__ = "customers"
    uuid = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    fantasy_name = Column(String, nullable=False, index=True)
    cnpj = Column(String(14), nullable=False, index=True)
    cnpj_formated = Column(String(18), nullable=False, index=True)
    address = Column(String, nullable=False)