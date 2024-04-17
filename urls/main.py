# urls/main.py
from fastapi import APIRouter
from views.user import router as user_router

app_router = APIRouter()

app_router.include_router(user_router)
