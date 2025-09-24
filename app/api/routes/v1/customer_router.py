from fastapi import APIRouter, HTTPException
from app.services.customer_service import CustomerService
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List
from app.schemas.customer import CustomerBase
from app.db.database import get_db

customer_router_v1 = APIRouter(prefix="/api/v1", tags=["Customer"])

@customer_router_v1.get("/customer", response_model=List[CustomerBase])
def get_customer(db: Session = Depends(get_db)):
    service = CustomerService(db)
    return service.get_list_customers()

@customer_router_v1.post("/customer")
def create_customer(customer: CustomerBase, db: Session = Depends(get_db)):
    try:
        service = CustomerService(db)
        return service.create_customer(customer)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
        