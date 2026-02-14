from fastapi import APIRouter, HTTPException, Form
from fastapi.responses import RedirectResponse
from app.database import user_collection
from app.models import User
from app.auth import (
    hash_password,
    verify_password,
    create_access_token,
)

import re

router = APIRouter()


# =========================
# SIGN UP
# =========================
@router.post("/signup")
async def signup(
    full_name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
):
    full_name = full_name.strip()
    email = email.strip().lower()
    password = password.strip()

    if len(password) < 4:
        raise HTTPException(status_code=400, detail="Password too short")

    existing_user = await user_collection.find_one({"email": email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        full_name=full_name,
        email=email,
        hashed_password=hash_password(password),
        role="user"  # mặc định
    )

    await user_collection.insert_one(user.dict())

    return RedirectResponse(url="/signin", status_code=303)


# =========================
# SIGN IN
# =========================
@router.post("/signin")
async def signin(
    email: str = Form(...),
    password: str = Form(...)
):
    email = email.strip().lower()
    password = password.strip()

    user = await user_collection.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not verify_password(password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # 👉 đưa role vào token
    token = create_access_token({
        "sub": user["email"],
        "role": user["role"]
    })

    # 👉 phân quyền redirect
    if user["role"] == "admin":
        redirect_url = "/dashboard"
    else:
        redirect_url = "/quiz"

    response = RedirectResponse(url=redirect_url, status_code=303)
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        max_age=60 * 60 * 24,
        samesite="lax"
    )

    return response


# =========================
# LOGOUT
# =========================
@router.get("/logout")
async def logout():
    response = RedirectResponse(url="/", status_code=303)
    response.delete_cookie("access_token")
    return response
