from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.auth import get_current_user

router = APIRouter()

# Template engine
templates = Jinja2Templates(directory="app/templates")


# =========================
# PUBLIC PAGES (không cần login)
# =========================

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


@router.get("/signin", response_class=HTMLResponse)
def signin(request: Request):
    return templates.TemplateResponse("signin.html", {"request": request})


@router.get("/signup", response_class=HTMLResponse)
def signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


# =========================
# USER PAGES (cần login)
# =========================

@router.get("/quiz", response_class=HTMLResponse)
async def quiz(request: Request, user=Depends(get_current_user)):
    return templates.TemplateResponse("quiz.html", {
        "request": request,
        "user": user
    })


@router.get("/result", response_class=HTMLResponse)
async def result(request: Request, user=Depends(get_current_user)):
    return templates.TemplateResponse("result.html", {
        "request": request,
        "user": user
    })


# =========================
# ADMIN PAGES (admin only)
# =========================

from app.routes.auth import admin_required


@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request, user=Depends(get_current_user)):

    admin_required(user)

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "user": user
    })


@router.get("/create-question", response_class=HTMLResponse)
async def create_question(request: Request, user=Depends(get_current_user)):

    admin_required(user)

    return templates.TemplateResponse("create_question.html", {
        "request": request,
        "user": user
    })
