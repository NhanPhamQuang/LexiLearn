from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.get("/quiz", response_class=HTMLResponse)
def quiz(request: Request):
    return templates.TemplateResponse("quiz.html", {"request": request})

@router.get("/result", response_class=HTMLResponse)
def result(request: Request):
    return templates.TemplateResponse("result.html", {"request": request})
