from pydantic import BaseModel


class Customer(BaseModel):
    customer_id: str
    country: str
