import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base


class Product(Base):

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    seller_id = Column(Integer, ForeignKey('sellers.id'), nullable=False)
    seller = relationship("Seller", back_populates='products')
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, nullable=True, onupdate=datetime.datetime.utcnow)

    def __str__(self):
        return (
            f"id:{self.id}\n"
            f"name: {self.name}\n"
            f"description: {self.description}\n"
            f"price: {self.price}"
        )
