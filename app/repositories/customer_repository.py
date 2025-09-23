from sqlalchemy.orm import Session
from app.models.customer import Customer
from app.schemas import CustomerCreate

class CustomerRepository:
    def __init__(self, db: Session):
      self.db = db
      
    def get_all(self):
        return self.db.query(Customer).all()
    
    def get_by_uuid(self, uuid: str):
        return self.db.query(Customer).filter(Customer.uuid == uuid).first()
    
    def get_by_fantasy_name(self, fantasy_name: str):
        return self.db.query(Customer).filter(Customer.fantasy_name == fantasy_name).first()
    
    def get_by_cnpj(self, cnpj: str):
        return self.db.query(Customer).filter(Customer.cnpj == cnpj).first()
    
    def create(self, customer: CustomerCreate) -> Customer:
        db_customer = Customer()
        db_customer.fantasy_name = customer.fantasy_name
        db_customer.cnpj = customer.cnpj
        db_customer.cnpj_formated = customer.cnpj_formated
        db_customer.address = customer.address
        
        self.db.add(db_customer)
        self.db.commit()
        self.db.refresh(db_customer)
        
        return db_customer