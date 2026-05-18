from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class Item(BaseModel):
    product_name: str
    quantity: int = Field(..., gte=1) # ต้องมีจำนวนอย่างน้อย 1 ชิ้น
    price: float

class OrderCreateInput(BaseModel):
    customer_id: str
    items: List[Item]
    total_amount: float