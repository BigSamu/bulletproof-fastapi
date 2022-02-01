from fastapi import APIRouter

from . import products
from . import sellers
from . import auth


api_router = APIRouter()
api_router.include_router(products.router, prefix="/products", tags=["Products"])
api_router.include_router(sellers.router, prefix="/sellers", tags=["Sellers"])
api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
