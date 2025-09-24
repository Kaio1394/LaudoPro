from fastapi import APIRouter, HTTPException
from app.services.work_order_service import WorkOrderService
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List
from app.db.database import get_db
from app.schemas.work_order import WorkOrderBase

work_order_router_v1 = APIRouter(prefix="/api/v1", tags=["Work Order"])

@work_order_router_v1.get("/work_order", response_model=List[WorkOrderBase])
def get_work_orders(db: Session = Depends(get_db)):
    service = WorkOrderService(db)
    return service.get_list_work_order()
        