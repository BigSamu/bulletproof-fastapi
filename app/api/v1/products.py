from typing import Any, List

from fastapi import APIRouter, Depends, Response, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, models
from ..deps import get_db, get_current_user

router = APIRouter()


@router.get("", response_model=List[schemas.ProductResponse])
async def get_all_products(
    db: Session = Depends(get_db),
    current_user: schemas.Seller = Depends(get_current_user),
):
    """
    Get all products
    """
    all_products = db.query(models.Product).all()
    return all_products


@router.get("/{id}", response_model=schemas.ProductResponse)
async def get_one_product(id: int, response: Response, db: Session = Depends(get_db), current_user: schemas.Seller = Depends(get_current_user),):
    """
    Get one product
    """
    selected_product = db.query(models.Product).filter(models.Product.id == id).first()
    if not selected_product:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Product not found")
    return selected_product


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_product(request: schemas.Product, db: Session = Depends(get_db), current_user: schemas.Seller = Depends(get_current_user),):
    """
    Add a product
    """
    new_product = models.Product(
        name=request.name,
        description=request.description,
        price=request.price,
        seller_id=current_user.id,
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return request


@router.put("/{id}")
async def update_product(
    id: int, request: schemas.Product, db: Session = Depends(get_db), current_user: schemas.Seller = Depends(get_current_user),
):
    """
    Update a product
    """
    selected_product = db.query(models.Product).filter(models.Product.id == id)
    if not selected_product.first():
        pass
    selected_product.update(request.dict())
    db.commit()
    return request


@router.delete("/{id}")
async def remove_product(id: int, db: Session = Depends(get_db), current_user: schemas.Seller = Depends(get_current_user),):
    """
    Delete a product
    """
    db.query(models.Product).filter(models.Product.id == id).delete(
        synchronize_session=False
    )
    db.commit()
    return {"Product Deleted"}
