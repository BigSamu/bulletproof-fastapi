import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.database.base import Base


class Seller(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    products = relationship("Product", back_populates='seller')
    created_on = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_on = Column(DateTime, nullable=True, onupdate=datetime.datetime.utcnow)

    def __str__(self):
        return f"id:{self.id}\n" f"username: {self.username}\n" f"email: {self.email}\n"
