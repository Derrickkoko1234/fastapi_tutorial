# main.py
from fastapi import FastAPI
from urls.main import app_router

app = FastAPI()


app.include_router(app_router)
