from fastapi import APIRouter
from .endpoints import diagnostics, maintenance, tips

api_router = APIRouter()
api_router.include_router(diagnostics.router)
api_router.include_router(maintenance.router)
api_router.include_router(tips.router)