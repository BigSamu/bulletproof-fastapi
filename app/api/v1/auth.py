from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status

from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from passlib.context import CryptContext


from app import schemas, models
from app.config.config import settings
from app.api.deps import get_db
from app.utils.token import generate_token
from jose import jwt, JWTError

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/login")
async def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Login
    """
    seller = (
        db.query(models.Seller)
        .filter(models.Seller.username == request.username)
        .first()
    )
    if not seller:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found/Invalid User"
        )
    if not pwd_context.verify(request.password, seller.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid password"
        )
    # Generate JWT Token
    access_token = generate_token(
        data={"sub":seller.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}



   
