from fastapi import APIRouter
from .items import router as items_router
from .users import router as users_router
from .orders import router as orders_router

api_router = APIRouter()
api_router.include_router(items_router, prefix="/items", tags=["Items"])
api_router.include_router(users_router, prefix="/users", tags=["Users"])
api_router.include_router(orders_router, prefix="/orders", tags=["Orders"])
