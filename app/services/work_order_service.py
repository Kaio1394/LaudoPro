from sqlalchemy.orm import Session
from app.repositories.work_order_repository import WorkOrderRepository
from app.models.work_order import WorkOrder

class WorkOrderService:
    def __init__(self, db: Session):
        self.repository = WorkOrderRepository(db)
        
    def get_list_work_order(self) -> list[WorkOrder]:
        return self.repository.get_all()