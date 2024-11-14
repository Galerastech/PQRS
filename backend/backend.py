from fastapi import FastAPI

app = FastAPI(
    title="PQRS",
    docs_url="/app/docs",

)


@app.post("/auth/register", tags=["Auth"])
async def register(user:):
    return {'username': 'bayron',
            'password': '123456',
            'email': 'rysh3n98@outlook.com'
            }
