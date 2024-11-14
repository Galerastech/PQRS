from fastapi import FastAPI

from backend import models

app = FastAPI(
    title="PQRS",
    docs_url="/app/docs",

)


@app.post("/auth/register/{id}", tags=["Auth"])
async def register(user: models.User):
    return {'username': 'bayron',
            'password': '123456',
            'email': 'rysh3n98@outlook.com'
            }
