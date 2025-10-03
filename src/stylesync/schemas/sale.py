from pydantic import BaseModel, ConfigDict
from datetime import datetime

class Sale(BaseModel):
    sale_date: datetime
    product_id: str
    quantity: int
    total_price: float

    model_config = ConfigDict(arbitrary_types_allowed=True)
