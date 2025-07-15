from fastapi import FastAPI
from dotenv import load_dotenv
from Routes import base

# Load env once here
load_dotenv("assets/.env")

app = FastAPI()
app.include_router(base.base_router)
