from fastapi import APIRouter
import os

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

@base_router.get("/")
def welcome_message():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return {
        "message": f"Welcome to our first step in learning RAG.\nOur AppName: {app_name} and version: {app_version}"
    }
