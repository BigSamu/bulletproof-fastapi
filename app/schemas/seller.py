from pydantic import BaseModel


class Seller(BaseModel):
    username: str
    email: str
    password: str


class SellerResponse(BaseModel):
    username: str
    email: str
    class Config:
        from_attributes = True
