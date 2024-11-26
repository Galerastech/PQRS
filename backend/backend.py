from fastapi import FastAPI
from backend.routes import auth
from fastapi import APIRouter

router = APIRouter()

app = FastAPI(
    title="PQRS",
    docs_url="/app/docs",

)

app.include_router(auth.router, tags=["Auth"])
