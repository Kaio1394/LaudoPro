from app.repositories.customer_repository import CustomerRepository
from app.schemas.customer import CustomerBase
from app.models.customer import Customer
from sqlalchemy.orm import Session

class CustomerService:
    def __init__(self, db: Session):
        self.repository = CustomerRepository(db)
        
    def create_customer(self, customer: CustomerBase) -> Customer:
        existing_customer_fantasy_name = self.repository.get_by_fantasy_name(customer.fantasy_name)
        if existing_customer_fantasy_name:
            raise ValueError(f"Customer already exists with fantasy name '{customer.fantasy_name}'.")
        existing_customer_cnpj = self.repository.get_by_cnpj(customer.cnpj)
        if existing_customer_cnpj:
            raise ValueError(f"Customer already exists with cnpj '{customer.cnpj}'.")
        return self.repository.create(customer)
    
    def get_list_customers(self) -> list[Customer]:
        return self.repository.get_all()