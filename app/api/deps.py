from typing import Generator, Dict
from app.database.session import SessionLocal

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.config.config import settings

from sqlalchemy.orm import Session
from app import models

from jose import jwt, JWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = f"{settings.API_V1_STR}/auth/login")


# *******************************************************************************
# SESSION DATABASE DEPENDENCY
# *******************************************************************************

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# *******************************************************************************
# AUTHENTICATION DEPENDENCY
# *******************************************************************************


def verify_jwt_access_token(access_token: Dict, credentials_exception: HTTPException) -> str:
    
    # Try to decode JWT token
    try:
        payload = jwt.decode(
            access_token["value"], settings.JWT_SECRET_KEY, algorithms=[settings.JWT_SIGN_ALGORITHM]
        )
        user_id = payload.get("sub")
    
        # If no username id raise credentials exception (one passed as argument)
        if user_id is None:
            raise credentials_exception

    # If error found during decoding JWT (mismatch in signature), raise credentials
    # exception (one passed as argument)
    except JWTError:
        raise credentials_exception
    return user_id

def get_current_user(
    access_token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> models.Seller:

    # Create HTTP Exception for credentilas error

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    user = None
   
    # Verify Access Token (either JWT or Macaroon). If error found in verification,
    # raise credentials exception

    try:
        payload = jwt.decode(
            access_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username = payload.get("sub")
    
        # If no username id raise credentials exception (one passed as argument)
        if username is None:
            raise credentials_exception
        user = db.query(models.Seller).filter(models.Seller.username == username).first()
        return user

    # If error found during decoding JWT (mismatch in signature), raise credentials
    # exception (one passed as argument)
    except JWTError:
        raise credentials_exception
