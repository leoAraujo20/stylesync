from pydantic import BaseModel
from typing import Optional

class Produt(BaseModel):
    nome: str
    price: float
    description: Optional[str] = None
    stock: int