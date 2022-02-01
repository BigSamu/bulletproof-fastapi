from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app import schemas, models
from app.api.deps import get_db

router = APIRouter()
pwd_context= CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("", response_model=schemas.SellerResponse)
async def create_seller(request: schemas.Seller, db: Session = Depends(get_db)):
    """
    Add a Seller
    """
    hashed_password = pwd_context.hash(request.password)
    new_seller = models.Seller(username=request.username, email=request.email, password=hashed_password)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return request
