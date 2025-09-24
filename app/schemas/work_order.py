from pydantic import BaseModel
from datetime import date

class WorkOrderBase(BaseModel):
    work_order_number: str
    calibration_date: date
    validate_date: date
    issue_date: date