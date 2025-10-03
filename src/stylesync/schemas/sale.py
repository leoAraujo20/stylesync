from pydantic import BaseModel, ConfigDict
from datetime import date

class Sale(BaseModel):
    sale_date: date
    product_id: str
    quantity: int
    total_price: float

    model_config = ConfigDict(arbitrary_types_allowed=True)
