from fastapi import  FastAPI
from backend.routes import auth,tenant
from fastapi import APIRouter


router = APIRouter()


app = FastAPI(
    title="PQRS",
    docs_url='/app/docs',
)


app.include_router(auth.router)
app.include_router(tenant.router)