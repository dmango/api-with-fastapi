from pydantic import BaseModel
from typing import Optional

from app.routers.urllink import URLLink


class Invoice(BaseModel):
    invoice_id: int
    invoice_date: str
    customer : Optional[URLLink] = None
