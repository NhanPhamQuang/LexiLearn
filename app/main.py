from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import web

app = FastAPI()

# Mount static folder
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include routes
app.include_router(web.router)
