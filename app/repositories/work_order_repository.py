from sqlalchemy.orm import Session
from app.models.work_order import WorkOrder

class WorkOrderRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_all(self):
        return self.db.query(WorkOrder).all()
    