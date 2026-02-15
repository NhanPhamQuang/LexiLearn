from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import web, auth, questions

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(web.router)
app.include_router(auth.router)
app.include_router(questions.router)
