from pydantic import BaseModel
from . import seller

class Product(BaseModel):
    name: str
    description: str
    price: int

class ProductResponse(BaseModel):
    name: str
    description: str
    seller: seller.SellerResponse
    class Config:
        from_attributes = True
