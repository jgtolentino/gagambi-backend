from fastapi import APIRouter
from app.api.v1 import auth, users, retail, analytics, prd, ph_awards

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["scout-analytics"])
api_router.include_router(prd.router, prefix="/prd", tags=["documentation"])
api_router.include_router(retail.router, prefix="/retail", tags=["retail-data"])
api_router.include_router(ph_awards.router, prefix="/ph-awards", tags=["ph-awards"])