from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@router.get("/platform", response_class=HTMLResponse)
def platform(request: Request):
    return templates.TemplateResponse("platform.html", {"request": request})


@router.get("/architecture", response_class=HTMLResponse)
def architecture(request: Request):
    return templates.TemplateResponse("architecture.html", {"request": request})


@router.get("/about", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


@router.get("/quiz", response_class=HTMLResponse)
def quiz(request: Request):
    return templates.TemplateResponse("quiz.html", {"request": request})


@router.get("/result", response_class=HTMLResponse)
def result(request: Request):
    return templates.TemplateResponse("result.html", {"request": request})

@router.get("/signin", response_class=HTMLResponse)
def signin(request: Request):
    return templates.TemplateResponse("signin.html", {"request": request})


@router.get("/signup", response_class=HTMLResponse)
def signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})
